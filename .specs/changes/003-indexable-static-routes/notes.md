# Decisões, riscos e reversão

Decisão: Node.js nativo avalia apenas JS de fontes controladas pelo próprio projeto; renderizador puro serve geração e navegador. Sem framework, pacote ou backend novo. Inglês é padrão; pt/es têm prefixo, slugs estáveis compartilhados. Conteúdo científico/histórico não foi traduzido ou reescrito. Ver contrato em docs/seo/route-contract.md.

Risco de HTML obsoleto mitigado por hashes das fontes e das saídas e bloqueio em update_manifest.py. O fluxo recorrente ainda precisa autorização específica para gerar/publicar novos arquivos e atualizar o HTML diariamente mesmo sem vídeo novo. Ativação antes de resolver isso está fora do aceite de release.

Rollback local: restaurar somente superfícies desta Change e seu manifesto, preservando fontes e documentos de outras tarefas. Produção não foi alterada; não executar reset global. Arquivo 2023 e aliases intactos. Nunca incluir backups privados, output/ ou credenciais em futuro commit.

## Estado de publicação

PUBLICATION_STATE: LOCAL_ONLY
REVIEW_CANDIDATE: LAFMAT-20261124-B80A75C9CAC0
CANDIDATE_SHA256: b80a75c9cac0adcf71039cc52264cbf848e6dda8f25fdf85398231ed775b0c79
APPROVED_REVISION: implementação local deste Change, não release de produção
APPROVED_DESTINATION: workspace atual
APPROVAL_EVIDENCE: usuário “pode seguir com a Change 003”, 24/11/2026
PUBLICATION_EVIDENCE: nenhuma; recibo HTTP confirma manifesto público anterior
NEXT: 004 integrada e autorização da expansão recorrente antes de release
