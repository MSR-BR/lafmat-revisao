# Decisões e limites

FOLLOW_UP_STATE: ACTIVE
AUTOMATION_ID: acompanhar-sa-de-seo-lafmat
SCHEDULED_FOR:09h30 America/Sao_Paulo; datas em monitoring-plan.json; última 24/12/2026
TARGET_THREAD_OR_PROJECT: este chat / lafmat web
MUTATION_POLICY: consultas read-only e evidência local ignorada; sem mutações de produção/Google ou rotina de vídeos
APPROVAL_EVIDENCE: usuário pediu C07 e confirmou especificamente o acompanhamento automático separado
PUBLICATION_STATE: sem alteração do site; documentação e probe de observação locais

A primeira medição já foi feita. Critério temporal de 30 dias ainda não alcançado; não marcar a Change completa. Relatórios futuros não serão comitados automaticamente, evitando conflitos com a rotina de vídeos. Snapshot de início preservado e dia 24 excluído das comparações por QA/rollbacks. Não há timestamp exato de corte consolidado; primeiro dia completo escolhido 25/11.

O agendador tem gatilho diário finito, com guarda no prompt para consultar apenas nas datas autorizadas da primeira semana/semanas posteriores. Dias intermediários não realizam rede ou consultas; não representam observações. Limite final24/12 às 09h30. Essa implementação e dependência do ambiente local estão explícitas no recibo; nenhuma execução futura foi observada.

Rollback de monitor defeituoso: preservar relatórios e interromper a observação específica, sem desfazer migração por flutuação de posição. Mudanças de tags/DNS/código, novos pedidos de indexação ou mensagens institucionais não estão autorizados pela rotina. WordPress e backups preservados.
