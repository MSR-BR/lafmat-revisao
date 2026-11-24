# Validação — Change 002

Resultado: PASS para posse, acessos e preservação do DNS; PARTIAL para exportações históricas, ainda indisponíveis.

- 24/11/2026: usuário confirmou a conta Google proprietária. Sessão Namecheap renovada pelo próprio usuário.
- Inserido único TXT @ na UI Namecheap; Google Ownership verified e Settings You are a verified owner observados.
- Users (1): Mario Reis, Owner Verified. Sem convites/remoções adicionais.
- DNS Cloudflare/Google resolveram o TXT; A/CNAME/NS de produção preservados; manifesto HTTPS igual ao local, sem mudança de site.
- Sitemaps: 0 cadastrados. Segurança e ações manuais: sem problemas detectados.
- Desempenho/indexação: processando; não há baseline de tráfego exportável confirmada. HTTPS 14/1 com motivo HTTPS not evaluated e atualização 23/11. Recibo estruturado em docs/seo/search-console-baseline-2026-11-24.json.
- Exportação CSV HTTPS tentada mas arquivo não recebido; registrar limite, não marcar download como sucesso.
- Screenshot de Owner Verified e recibo DNS fornecem prova de posse. Mais detalhes em docs/seo/search-console.md.

Próxima etapa técnica local pode avançar. Retomar métricas/exportações em 006/007 quando disponíveis. Sem commit, push ou deploy; dist inalterado.
