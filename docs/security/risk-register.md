# Riscos do release SEO 003+004

| ID | Nível | Evidência/estado | Controle e ação |
|---|---|---|---|
| SEO-OLD | Médio | Diversos anexos/mídias/páginas antigas já ausentes antes deste release | Preservar resposta atual, registrar decisão/HTTP por URL; não enviar a home nem publicar backup privado. Recuperação editorial fora deste release. |
| SEO-SYNC | Médio | HTML de vídeos/agenda depende de geração | Guard de manifesto e validação de hashes; ampliação recorrente autorizada pelo usuário; ativação depende de configuração operacional confirmada. |
| SEO-ROUTES | Médio | Novas regras sensíveis a precedência/query/trailing slash da Vercel | Schema/padrões e destinos locais verificados; conferir no candidato hospedado e pós-release; rollback para implantação anterior sem mudar DNS. |
| SEO-PREVIEW | Baixo | Candidato tem URLs próprias de implantação | Manter proteção Vercel, mais X-Robots-Tag condicional; não desproteger previews. |
| SEO-DATE | Baixo | Agenda sem JS reflete data do build | Rotina diária deve gerar mesmo sem vídeo novo; lastmod muda apenas se conteúdo relevante mudar. |

Não aceitar risco em nome do usuário. Resultado final de gate será registrado para revisão e destino exatos. Nenhum segredo ou conteúdo privado foi usado na imagem de compartilhamento.

Limite observado em 24/11: o cliente HTTP recebeu Vercel Security Checkpoint (x-vercel-mitigated: challenge) após a checagem em lote. 403 não comprova ausência de recurso. Varredura interrompida; repetir somente verificações pontuais quando o acesso normal estiver disponível, sem bypass de challenge nem alteração de firewall. Recibo de baseline marcado PARTIAL.

## Fechamento verificado — 24/11/2026

SEO-SYNC: rotina substituta ACTIVE e escopo autorizado; execução futura depende do ambiente local. SEO-ROUTES: 305 checks reais PASS, cobrindo 54 páginas e 121 regras. SEO-PREVIEW: 302 para vercel.com/sso-api confirmado, sem modificar proteção. SEO-OLD: exceções conservadoras aceitas pelo usuário, sem recuperação de conteúdo não comprovado. SEO-DATE: build diário configurado; não se afirma disparo futuro já observado. Gate de release final PASS em docs/seo/release-gate-2026-11-24.json.
