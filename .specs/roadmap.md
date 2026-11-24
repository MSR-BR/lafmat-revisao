# LAFMAT — ciclo de SEO, migração e medição

Criado em 23/11/2026 por solicitação de criar as Changes. Change 001 concluída como inventário local em 23/11/2026; Change 002 com posse concluída em 24/11/2026 e exportações pendentes de processamento Google; Changes 003+004 publicadas e validadas em 24/11/2026; Changes 005–007 planejadas. Não há sequência anterior em .specs/changes; numeração deste ciclo começa em 001 e não representa as entregas históricas já concluídas. Memória existente: HANDOFF.md.

| Change | Entrega | Dependências | Estado |
|---|---|---|---|
| 001 | [Inventário de URLs e linha de base SEO](changes/001-inventory-and-seo-baseline/objective.md) | — | Concluída (local) |
| 002 | [Propriedade e acessos do Search Console](changes/002-search-console-ownership/objective.md) | 001 | Posse concluída; histórico processando |
| 003 | [URLs reais e HTML estático indexável](changes/003-indexable-static-routes/objective.md) | 001 | Publicada e validada com 004 |
| 004 | [SEO técnico e redirecionamentos da migração](changes/004-technical-seo-and-migration-redirects/objective.md) | 001, 003 | Publicada e validada; rotina ACTIVE |
| 005 | [GA4, privacidade e medição](changes/005-ga4-privacy-and-measurement/objective.md) | 001 | Publicada e validada com 004 |
| 006 | [Submissão e validação no Google](changes/006-index-submission-and-google-validation/objective.md) | 002, 004, 005 | Planejada |
| 007 | [Acompanhamento e fechamento da migração](changes/007-post-migration-monitoring/objective.md) | 004, 006 | Planejada |

Ordem: 001 primeiro; 002 e preparação de 005 podem ocorrer em paralelo com 003/004. O site com URLs reais e redirects deve sair em uma publicação integrada 003+004. Submissão de sitemap pode seguir 002+004; vínculo com GA4 aguarda 005. 007 acompanha o release, com revisão inicial de 30 dias, sem prazo garantido de indexação.

Próxima Change: 005-ga4-privacy-and-measurement. Não executar sem solicitação. Plano de modelo: tier standard/medium, sujeito à disponibilidade real; sem delegação automática.

Autorização inicial: criar planejamento local; em seguida, "segue" autorizou executar Change 001. Não executar Changes, registrar propriedades, instalar tag, alterar DNS, agendar monitoramento, fazer commit/push ou deploy apenas por este pedido. As autorizações anteriores de outras tarefas não transformam este backlog em execução concluída.

## Evidência de partida

- Produção Vercel https://lafmat.com/, projeto lafmat-revisao, time msr-brs-projects, main, raiz dist.
- Último conteúdo publicado: commit cd4d110, manifesto LAFMAT-20261123-BCB04519421A. Revalidar na execução.
- 306 gravações catalogadas; manutenção recorrente tem escopo restrito e deve ser preservada.
- Auditoria preliminar: hash routing; aliases antigos 200/noindex com meta refresh; robots/sitemap 404; canonical/GA4 ausentes na entrada atual. Não equivale a confirmação do índice Google.
- Contas SC/GA4 não verificadas; conector GSC Wizard indisponível por assinatura. Interfaces oficiais gratuitas são alternativa.
- WordPress antigo suspenso; domínio agora atende pela Vercel. Redirects da migração pertencem ao servidor atual.

## Referências primárias

- https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes
- https://developers.google.com/search/docs/crawling-indexing/site-move-no-url-changes
- https://developers.google.com/search/docs/crawling-indexing/url-structure
- https://developers.google.com/search/docs/specialty/international/localized-versions
- https://developers.google.com/analytics/devguides/collection/ga4/single-page-applications
- https://support.google.com/analytics/answer/10737381

Referências consultadas na avaliação; verificar documentação vigente na execução.

Autorização em 24/11/2026: “pode seguir com a Change 003”. Candidato local LAFMAT-20261124-B80A75C9CAC0; nenhum commit/push/deploy.

24/11/2026: execução de 004 autorizada; metadados e redirects preparados/testados localmente, 11 aliases e expansão recorrente explicitamente autorizados. Rotina precisa resolver cadastro e publicação exige gate do candidato. Baseline HTTP parcial por Vercel Security Checkpoint, sem provar ausência de mídias pelos 403.

Fechamento 24/11: d45f880 publicado no projeto/domínio aprovados, Vercel READY, manifesto 20C36699ED23, 305 checks HTTP PASS, dez assets PASS, rotina substituta ACTIVE 09h/failed_runs_only. Ver release-validation.md.
