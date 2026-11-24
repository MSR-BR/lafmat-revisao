# Validação parcial — 24/11/2026

PASS_LOCAL / PARTIAL_END_TO_END. Não publicada; candidato local habilitado somente no host HTTPS lafmat.com com ID real G-R5KQ774N5V.

- node scripts/test_analytics.cjs: opt-in/recusa/revogação e outra aba, cookies funcionais, uma page_view por rota/idioma, nenhuma PII/URL livre no mock, flags de publicidade negadas e rascunho sem campos. Transporte simulado, zero requests Google nesse teste.
- node scripts/build_site.cjs e verify_static_site.cjs: 45 páginas, 3.570 links/assets; fontes e hashes.
- python3 scripts/verify_seo.py: 57 URLs de sitemap, canonical/idiomas; regras 004 preservadas.
- python3 scripts/verify_conference.py: 22 páginas/aliases e dez assets, fonte textual/tabelas/mídias intactas. Somente HEADs de canônicos instrumentados.
- node scripts/verify_videos.cjs: 306 gravações/273 grupos. Oito testes de sync PASS.
- Browser local: recusa persiste em reload; preferências reabrem por teclado; troca PT/ES; política estática; painel 390 px sem overflow; Google tag ausente antes da escolha/na recusa. Configuração disabled não testa tráfego real do Google.
- Manifesto local e security fast check: ver recibo analytics-local-validation-2026-11-24.json. Produção intacta no release 004.

Serviço GA4 configurado e conferido: conta/propriedade/fluxo reais, retenção 2 meses eventos/usuários, reset off, Signals/user-provided/granular off, personalização 0/307, compartilhamentos off, filtro Testing e três dimensões. Recibo analytics-service-validation-2026-11-24.json.

PENDENTE: revisão/autorização do candidato exato, publicação, DebugView/Realtime e payload/duplicação em tráfego real consentido. Não afirmar eventos recebidos no GA4.
