# Change 003 — contrato de rotas e geração estática

Implementado e validado localmente em 24/11/2026. **Não publicado.** A publicação será integrada com a Change 004 (canonical, hreflang, metadados, sitemap e redirects). O site público continua no manifesto `LAFMAT-20261123-BCB04519421A`.

## Endereços

Inglês é o idioma padrão, sem prefixo. Português usa `/pt/`; espanhol, `/es/`. O endereço explícito prevalece sobre a preferência salva; não há redirecionamento automático por idioma do navegador. Os slugs são estáveis e iguais entre idiomas.

| Seção | Inglês | Português | Espanhol |
|---|---|---|---|
| Início | `/` | `/pt/` | `/es/` |
| Membros | `/members/` | `/pt/members/` | `/es/members/` |
| Vídeos | `/videos/` | `/pt/videos/` | `/es/videos/` |
| Notícias | `/news/` | `/pt/news/` | `/es/news/` |
| Seminários | `/seminars/` | `/pt/seminars/` | `/es/seminars/` |
| Conferências | `/conferences/` | `/pt/conferences/` | `/es/conferences/` |
| Contato | `/contact/` | `/pt/contact/` | `/es/contact/` |

Vídeos por ano: `/videos/2020/` até `/videos/2026/`, com as duas outras versões de idioma. São 21 páginas de seções e 21 páginas anuais: **42 páginas**, sem contar o arquivo de conferência já existente. Novos anos surgem a partir das datas do catálogo, sem lista anual editorial duplicada.

Links divulgados como `/#seminars`, `/#gallery/2023`, `/#news/item-0` e `/#home/institutional-video` são interpretados pelo navegador e normalizados para endereço real e âncora. Fragmentos não são enviados ao servidor: sem JavaScript um link hash antigo ainda entrega a home, cujos links permitem chegar à seção; não é possível redirecionar seu fragmento via HTTP. Links novos usam `href` reais. Não há fallback de todas as rotas para a home: destinos inexistentes devem continuar 404.

O arquivo `/conferences/2023/`, suas 11 páginas e seus aliases `/home/...` permanecem intactos. A página nova de conferências mantém o submenu e os links em outra aba para esse arquivo. Nenhuma consolidação de aliases históricos foi executada.

## Fonte única e geração

`content.js`, `archive.js`, `i18n.js` e `videos.js` continuam como fontes. `video-gallery.js` mantém a regra de agrupamento. `routes.js` define rotas; `site-render.js` contém o renderizador puro compartilhado pelo build e pelo navegador. `site.js` acrescenta navegação, filtros, submenu e formulário. `templates/site.html` define a estrutura da página. Não foi adicionado framework, pacote ou backend.

```bash
node scripts/build_site.cjs
node scripts/verify_static_site.cjs
python3 scripts/update_manifest.py
python3 scripts/verify.py
```

Requer Node.js 20+ e Python 3; usa somente bibliotecas nativas. `--date AAAA-MM-DD` permite reconstrução determinística para testes. O padrão é a data de São Paulo. `docs/seo/static-build.json` registra os hashes das entradas e saídas, data, contagens e lista de páginas. Não editar os HTML gerados diretamente. O build remove somente saídas anuais obsoletas explicitamente registradas e não modifica arquivos de conferências/WordPress.

O HTML inicial contém todos os membros, agenda e links das gravações; não é uma casca vazia nem conteúdo dentro de `noscript`. Com JavaScript, a galeria mantém carregamento de 24 cartões por vez, busca, filtro por canal e ano. Sem JavaScript, todos os cartões daquela página ficam disponíveis; controles dependentes de JavaScript são ocultados, o menu móvel continua acessível e contato fornece link direto de e-mail. O formulário interativo continua abrindo rascunho no aplicativo, sem envio pelo servidor. A troca de idioma mantém o rascunho enquanto não houver recarga.

As biografias, notícias históricas e títulos científicos mantêm o idioma da fonte, conforme comportamento anterior. Não se afirma tradução integral desses registros. As variantes de idioma traduzem a apresentação, introduções e controles existentes; a política de indexação/hreflang e conteúdo histórico será revisada na Change 004.

## Atualização dos vídeos e da data

Uma alteração de catálogo, agenda ou tradução exige executar o build antes de atualizar o manifesto. `update_manifest.py` agora recusa HTML derivado desatualizado e não reconstrói nem publica silenciosamente. O build é offline; não baixa vídeos ou consulta YouTube.

**Contrato preparado, ativação pendente:** a automação `atualizar-v-deos-lafmat` não foi alterada. Sua autorização atual cobre apenas catálogo, miniaturas e manifesto. Antes da publicação integrada 003+004, obter autorização específica para acrescentar geração/validação e as saídas HTML registradas em `static-build.json` ao escopo recorrente. Atualizar então o prompt/contrato da automação por ferramenta própria; não autorizar commit de outros arquivos, backups ou conteúdo privado. Uma rotina que alterou o catálogo e não executou o build deve parar no guard de manifesto, nunca publicar HTML obsoleto.

O destaque e a agenda usam a data corrente no navegador; para JavaScript desligado, representam a data do último build registrada no recibo. Definir em 004 a atualização diária do HTML mesmo quando nenhum vídeo novo existir. Não há agendamento novo ativo nesta Change. Durante o trabalho local, qualquer publicação automática deve respeitar o guard existente de alterações fora do escopo e não incluir este candidato parcial.

## Validação e publicação

Recibo HTTP: `static-http-validation-2026-11-24.json`. As 42 páginas responderam 200 com bytes iguais ao HTML local; uma URL inexistente respondeu 404. Conteúdo sem JavaScript foi testado com CSP `script-src 'none'` na prévia de QA. Navegador: busca de membros, país, vídeos/canal/ano, carregar mais, idiomas, histórico, recarga, notícias com âncora, submenu/teclado, rascunho e larguras 390, 820 e 1280 px; sem overflow nas amostras.

Não foram enviados sitemap, pedidos de indexação ou eventos GA4. Nenhum DNS, serviço Google ou WordPress foi alterado. O servidor Python local não comprova normalização de barras, index.html, redirects, cache ou TLS da Vercel: conferir esses pontos no candidato integrado de 004 antes de publicar.

Rollback: preservar as fontes editoriais atuais; restaurar renderizador/navegação/template/saídas e manifesto anteriores usando a lista deste Change. Não usar `git reset --hard`, pois há documentos e artefatos de outras tarefas. Nenhum rollback de produção é necessário enquanto esta entrega permanecer local.

Referências primárias consultadas em 24/11/2026: [JavaScript SEO](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics) e [sites multilíngues](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites). Servir conteúdo no HTML e usar URLs distintas por idioma segue essas orientações; indexação efetiva ainda depende da publicação e do Google.

## Estado após release 24/11/2026

PUBLICADO e validado com 004: d45f880, manifesto 20C36699ED23, Vercel READY. A expansão recorrente foi autorizada e ativada na rotina substituta atualizar-v-deos-e-seo-lafmat, 09h/failed_runs_only; não há pendência de ativação. Os parágrafos de preparação acima documentam o estado anterior, não o estado atual. Provas e limites em release-validation.md.
