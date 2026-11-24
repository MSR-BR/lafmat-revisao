# Validação — 24/11/2026

Resultado: PASS para implementação local. Release integrado com 004: NOT_RUN.

- `node scripts/build_site.cjs`: 42 páginas; 306 gravações, 273 grupos, 25 representantes e 4 colaboradores.
- `node scripts/verify_static_site.cjs`: PASS; 2.952 referências locais verificadas; paridade com fontes, hashes de entradas/saídas, datas, filtros e links legados.
- Reconstrução na mesma data: hashes das 42 páginas idênticos.
- Fixture isolada com catálogo alterado: `update_manifest.py` recusou execução, nenhum manifesto criado. Não houve alteração de fonte real para esse teste.
- HTTP nas 42 URLs: 200 e bytes iguais aos arquivos; destino inexistente 404. Recibo `docs/seo/static-http-validation-2026-11-24.json`.
- Navegador com JS e com scripts bloqueados por CSP: conteúdo, idiomas, filtros, carregar mais, navegação por ano, recarga, histórico, notícias com âncora/query, links hash, menu/teclado e rascunho de contato. Sem envio de mensagem. Layout amostrado em 390/820/1280 px, sem overflow; imagens da home verificadas carregadas.
- `node scripts/verify_videos.cjs`: PASS 306 gravações / 273 grupos.
- `python3 scripts/test_youtube_sync.py`: 8 testes PASS.
- `python3 scripts/verify_conference.py`: PASS 22 páginas de arquivo/aliases e 10 assets.
- `.venv-youtube/bin/python scripts/verify_seo_inventory.py`: PASS, inventário anterior preservado.
- `python3 scripts/update_manifest.py` e `python3 scripts/verify.py`: PASS, LAFMAT-20261124-B80A75C9CAC0, 635 arquivos.
- Security fast check worktree: PASS, sem achados; sem dependência nova ou autenticação.
- `git diff --check`: PASS.

Produção observada intacta: LAFMAT-20261123-BCB04519421A. Não foram validados redirects/canonical/hreflang/robots/sitemap na Vercel (004), Google index (006) ou expansão da automação. A prévia Python não é evidência de TLS/regras da Vercel. Conteúdo sem JS acompanha a data do build; atualização diária será integrada antes do release.

## Validação pública final

PASS: 305 requisições sequenciais, 54 páginas canônicas, 121 regras permanentes, artefatos com bytes exatos, 404 real, HTTPS/www e dez assets. Deployment dpl_CJWnMJJbfTAbgEnw9CUqzstuoyqg READY, proteção de URL individual preservada (302 login). Navegador/rotina ACTIVE comprovados. Estado pendente/local acima descreve preparação histórica; estado atual em release-validation.md.
