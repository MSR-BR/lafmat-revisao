"""Collect public channel metadata and local thumbnails; never download video files.

Default: check both public Atom feeds. --full also checks each channel's entire
video/stream catalog using the pinned development dependency in requirements-youtube.txt.
Existing records are retained when YouTube removes or hides an upload.
"""
import argparse
import concurrent.futures
import datetime as dt
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "dist/assets/videos.js"
CACHE = ROOT / ".cache/youtube-sync"
PREFIX = "window.youtubeCatalog = "
CHANNELS = [
    {"id": "UC6WvDFTjgFk3Q35q4mpaL0g", "name": "Lafmatnetwork", "url": "https://www.youtube.com/@Lafmatnetwork"},
    {"id": "UCfiQBBY25mMqY4seHB_fCmg", "name": "GI MATEFUN", "url": "https://www.youtube.com/@gimatefun5035"},
]
VIDEO_ID = re.compile(r"[A-Za-z0-9_-]{11}\Z")
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015"}


def read_url(url):
    for attempt in range(3):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.9"})
            with urllib.request.urlopen(request, timeout=35) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code == 429:
                raise RuntimeError("YouTube requested a pause (HTTP 429); keep the existing catalog and retry a later scheduled run") from error
            if attempt == 2:
                raise
            time.sleep(1 + attempt)
        except Exception:
            if attempt == 2:
                raise
            time.sleep(1 + attempt)


def read_catalog():
    if not CATALOG.exists():
        return {"schemaVersion": 1, "channels": CHANNELS, "videos": []}
    source = CATALOG.read_text()
    if not source.startswith(PREFIX):
        raise ValueError("Unexpected catalog format; refusing to overwrite it")
    return json.loads(source[len(PREFIX):].strip().removesuffix(";"))


def feed_inventory(channel):
    feed = ET.fromstring(read_url("https://www.youtube.com/feeds/videos.xml?channel_id=" + channel["id"]))
    feed_id = feed.findtext("yt:channelId", namespaces=NS)
    author_url = feed.findtext("a:author/a:uri", namespaces=NS)
    if feed_id not in [channel["id"], channel["id"][2:]] or author_url != "https://www.youtube.com/channel/" + channel["id"]:
        raise ValueError("Unexpected YouTube feed identity")
    entries = []
    for entry in feed.findall("a:entry", NS):
        if entry.findtext("yt:channelId", namespaces=NS) != channel["id"]:
            raise ValueError("Feed entry belongs to a different channel")
        entries.append({"id": entry.findtext("yt:videoId", namespaces=NS),
                        "title": entry.findtext("a:title", namespaces=NS), "channelId": channel["id"]})
    if not entries:
        raise ValueError("Empty feed; existing catalog was not changed")
    return entries


def full_inventory(channel):
    try:
        import yt_dlp
    except ImportError as error:
        raise RuntimeError("--full requires Python 3.11+ and requirements-youtube.txt") from error
    with yt_dlp.YoutubeDL({"extract_flat": True, "skip_download": True, "quiet": True, "no_warnings": True}) as client:
        data = client.extract_info(channel["url"], download=False)
    if data.get("channel_id") != channel["id"]:
        raise ValueError("Channel identity differs from the approved source")
    entries = []

    def walk(item):
        if item.get("_type") == "playlist":
            for child in item.get("entries", []):
                walk(child)
        elif item.get("ie_key") == "Youtube":
            entries.append({"id": item["id"], "title": item["title"], "channelId": channel["id"]})
    walk(data)
    if not entries:
        raise ValueError("Empty channel inventory; existing catalog was not changed")
    return entries


def player_json(html):
    match = re.search(r"(?:var\s+)?ytInitialPlayerResponse\s*=\s*", html)
    if not match:
        raise ValueError("YouTube player metadata unavailable; refusing to guess dates")
    return json.JSONDecoder().raw_decode(html[match.end():])[0]


