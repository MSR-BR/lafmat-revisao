# Acompanhamento pós-migração — Change 007

Estado em 24/11/2026: primeira medição concluída; janela de observação aberta até 24/12/2026. Não é fechamento antecipado de 30 dias.

## O que já foi observado

O probe público fez 23 requisições pausadas e aprovou 12 rotas canônicas, incluindo idiomas, agenda, galeria, página anual, arquivo, contato, privacidade, membros e notícias. Validou também sitemap/robots/manifesto, dois aliases permanentes, normalização HTTP/www e verdadeiro 404. Sem incidente na amostra. Não equivale a rastrear todo o domínio nem provar ausência de soft404 no índice Google.

O Search Console confirmou indexação efetiva de três das cinco páginas prioritárias consultadas: início, agenda PT e arquivo de 2023. Canonical declarado e escolhido coincidem; Googlebot smartphone, fetch bem-sucedido e HTTPS. A galeria ES continua descoberta sem indexação; a página anual 2026 aparece como desconhecida no snapshot atual, embora a C06 tivesse mostrado descoberta. Registrar a diferença como processamento/discovery ainda instável, sem novo pedido repetido ou conclusão de falha técnica: ambos os testes ao vivo anteriores e as rotas públicas passaram. O total indexado do domínio permanece indisponível no relatório em processamento; não calcular 3/57 como cobertura.

O Analytics Realtime mostra um usuário ativo e eventos first_visit, page_view e session_start. Isso comprova recepção, sem provar visita orgânica: o dia inclui QA e implantação. O cartão consolidado da Home ainda mostra dados não recebidos/zero na janela padrão. Não usar esses zeros como contagem total do site. Comparações por idioma, país e dispositivo ainda não têm duas janelas completas disponíveis.

## Janela e fontes

- Data de implantação/configuração estável: 24/11/2026; implementação 5c69d78 e container Google v2, manifesto 9CB50AF756EB.
- Timestamp exato de corte não foi retido como campo autoritativo durante rollbacks/re-promoções. Excluir todo o dia 24/11 das comparações.
- Primeiro dia completo para comparação: 25/11/2026.
- Observação inicial até 24/12/2026. O fechamento usa somente dias efetivamente disponíveis, respeitando atraso do Google; não promete 30 dias completos de dados consolidados.
- Fontes: HTTP público, Search Console sc-domain:lafmat.com, GA4 565753617 / fluxo 16408359562, recibos005/006 e registros datados007.
- Search Console: comparar sete dias completos, com pelo menos dois dias de defasagem e conforme a última data disponível, contra os sete dias anteriores. Uma primeira comparação útil exige que ambas as semanas tenham dados. Comparar semanas preserva os mesmos dias da semana, mas não elimina diferenças de seminários/feriados/sazonalidade.
- GA4: mesmo intervalo completo quando disponível; diferenciar consentimento, usuários/sessões, cliques SC e eventos. Não esperar igualdade entre denominadores.

## Métricas e alertas

| Controle | Denominador / limite | Ação |
|---|---|---|
| Rotas públicas válidas | 12 URLs fixas da amostra | Falha nova exige confirmação pontual e diagnóstico |
| Cobertura do sitemap | URLs indexadas pertencentes ao sitemap / URLs canônicas atuais, somente se ambos disponíveis | Total não disponível = não verificado |
| Amostra de indexação | Mesmas cinco prioridades; hoje 3/5 | Registrar evolução, sem extrapolar ao domínio |
| Rastreio e canonical | Report Google + metadata/headers públicos | Investigar divergência persistente; não remover URLs |
| Cliques/impressões SC | Semanas completas comparáveis e volume suficiente | Queda >=40%, com >=100 impressões anteriores e repetida em duas observações, é heurística para investigar |
| Recepção GA4 | Eventos previstos; dia de QA separado | Ausência com tráfego conhecido pede diagnóstico; clique não é reprodução/envio |
| País/dispositivo/idioma | Apenas dimensões disponíveis e amostra suficiente | Sem dados não significa zero nem permite tendência |
| Soft404/404 | Relatório Google separado do verdadeiro 404 técnico esperado | 404 esperado não é incidente; perda de URL válida é |

TLS inválido, 5xx persistente, canonical errado, noindex inesperado, bloqueio robots, sitemap inválido ou loop de redirect são incidentes. Confirmar apenas o endereço afetado antes de alertar, sem repetir varredura. Desafio WAF/429 interrompe a consulta e não deve ser rotulado como recurso ausente. Não desativar firewall ou proteções. Nenhuma mudança na migração apenas por flutuação de posições ou primeiros dias de indexação pendente.

Depois de sete dias, revisar páginas críticas ainda sem cobertura; após 14 dias de ausência persistente, registrar plano de investigação. Isso não constitui prazo garantido para o Google. Exceções históricas de mídias sem equivalente continuam no inventário; não declarar todas recuperadas nem publicar backups para melhorar números.

## Rotina autorizada e estado real

Usuário confirmou acompanhamento automático separado às 09h30 de Brasília, avisos somente em falhas/problemas acionáveis. Ferramenta confirmou criação e atualização ACTIVE: acompanhar-sa-de-seo-lafmat, heartbeat neste chat. Recibo monitoring-automation-2026-11-24.json. A rotina de vídeos/SEO das 09h não foi alterada.

Checagens futuras: 25–30/11 e 01/12 (primeira semana diária); 08, 15 e 22/12 (semanais); 24/12 (observação de fechamento). O agendador usa um disparo diário finito com guarda explícita: nos demais dias não há rede ou consulta a contas. O limite final é 24/12/2026 às09h30. Não há ocorrência posterior programada. Depende do ambiente Codex local e de acesso válido aos painéis; nenhuma execução futura foi observada ainda.

Nos dias previstos, executar `python3 scripts/monitor_seo.py --output .cache/seo-monitoring/AAAA-MM-DD-http.json` e consultar os painéis em modo read-only. Evidência futura e síntese de 30 dias ficam em `.cache/seo-monitoring/`, ignorado pelo Git. Não criar modificações rastreadas que interrompam a rotina de vídeos. Registrar dias perdidos e indisponibilidade de acesso; nunca inventar medições retroativas.

Responsável: acompanhamento automatizado neste chat; Mario decide correções externas. O monitor não pode alterar código, consentimento, contas, usuários, filtros, DNS, WordPress, Ads, sitemap submetido, pedidos de indexação, implantação ou a rotina de vídeos. Não enviar mensagens institucionais. Se aparecer um link externo desatualizado, preparar rascunho e aguardar autorização para envio. Sem novo erro comprovado, não criar uma Change corretiva artificial.

## Evidências

- monitoring-baseline-2026-11-24.json: limites, janelas e métricas congeladas.
- monitoring-http-2026-11-24.json: resultado público inicial.
- monitoring-google-2026-11-24.json: estado indexado e recepção GA4.
- monitoring-plan.json e monitoring-automation-2026-11-24.json: calendário e confirmação real.
- migration-closure.md: condições de fechamento ainda pendentes.
