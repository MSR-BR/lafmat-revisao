# LAFMAT Web

O site está publicado em https://lafmat.com/. Para conferir uma prévia local, execute `python3 scripts/preview_site.py` e abra `http://127.0.0.1:8765/`. A navegação agora usa endereços reais, portanto abrir via `file://` não é mais o modo de prévia suportado. O vídeo institucional e as imagens migradas são arquivos locais. YouTube e Google Scholar precisam de internet. O release integrado 003+004 foi publicado e validado em 24/11/2026; veja docs/seo/release-validation.md.

## HTML estático e URLs

As fontes continuam em `dist/assets/content.js`, `archive.js`, `i18n.js` e `videos.js`. Após alterá-las, execute `node scripts/build_site.cjs`, `node scripts/verify_static_site.cjs`, `python3 scripts/update_manifest.py` e `python3 scripts/verify.py`. Node.js 20+ é usado somente na manutenção, sem dependências novas; o resultado permanece HTML/CSS/JS estático, sem build na hospedagem. Não editar os HTML gerados manualmente.

São 42 páginas com conteúdo inicial, inclusive sem JavaScript: sete seções em três idiomas e sete anos de vídeos em três idiomas. Inglês usa `/members/`, `/videos/`, `/seminars/` etc.; português e espanhol usam `/pt/` e `/es/`. O menu conserva o arquivo de 2023 em outra aba. Links hash antigos continuam compatíveis no navegador. Veja [o contrato de rotas](docs/seo/route-contract.md) para fontes, limitações, QA e preparação da automação.

O comando `python3 scripts/preview_site.py --port 8766 --no-js` serve a mesma saída com scripts bloqueados via CSP para conferir conteúdo e navegação sem JavaScript. A data do HTML é a do build; o navegador com JavaScript atualiza o destaque/agenda pela data corrente. SEO técnico e atualização diária do HTML estão integrados ao release 003+004.

## SEO técnico e migração — Change 004

`dist/assets/seo.js` gera canonical, metadados específicos, idiomas recíprocos/x-default e Organization JSON-LD, mantendo os mesmos valores na navegação do navegador. A imagem de compartilhamento é `dist/assets/lafmat-social.png` (1200×630, original; ver provenance em docs/seo). O sitemap tem 54 URLs canônicas: 42 páginas e 12 entradas existentes do arquivo; não contém hashes, aliases ou recursos. Datas lastmod seguem mudança real de conteúdo; o arquivo histórico não recebe data inventada.

`dist/vercel.json` é a configuração da raiz efetiva de hospedagem. Contém redirects permanentes, normalização de index.html/barra final, cabeçalhos canonical do arquivo e noindex condicional em hosts de preview. Não alterar DNS para esse release. Oito HTML de atalhos permanecem como fallback para hospedagem estática sem suporte às regras Vercel. A proteção dos previews deve continuar ativa.

Para reconstruir regras a partir do inventário congelado e do mapa da conferência, execute `python3 scripts/build_seo_routes.py`, depois `node scripts/build_site.cjs` e `python3 scripts/verify_seo.py`. Não execute `seo_inventory.py` para sobrescrever a linha de base histórica ao reconstruir o site. O comando de build comum reaproveita a lista fixa de rotas canônicas do arquivo; a rotina de vídeos não pode alterar regras/aliases.

O mapa de decisões cobre as 1.672 URLs inventariadas. Mídias/páginas antigas sem equivalente público comprovado continuam como exceções, sem recuperação em massa do backup nem redirect genérico à home. HTTP 403 de Vercel Security Checkpoint não é prova de conteúdo ausente. Faça verificações públicas pontuais; evite varredura concorrente e pare ao receber desafio de segurança. Ver `docs/seo/release-validation.md` para estado real de release, limites e rollback.

