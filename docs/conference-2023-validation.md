# Conferência 2023 — cópia e conferência

Data: 18/11/2026. Escopo: as 11 páginas públicas do menu da conferência de 2023 e os arquivos referenciados nesse conteúdo. Fontes HTML anônimas preservadas em `sources/conference-2023/`; inventário com hashes em `conference-2023-inventory.json`.

## Resultado local

- 11 páginas copiadas, com os 11 destinos do menu na ordem original.
- 11 caminhos antigos `/home/<slug>/` também atendidos por HTML estático, sem depender de redirecionamentos de servidor ou do WordPress. São 22 páginas completas mais o índice do arquivo.
- Igualdade integral do texto normalizado de cada página, incluindo tabelas, datas, nomes, fórmulas com sub/sobrescritos e informações públicas históricas.
- 10 arquivos locais: 8 imagens (incluindo o cabeçalho original e sua prévia menor), um PDF de modelo de resumo e um ZIP LaTeX. Binários verificados por assinatura e SHA-256; ZIP testado internamente.
- Dois vídeos YouTube preservados como incorporações externas. Não foram baixados.
- Nenhuma referência de mídia ou navegação depende do servidor WordPress. Cabeçalho, cartaz, patrocinadores, programa e imagens estão locais.
- Rota Conferências do site aponta para o arquivo local; textos de entrada atualizados em português, inglês e espanhol. O conteúdo histórico conserva o idioma da fonte.
- Arquivo funciona sem JavaScript, PHP, Divi ou serviços de envio. Aviso explicita que as inscrições estão encerradas e que taxas/instruções são históricas.

## Exceções da origem

1. A imagem `logoevent-e1677099273566.jpeg` da página de contato retorna HTTP 404. Foi substituída pelo logotipo do mesmo evento disponível na biblioteca pública do WordPress (anexo 1603, `logoevent-removebg-preview.png`). O original ausente não foi recuperado. A substituição foi inspecionada visualmente e registrada no inventário; não se afirma identidade binária com o arquivo perdido.
2. O link consular para requisitos de visto não respondeu à consulta. O link da Wikipédia retornou HTTP 403 ao cliente de conferência. Ambos foram preservados; isso não significa que seu conteúdo externo tenha sido validado. Mapa, universidade e duas referências Springer responderam com sucesso. Evidências em `conference-2023-external-links.json`.
3. A fonte tem divergência de datas (23–28 na apresentação, 23–27 em outras páginas) e um rótulo de link consular malformado. Conservados literalmente, sem correção editorial não autorizada.
4. O XML administrativo, banco WordPress, anexos não referenciados pelo conteúdo e demais páginas do site não fazem parte desta cópia pública da conferência. Não foram copiados registros privados ou credenciais.

## Validação executada

- `python3 scripts/verify_conference.py`: PASS — texto fonte/destino nas 22 páginas, contagem de imagens/tabelas, identidade dos endereços dos vídeos, menu, existência de links/arquivos locais, hashes e assinaturas binárias.
- `node --check` nos três arquivos JavaScript alterados: PASS.
- Navegador: página inicial do arquivo e navegação do site conferidas em desktop; todas as 11 páginas abertas a 390 px, sem transbordamento horizontal da página. Tabela histórica usa rolagem própria (650 px em região de 332 px), preservando todas as colunas.
- Conferência visual do cabeçalho e logotipo recuperado. A resolução original do cabeçalho permanece acessível ao clicar na imagem.
- `security_fast_check.py --root . --mode worktree`: PASS, 52 arquivos inspecionados antes dos registros finais, nenhum gatilho sensível. Escopo S0_STATIC; nenhuma nova autenticação, API, dependência de produção, workflow, DNS ou configuração de hospedagem.

## Publicação

Destino proposto: GitHub Pages existente, `MSR-BR/lafmat-revisao`, branch `gh-pages`, raiz de `dist/`.
A versão pública anterior é `4d811bbae0b13bc00e5beabb7d4172f4384030fd`; conteúdo anterior identificado por `LAFMAT-20261117-2B1B0764BEA2`. Rollback: publicar novamente a árvore dessa revisão por um novo commit na branch de publicação. Não fazer force-push nem apagar a história.

Decisão técnica: PASS para a cópia estática, com as limitações documentadas acima. A identidade da produção nova só poderá ser conferida depois de publicada. A mudança do domínio não integra esta publicação.
