"""Focused regression checks for source identity and unavailable/upcoming data."""
import json
import tempfile
import unittest
import urllib.error
from pathlib import Path
from unittest.mock import patch
import sync_youtube as sync


class YouTubeSyncTests(unittest.TestCase):
    def feed(self, root_id=None, author=None, entries=True):
        channel = sync.CHANNELS[0]["id"]
        entry = f'<entry><yt:channelId>{channel}</yt:channelId><yt:videoId>AAAAAAAAAAA</yt:videoId><title>Scientific seminar</title></entry>' if entries else ''
        return (f'<feed xmlns="http://www.w3.org/2005/Atom" xmlns:yt="http://www.youtube.com/xml/schemas/2015">'
                f'<yt:channelId>{root_id or channel}</yt:channelId><author><uri>{author or "https://www.youtube.com/channel/"+channel}</uri></author>{entry}</feed>').encode()

    def test_feed_accepts_full_and_short_channel_ids(self):
        for identity in [sync.CHANNELS[0]["id"],sync.CHANNELS[0]["id"][2:]]:
            with patch.object(sync,'read_url',return_value=self.feed(root_id=identity)):
                self.assertEqual(sync.feed_inventory(sync.CHANNELS[0])[0]['id'],'AAAAAAAAAAA')

    def test_feed_rejects_wrong_owner(self):
        with patch.object(sync,'read_url',return_value=self.feed(author='https://example.com/channel')):
            with self.assertRaises(ValueError):sync.feed_inventory(sync.CHANNELS[0])

    def test_empty_feed_does_not_replace_existing_catalog(self):
        with patch.object(sync,'read_url',return_value=self.feed(entries=False)):
            with self.assertRaises(ValueError):sync.feed_inventory(sync.CHANNELS[0])

    def test_player_json_handles_nested_strings(self):
        data={'videoDetails':{'title':'A talk with {braces} and "quotes"'}}
        self.assertEqual(sync.player_json('var ytInitialPlayerResponse = '+json.dumps(data)+'; otherScript();'),data)

    def test_missing_player_is_an_error(self):
        with self.assertRaises(ValueError):sync.player_json('<html>temporarily unavailable</html>')

    def test_upcoming_video_is_not_added(self):
        item={'id':'AAAAAAAAAAA','title':'Future seminar','channelId':sync.CHANNELS[0]['id']}
        player={'videoDetails':{'videoId':item['id'],'channelId':item['channelId'],'isUpcoming':True}}
        with tempfile.TemporaryDirectory() as folder,patch.object(sync,'CACHE',Path(folder)),patch.object(sync,'read_url',return_value=('var ytInitialPlayerResponse = '+json.dumps(player)).encode()):
            self.assertIsNone(sync.video_metadata(item))

    def test_existing_metadata_is_not_requested_again(self):
        item={'id':'AAAAAAAAAAA','title':'A revised listing title','channelId':sync.CHANNELS[0]['id']}
        video={'id':item['id'],'channelId':item['channelId'],'title':'Confirmed title'}
        with tempfile.TemporaryDirectory() as folder,patch.object(sync,'CACHE',Path(folder)),patch.object(sync,'read_url') as read:
            (Path(folder)/'watch').mkdir()
            (Path(folder)/'watch/AAAAAAAAAAA.json').write_text(json.dumps({'video':video}))
            self.assertEqual(sync.video_metadata(item),video)
            read.assert_not_called()

    def test_rate_limit_does_not_trigger_immediate_retries(self):
        error=urllib.error.HTTPError('https://www.youtube.com',429,'Too many requests',{},None)
        with patch.object(sync.urllib.request,'urlopen',side_effect=error) as request,patch.object(sync.time,'sleep') as sleep:
            with self.assertRaises(RuntimeError):sync.read_url('https://www.youtube.com')
            self.assertEqual(request.call_count,1)
            sleep.assert_not_called()


if __name__ == '__main__':unittest.main()
