# Linha de base SEO — 23/11/2026

Change 001 concluída como inventário e diagnóstico local; migração SEO ainda não concluída. Nenhum arquivo de dist, conta, DNS, tag ou configuração Vercel foi alterado. Sem commit/push/deploy neste ciclo. O corpus privado foi consultado somente para URLs e metadados públicos; XML, corpos de páginas, autores e contatos não foram exportados.

## Identidade e fontes

- Revisão do site: `cd4d110ce164457ee5a6e7557afdaa281242d50c`.
- Manifesto: `LAFMAT-20261123-BCB04519421A`, 592 arquivos incluindo metadados de hospedagem.
- Produção: https://lafmat.com/, projeto Vercel lafmat-revisao / msr-brs-projects, main, raiz dist.
- Fontes: árvore dist e links HTML internos; metadados de 29 páginas e 2 posts com status publish no WXR de 19/11; 512 registros de anexos/mídias e recibos de hashes do backup; ledger existente de rotas da conferência 2023. O conteúdo histórico da conferência não foi reavaliado ou editado.
- Inventário normaliza http/www para https://lafmat.com; variantes de host são testadas separadamente. Fragmentos de elementos HTML não são URLs SEO separadas; sete vistas de navegação por hash são registradas como exceção por representar telas atuais. Somente queries p/page_id/attachment_id/year são aceitas; endpoints administrativos e outros domínios ficam fora do escopo.

## Cobertura

| Medida | Quantidade |
|---|---:|
| URLs únicas inventariadas | 1.672 |
| Linhas no mapa de revisão/redirecionamento | 1.125 |
| Manter | 574 |
| Consolidar | 18 |
| Redirecionamento com equivalente identificado | 45 |
| Revisão necessária, com motivo explícito | 1.035 |
| Amostra HTTP consultada | 50 |
| Destinos locais declarados e conferidos existentes | 616 |

As categorias não representam indexação efetiva. Os 45 redirecionamentos são propostas, não regras aplicadas. Há 7 destinos de vistas hash a definir como rotas reais e 14 correspondências que ainda dependem de vistas hash atuais. A quantidade de 616 conta linhas do inventário, não destinos únicos.

Das 1.035 revisões: 512 são páginas de anexos; 494 são referências de mídia sem correspondência binária idêntica no manifesto; 12 são aliases por ID sem equivalente definido; 12 são páginas/posts antigos sem equivalência comprovada; 5 são outras referências ou variantes. Cada linha registra justificativa. Isso não significa 1.035 links quebrados: a maioria não recebeu consulta HTTP e pode incluir caminhos obsoletos, páginas de anexos e duplicações legítimas. Não configurar 410 nem publicar o backup em massa a partir dessa contagem.

## Evidência HTTP

Recibo: `http-baseline-2026-11-23.json`, GET público com validação TLS, até seis saltos e amostra limitada. Resultado final: 27 respostas 200, 18 respostas 404 e 5 respostas 403. Metadados de HTML foram extraídos; corpos não foram salvos.

- HTTP raiz e www passam por 308 e chegam a https://lafmat.com/ com 200.
- As 31 URLs de páginas/posts publicados do WXR foram consultadas: 19 respondem 200 e 12 respondem 404. Onze dos 200 pertencem aos aliases históricos de conferência já preservados; os oito atalhos gerais respondem com noindex e meta refresh, em vez de 301/308 HTTP.
- Cinco galerias anuais antigas (2022–2026) retornam 404. A galeria atual possui 306 vídeos, mas não foi verificada correspondência individual entre cada página anual e os novos cartões neste Change. Destino equivalente e filtro/ano devem ser definidos antes do redirect.
- Também retornam 404: /home/contenido/, /home/nosotros/, /home/events/, /home/gallery/, /home/2825-2/ e os dois posts publicados antigos. Conteúdo/equivalência requer revisão específica; não enviar todos à home.
- Três aliases WordPress por ID da amostra respondem com o mesmo wrapper de /home/, independentemente do registro solicitado. Regras futuras precisam considerar as queries.
- robots.txt, sitemap.xml, wp-sitemap.xml, /home/wp-sitemap.xml e /home/sitemap_index.xml retornam 404. A ausência de robots não bloqueia por si só o Google, mas não há sitemap público identificado.
- Uma URL inventada retorna 404 real, comportamento correto.
- Cinco URLs históricas de mídia consultadas retornam 403. Isso é acesso negado observado, não evidência de inexistência ou indicação para remover; investigar no Change 004 se relevantes.
- O folder atual de Débora e verification.json respondem 200.