- **Agenda e banner.** Em `dist/assets/content.js`, acrescente seminários com data `AAAA-MM-DD`. O destaque na home acompanha a data do próximo seminário identificado. Para atualizar o cartaz semanal, copie a imagem para `dist/assets/` e preencha `weeklyBanner`, por exemplo:
  ```js
  weeklyBanner: {
    date: '2026-11-21',
    image: 'assets/seminario-2026-11-21.webp',
    alt: {pt: 'Cartaz do seminário de Johan Triana', en: 'Johan Triana seminar flyer', es: 'Cartel del seminario de Johan Triana'}
  },
  ```
  A agenda pública mostra apenas datas a partir de hoje. O próximo seminário aparece em destaque no topo da página, junto com o cartaz quando a imagem da semana estiver configurada.
- **Membros, notícias e artigos.** Atualize `members` e `news` no mesmo arquivo. As notícias novas aparecem antes das notícias migradas e a primeira alimenta o destaque na home. Cada uma contém `date`, `title`, `lines` e, se houver, `links` no formato `[[rótulo, URL]]`. A busca atual abre o Google Scholar com uma consulta por membro e afiliação. Para inserir artigos conferidos, acrescente objetos com `title` e `url` em `publications`. Um futuro feed automático pode usar identificadores ORCID confirmados e revisão editorial.
- **Conteúdo migrado.** `dist/assets/archive.js` reúne os cinco anos da galeria, as biografias existentes, as notícias e os textos de referência do WordPress. A navegação, os controles e a apresentação da rede estão em português, inglês e espanhol. Biografias, títulos científicos e notícias históricas mantêm o idioma da fonte.
- **Contato.** A caixa de mensagem abre um rascunho no aplicativo de e-mail para revisão e envio. Para receber mensagens diretamente pelo site depois de publicado, será necessário configurar um serviço de envio e o endereço de destino.

