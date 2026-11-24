# Validação — 24/11/2026

PASS_LOCAL para implementação. Aceite de produção: PENDING; baseline HTTP: PARTIAL_SECURITY_CHALLENGE.

- build_site/verify_static_site: 42 páginas e 3.204 links/assets; paridade, hashes e sem JS preservados.
- verify_seo.py: 42 conjuntos de metadados/idiomas, 54 URLs, 121 regras permanentes, 1.672 decisões.
- Schema público Vercel e todos os 149 padrões (redirects+headers) compilados localmente; ver recibo de versão/limites. Build com --prod --yes foi recusado por auto-review por risco de download de variáveis; não executado nem contornado.
- Testes anteriores de vídeos 306/273, oito testes sync, arquivo 22 páginas/dez assets e inventário 001: PASS.
- Navegador: metadados acompanham rota/idioma; recarga PT seminários correta; sem erro JS capturado. Social PNG 1200×630 inspecionado.
- HEAD de 1.722 URLs (inventário + novas/negativas): 629×200, 519×404, 574×403; após confirmação de x-vercel-mitigated: challenge, 403 foram marcados como NÃO verificados. Consulta pública normal também mostrou Vercel Security Checkpoint. Parar lotes e não contornar challenge ou mudar firewall.
- Security fast check: PASS, com trigger dist/vercel.json; revisão focada sem backend, segredo ou proxy introduzido.
- verify.py: LAFMAT-20261124-20C36699ED23, SHA256 20c36699ed232c98379718c4fa0a9587e11bf08ab3fa34e476dc42affa911aea, 641 arquivos.

Nada foi publicado; callbacks de proteção, equivalência real de URLs com query e precedência no servidor continuam exigindo prova do candidato real. Não alegar indexação, GA4 ou recuperação integral de WordPress. Gate final deve citar commit e destino aprovados.