def video_metadata(item):
    video_id = item["id"]
    if not VIDEO_ID.fullmatch(video_id):
        raise ValueError("Invalid YouTube video ID")
    cache_path = CACHE / "watch" / (video_id + ".json")
    if cache_path.exists():
        cached = json.loads(cache_path.read_text())
        if cached["video"]["channelId"] == item["channelId"]:
            return cached["video"]
    player = player_json(read_url("https://www.youtube.com/watch?v=" + video_id).decode())
    details = player.get("videoDetails", {})
    if details.get("videoId") != video_id or details.get("channelId") != item["channelId"]:
        raise ValueError("Video identity unavailable or outside the two approved channels: " + video_id)
    micro = player.get("microformat", {}).get("playerMicroformatRenderer", {})
    live = micro.get("liveBroadcastDetails", {})
    if details.get("isUpcoming") or live.get("isLiveNow"):
        return None
    published = micro.get("publishDate") or micro.get("uploadDate")
    if not published:
        raise ValueError("Missing publication date: " + video_id)
    instant = dt.datetime.fromisoformat(published.replace("Z", "+00:00"))
    if instant.tzinfo is None:
        instant = instant.replace(tzinfo=dt.timezone.utc)
    if instant > dt.datetime.now(dt.timezone.utc):
        return None
    video = {"id": video_id, "title": details["title"].strip(), "channelId": item["channelId"],
             "publishedAt": instant.astimezone(dt.timezone.utc).isoformat(),
             "publishedDate": instant.date().isoformat(), "url": "https://www.youtube.com/watch?v=" + video_id,
             "duration": int(details.get("lengthSeconds", 0)), "image": "assets/video-thumbnails/" + video_id + ".jpg"}
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(json.dumps({"inventoryTitle": item["title"], "video": video}, ensure_ascii=False) + "\n")
    return video


def thumbnail(video):
    target = ROOT / "dist" / video["image"]
    if target.exists():
        return
    image = read_url("https://i.ytimg.com/vi/" + video["id"] + "/mqdefault.jpg")
    if not image.startswith(b"\xff\xd8") or len(image) < 500:
        raise ValueError("Invalid thumbnail: " + video["id"])
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(image)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true")
    parser.add_argument("--inventory", type=Path, help="Import a previously verified full inventory for initial collection")
    args = parser.parse_args()
    CACHE.mkdir(parents=True, exist_ok=True)
    old = read_catalog()
    # The committed catalog is also a metadata cache. A fresh computer must not
    # request every historical watch page just because .cache/ is absent.
    watch_cache = CACHE / "watch"
    watch_cache.mkdir(parents=True, exist_ok=True)
    approved_channels = {channel["id"] for channel in CHANNELS}
    for video in old["videos"]:
        if not VIDEO_ID.fullmatch(video["id"]) or video["channelId"] not in approved_channels:
            raise ValueError("Existing catalog contains an unapproved source")
        target = watch_cache / (video["id"] + ".json")
        if not target.exists():
            target.write_text(json.dumps({"inventoryTitle": video["title"], "video": video}, ensure_ascii=False) + "\n")
    inventory = []
    for channel in CHANNELS:
        inventory.extend(feed_inventory(channel))
        if args.full:
            inventory.extend(full_inventory(channel))
    if args.inventory:
        aliases = {"lafmat": CHANNELS[0]["id"], "gimatefun": CHANNELS[1]["id"]}
        for item in json.loads(args.inventory.read_text()):
            inventory.append({"id": item["id"], "title": item["title"], "channelId": aliases[item["source"]]})
    candidates = {}
    for item in inventory:
        if not VIDEO_ID.fullmatch(item.get("id") or "") or not item.get("title"):
            raise ValueError("Invalid inventory record; catalog was not changed")
        if item["id"] in candidates and candidates[item["id"]]["channelId"] != item["channelId"]:
            raise ValueError("Conflicting channel ownership")
        candidates[item["id"]] = item
    videos = {video["id"]: video for video in old["videos"]}
    count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for video in pool.map(video_metadata, candidates.values()):
            count += 1
            if video:
                videos[video["id"]] = video
            if count % 50 == 0:
                print("Metadata checked:", count, "/", len(candidates), flush=True)
    ordered = sorted(videos.values(), key=lambda video: (video["publishedAt"], video["id"]), reverse=True)
    # Validate all metadata before creating any new published catalog.
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        list(pool.map(thumbnail, ordered))
    changed = old.get("channels") != CHANNELS or ordered != old["videos"]
    if changed:
        new = {"schemaVersion": 1, "updatedAt": dt.datetime.now(dt.timezone.utc).isoformat(), "channels": CHANNELS, "videos": ordered}
        temporary = CATALOG.with_suffix(".tmp")
        temporary.write_text(PREFIX + json.dumps(new, ensure_ascii=False, indent=2) + ";\n")
        temporary.replace(CATALOG)
    report = {"changed": changed, "catalogTotal": len(ordered), "added": len(set(videos) - {v["id"] for v in old["videos"]}),
              "checked": len(candidates), "channels": {c["name"]: sum(v["channelId"] == c["id"] for v in ordered) for c in CHANNELS}}
    (CACHE / "last-run.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print("YouTube synchronization failed; do not publish:", str(error), file=sys.stderr)
        raise SystemExit(1)
