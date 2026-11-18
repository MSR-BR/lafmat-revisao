# LAFMAT Web

Abra `dist/index.html` no navegador. A versão local funciona sem dependências ou compilação. O vídeo institucional e as imagens migradas são arquivos locais. YouTube, Google Scholar e os links para o site anterior precisam de internet.

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
O GitHub Pages publica a branch gh-pages, contendo somente os arquivos de dist/.
Leia HANDOFF.md para retomar em outro computador e execute python3 scripts/verify.py.
O arquivo público verification.json permite comparar o conteúdo local com a publicação.
A prévia da Vercel está pausada desde a migração para o GitHub Pages.

## Arquivo da conferência de 2023

A seção Conferências abre `dist/conferences/2023/event-home/index.html`, com as 11 páginas públicas da conferência. As rotas antigas `/home/event-home/`, `/home/program/` e os outros nove caminhos também foram preservados em HTML estático. Imagens, PDF de resumo e ZIP LaTeX estão locais; os dois vídeos continuam no YouTube.

As fontes públicas imutáveis estão em `sources/conference-2023/`. Para reconstruir após instalar `beautifulsoup4==4.15.0`, execute `python3 scripts/archive_conference.py` (sem rede). `--download` recupera os arquivos locais da origem e exige rede. Execute `python3 scripts/verify_conference.py` para conferir paridade e links. Leia `docs/conference-2023-validation.md` para as exceções da origem e `docs/domain-migration-plan.md` para preparar o domínio sem afetar e-mails.

O menu **Conferências** abre uma lista de anos. Para acrescentar uma edição, inclua `{year: AAAA, url: 'caminho/da/edicao/index.html'}` em `conferences` no arquivo `dist/assets/content.js`. A lista alimenta o submenu e a página de conferências; as edições abrem em outra aba. Após alterações intencionais, execute `python3 scripts/update_manifest.py` e `python3 scripts/verify.py`.

## Domínio lafmat.com

O domínio personalizado é declarado em `dist/CNAME`. O DNS passou para Namecheap BasicDNS em 18/11/2026, após confirmação de que não há contas de e-mail ou encaminhamentos em uso. Consulte `docs/domain-cutover-2026-11-18.md` para a configuração, o rollback e o estado do certificado HTTPS. Preserve `dist/CNAME` e `dist/.nojekyll` em toda publicação. O segundo arquivo impede o processamento Jekyll e mantém rotas históricas com sublinhado, como `/home/__trashed/`. A hospedagem antiga não foi cancelada.

`python3 scripts/build_legacy_routes.py` reconstrói os atalhos das antigas páginas WordPress, incluindo `/home/`, sem depender do backend antigo.