## Achados priorizados

| Prioridade | Evidência | Consequência e próxima ação |
|---|---|---|
| P1 | 12 páginas/posts históricos 404, incluindo 5 galerias anuais | Recuperar significado e mapear equivalentes no 003/004; não presumir perda de tráfego quantificada. |
| P1 | Rotas principais com # e HTML inicial dependente de JS | Gerar conteúdo indexável e URLs reais no 003, antes de sitemap e redirects definitivos. |
| P1 | Oito aliases 200/noindex/meta refresh | Preparar 301/308 no servidor Vercel no 004. WordPress não atende mais o domínio público. |
| P1 | Acesso a Search Console/GA4 não comprovado | 002 identifica responsáveis e propriedade, preserva histórico e estabelece baseline de busca real. |
| P2 | Sitemap ausente; entrada sem canonical e metadados específicos por rota | Tratar no release integrado 003+004. |
| P2 | Mídias e páginas de anexos ainda sem correspondência | Priorizar por links reais/tráfego quando disponíveis; hashes fornecem equivalência apenas para 18 binários. |
| P2 | Analytics não identificado no código público | Plano GA4 e privacidade no 005, sem inventar número de visitas. |

P1/P2 são prioridades estruturais e de migração. Não há dados verificados de cliques, backlinks ou visitas para ordenar por impacto quantitativo. Não foi confirmada existência/ausência de propriedades; o conector recusou acesso por assinatura, e as interfaces oficiais gratuitas permanecem alternativa. Não é necessário comprar um plugin para esta migração.

## Decisões e dependências para implementação

1. Definir o contrato de URLs e idiomas em 003; destinos propostos em CSV não são URLs publicadas.
2. Separar páginas antigas realmente equivalentes de placeholders/posts sem valor atual; 404 atual não justifica 410 sem decisão.
3. Tratar antigas galerias anuais com preservação de contexto do ano. Não declarar paridade histórica individual com base no total de 306 vídeos.
4. Para mídia sem hash idêntico, identificar relevância e licença/proveniência antes de recuperar, transformar ou apontar para outro arquivo.
5. Para aliases da conferência 2023, somente registrar o ledger existente: nenhuma alteração será feita sem escopo específico. Pendência impede chamar a consolidação desses aliases de concluída.
6. Ao gerar HTML de vídeos, revisar o contrato da automação, que hoje só pode publicar catálogo/miniaturas/manifesto. Evitar página gerada desatualizada.
7. Manter 003 e 004 como candidato integrado de release, sem publicar links/sitemap que dependam de rotas ausentes.

## Reprodução e limites

Executar na raiz, com Python 3.11+ disponível:

```
.venv-youtube/bin/python scripts/seo_inventory.py
.venv-youtube/bin/python scripts/seo_probe.py
.venv-youtube/bin/python scripts/verify_seo_inventory.py
python3 scripts/verify.py
```

O inventário depende do backup privado local existente, não é parte da produção e não baixa arquivos. Não incluir o backup no Git. seo_probe.py registra a amostra deste ciclo com data de 23/11/2026; para nova baseline, atualizar explicitamente a data/recibo, preservando a anterior. Regerar o inventário limpa seus status HTTP; rodar a amostra em seguida. O recibo de mídia fornece hashes anteriormente verificados: não houve novo download ou recomputação dos 512 originais neste Change.

Não é inventário garantido de todas as URLs que já existiram: faltam exportações Search Console, backlinks externos, logs de acesso e eventuais URLs anteriores ao backup. Não foram coletadas estatísticas GA4, nem confirmado o índice Google. Evidência técnica HTTP e estado do índice são fatos distintos.

Referências metodológicas: [migrações Google](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes), [estrutura de URLs](https://developers.google.com/search/docs/crawling-indexing/url-structure) e [idiomas](https://developers.google.com/search/docs/specialty/international/localized-versions), consultadas na avaliação anterior; rever na implementação.