Fontes: [LAFMAT](https://www.lafmat.com/home/), Agreement de outubro de 2026 para a composição do grupo e a agenda fornecida para novembro de 2026 a julho de 2027. O Agreement serviu como fonte de nomes e afiliações. A página de membros lista Luis De Los Santos Valladares como presidente, conforme o Agreement. A página de contato conserva o cargo publicado no WordPress. Os e-mails dos palestrantes e os dados de contato internos do acordo ficaram fora dos arquivos do site.

## Sincronização e publicação

O repositório completo está em https://github.com/MSR-BR/lafmat-revisao.
A produção é https://lafmat.com/, hospedada na Vercel no projeto `lafmat-revisao` do time `msr-brs-projects`. A integração Git publica a branch `main`, com **Root Directory `dist`**, framework Other, sem build ou dependências de produção. A branch `gh-pages` conserva a versão estática anterior para contingência.
Leia HANDOFF.md para retomar em outro computador e execute python3 scripts/verify.py.
O arquivo público verification.json permite comparar o conteúdo local com a publicação.
O domínio de produção é público. Previews e URLs individuais de implantação continuam protegidos pela autenticação Vercel.

## Vídeos dos canais da rede

A galeria usa `dist/assets/videos.js`, com metadados conferidos nos canais [Lafmatnetwork](https://www.youtube.com/@Lafmatnetwork) e [GI MATEFUN](https://www.youtube.com/@gimatefun5035). As miniaturas ficam em `dist/assets/video-thumbnails/`; as gravações continuam no YouTube. A lista é organizada pelo **ano de publicação**, com filtros por canal, busca e carregamento gradual. Cópias de mesmo título e data em canais diferentes podem compartilhar um cartão, preservando os dois links. O conteúdo original importado do WordPress permanece intacto em `archive.js`; a nova galeria usa a identidade/título efetivos dos vídeos, evitando os links repetidos ou incompletos da fonte antiga.

Para sincronizar o catálogo público completo (vídeos e gravações de transmissões), use Python 3.11+:

```bash
python3 -m venv .venv-youtube
.venv-youtube/bin/python -m pip install -r requirements-youtube.txt
.venv-youtube/bin/python scripts/sync_youtube.py --full
node scripts/verify_videos.cjs
python3 scripts/test_youtube_sync.py
node scripts/build_site.cjs
node scripts/verify_static_site.cjs
python3 scripts/update_manifest.py
python3 scripts/verify.py
```

Sem `--full`, o coletor consulta os feeds recentes. O modo completo evita depender do limite de 15 itens dos feeds. Não baixa os vídeos, não precisa de chave de API e não altera os canais. Reutiliza o catálogo e o cache para não consultar novamente todas as páginas antigas; em falha ou limite do YouTube, interrompa a publicação e preserve a versão vigente. Não remove gravações antigas automaticamente. O site continua estático; o coletor e sua dependência são ferramentas de manutenção, fora de dist.

A automação Codex **Atualizar vídeos e SEO LAFMAT** (`atualizar-v-deos-e-seo-lafmat`) está ativa neste chat, diariamente às 09h de Brasília, autorizada a publicar catálogo, miniaturas, HTML derivados, sitemap, recibo de build e manifesto após os testes. A execução é local e depende da disponibilidade do Codex/computador; não é um serviço de agendamento da Vercel. A política de notificações informa falhas. Alterações em WordPress, conferências, DNS ou outras seções não fazem parte dessa autorização.

A ampliação e a substituição da rotina foram expressamente autorizadas em 24/11/2026. A rotina anterior não existia no cadastro; a substituta está ACTIVE, com avisos apenas em falhas. Ela também recompila a agenda/destaque por data mesmo sem vídeo novo, mas não cadastra novos seminários automaticamente. O guard de `update_manifest.py` interrompe o processo quando fontes e HTML divergem. Artefatos locais output/ e backups permanecem fora do escopo e do Git.

## Arquivo da conferência de 2023

A seção Conferências abre `dist/conferences/2023/event-home/index.html`, com as 11 páginas públicas da conferência. As rotas antigas `/home/event-home/`, `/home/program/` e os outros nove caminhos também foram preservados em HTML estático. Imagens, PDF de resumo e ZIP LaTeX estão locais; os dois vídeos continuam no YouTube.

As fontes públicas imutáveis estão em `sources/conference-2023/`. Para reconstruir após instalar `beautifulsoup4==4.15.0`, execute `python3 scripts/archive_conference.py` (sem rede). `--download` recupera os arquivos locais da origem e exige rede. Execute `python3 scripts/verify_conference.py` para conferir paridade e links. Leia `docs/conference-2023-validation.md` para as exceções da origem e `docs/domain-migration-plan.md` para preparar o domínio sem afetar e-mails.

O menu **Conferências** abre uma lista de anos. Para acrescentar uma edição, inclua `{year: AAAA, url: 'caminho/da/edicao/index.html'}` em `conferences` no arquivo `dist/assets/content.js`. A lista alimenta o submenu e a página de conferências; as edições abrem em outra aba. Após alterações intencionais, execute `python3 scripts/update_manifest.py` e `python3 scripts/verify.py`.

## Domínio lafmat.com

O registro e o DNS permanecem na Namecheap BasicDNS. Em 19/11/2026, a hospedagem mudou para Vercel: A `@` → `216.198.79.1` e `64.29.17.1`; CNAME `www` → `0986d6ca91bddc7d.vercel-dns-017.com.`; TTL 300. São os valores fornecidos para este projeto; consulte a Vercel antes de reaproveitá-los em outro projeto. O certificado cobre os dois nomes, e `www` redireciona permanentemente para `https://lafmat.com`. Não há contas de e-mail ou encaminhamentos em uso, conforme confirmação do usuário. A hospedagem antiga não foi cancelada. Veja `docs/vercel-migration-2026-11-19.md`.

`dist/CNAME` e `dist/.nojekyll` são metadados da publicação histórica GitHub Pages; não configuram o domínio na Vercel. O segundo preserva rotas com sublinhado, como `/home/__trashed/`, se o site voltar a ser publicado pelo Pages.

`python3 scripts/build_legacy_routes.py` reconstrói os atalhos das antigas páginas WordPress, incluindo `/home/`, sem depender do backend antigo.
