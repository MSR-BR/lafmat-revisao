# Validação Google — Change 006

Execução em 24/11/2026, na conta Google previamente confirmada. Base do site: c3177e1 (somente documentação sobre implementação 5c69d78); manifesto LAFMAT-20261124-9CB50AF756EB, sem alteração de código nesta Change.

## Sitemap

https://lafmat.com/sitemap.xml retorna HTTP 200 e corresponde ao arquivo local. Contém 57 URLs únicas no host HTTPS canônico. robots.txt e manifesto também conferidos. Submetido à propriedade de domínio sc-domain:lafmat.com; Google confirmou processamento bem-sucedido, última leitura em 24/11/2026 e 57 páginas descobertas. O aviso inicial “Couldn't fetch” resolveu durante o processamento, sem repetir o envio. Zero vídeos descobertos nesse sitemap de páginas não significa falha da galeria de links.

## Analytics

Associação confirmada pelo usuário e concluída na interface: domínio lafmat.com (Domain) para a propriedade GA4 LAFMAT — lafmat.com, ID 565753617, fluxo LAFMAT website, ID 16408359562, https://lafmat.com. Confirmação “Link created successfully” e linha da associação observadas. A coleção Search Console já constava “Published to all”, com Queries e Google organic search traffic no menu; não houve publicação duplicada. Queries abriu, mas ainda informa No data available. Não interpretar isso como zero tráfego histórico.

O Google informa que dados de Search Console podem levar cerca de 48 horas após a coleta para aparecer nesses relatórios. A propriedade Search Console ainda processa os relatórios iniciais de desempenho e indexação.

## Inspeções e limites

Resultados individuais e pedidos prioritários estão no recibo google-validation-2026-11-24.json. Distinguir: URL descoberta; teste ao vivo acessível/indexável; pedido aceito na fila; URL efetivamente indexada. O teste ao vivo não escolhe o canonical definitivo do índice, que só é determinado após indexação.

Não foi usado Change of Address: domínio mantido, somente hospedagem/caminhos alterados. Não foi usada Indexing API para páginas comuns, remoção de URLs ou repetição de pedidos. Sitemap processado e solicitação aceita não garantem prazo, indexação ou posição. A cobertura real depende do processamento posterior do Google.

## Referências oficiais

- https://support.google.com/analytics/answer/10737381
- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap

Resultado final: cinco URLs canônicas testadas e cinco pedidos aceitos. A amostra antiga /home/program/ foi carregada pelo Google com canonical https://lafmat.com/conferences/2023/program/, coerente com o redirect permanente. Nenhum pedido de indexação separado para o alias. A tabela final de sitemaps confirma Success / 57 páginas.
