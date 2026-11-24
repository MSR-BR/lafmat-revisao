# Release integrado SEO 003+004 — preparação 24/11/2026

Estado: CANDIDATO LOCAL VALIDADO; publicação ainda não executada. Nenhum claim de indexação Google.

Destino previsto: https://lafmat.com/, Vercel lafmat-revisao, time msr-brs-projects, Git main, Root Directory dist. Projeto confirmado por CLI (conector com 404 na conta desta sessão). Revisão exata e manifesto serão registrados no gate antes do push/deploy.

## Entrega concreta

- 42 páginas estáticas/idiomas e vídeos por ano, extraídas das fontes atuais; 306 gravações em 273 grupos.
- Metadados específicos, canonical HTTPS, hreflang recíproco/x-default, Open Graph/Twitter e imagem PNG original.
- JSON-LD Organization factual; sem Event por falta de página própria e dados completos do evento. Sem afirmação de elegibilidade a rich results.
- 54 URLs no sitemap: 42 páginas novas + 12 entradas canônicas do arquivo existente. Lastmod significativo nas páginas geradas; omitido para arquivo histórico cuja data original é desconhecida.
- 121 regras permanentes, com IDs WordPress antes da regra geral /home/. Conferência consolidada conforme autorização explícita, sem alterar seus arquivos/editorial. Canonical de arquivo via cabeçalho HTTP Link.
- trailingSlash, index.html e 404 explícitos; noindex de previews por host, sem enfraquecer a proteção da Vercel.

## Cobertura e exceções

As 1.672 URLs têm decisão registrada em migration-decisions.csv. Há 512 páginas de anexos ausentes, 497 mídias sem binário público comprovado, sete páginas/posts sem equivalente (incluindo templates/formulários antigos), uma referência órfã e sete aliases de ID desses caminhos ausentes. Esses são estados preexistentes mantidos; não se afirma recuperação de todo o WordPress nem se publica o backup. A decisão conservadora é preservar o 403/404 existente sem redirecionar a home ou declarar remoção 410. Resultados HTTP antes/depois distinguirão regressões. Qualquer regressão nova deve impedir conclusão e ser corrigida ou sofrer rollback.

## Evidências locais

- verify_static_site: PASS 42 páginas, paridade, 3.204 links/assets locais.
- verify_seo: PASS 42 conjuntos de metadados/idiomas recíprocos, 54 URLs de sitemap, 121 regras, 1.672 decisões.
- Schema público da Vercel validado localmente (declaração de meta-schema draft-04 omitida apenas para compatibilidade do AJV instalado); SHA do schema e limite no recibo vercel-config-validation-2026-11-24.json. Padrões compilados com path-to-regexp 6.1.0 já no cache da ferramenta, sem dependência nova do projeto. Isso não substitui o teste real do host.
- Vídeos: 306/273 PASS. Sync: oito testes PASS. Conferência: 22 arquivos/aliases, paridade e dez assets PASS. Inventário 001 preservado PASS.
- Navegador local: canonical/og/descrição/alternates acompanham navegação e idioma; recarga PT/seminars preserva metadados e conteúdo; console sem erros da aplicação. Candidato visual salvo fora do repositório.
- Security fast check: PASS; revisão focada em dist/vercel.json, sem proxy, APIs, segredos ou dependências de produção novas.

## Publicação e rollback

Somente dist será entregue à Vercel; backups, output, .env e .vercel não pertencem ao deploy. Push main dispara Git integration e só pode ocorrer após aprovação do candidato exato conforme gate. Verificar READY, manifesto/hash/TLS e status/redirects/canonical/sitemap nos domínios reais; manter a proteção dos endereços individuais. Submissão ao Search Console e GA4 permanecem nas Changes 006/005.

Rollback conhecido: implantação lafmat-revisao-m3cqnmy2r-msr-brs-projects.vercel.app, commit cd4d110, manifesto LAFMAT-20261123-BCB04519421A. Restaurar domínio para essa implantação sem mudar DNS/certificado; não apagar fontes atuais nem novos dados posteriores. Rollback pode exigir promoção explícita para retomar atribuição automática da Vercel.

Rotina: usuário autorizou ampliar e preservar horário/notificações em 24/11/2026. Configuração antiga não disponível no arquivo local; tentativa de atualização por ferramenta exige parâmetros completos. Prompt ampliado preparado; pergunta de substituição por rotina de chat pendente. Não declarar sincronização recorrente ativa antes de confirmação real.

Limite observado em 24/11: o cliente HTTP recebeu Vercel Security Checkpoint (x-vercel-mitigated: challenge) após a checagem em lote. 403 não comprova ausência de recurso. Varredura interrompida; repetir somente verificações pontuais quando o acesso normal estiver disponível, sem bypass de challenge nem alteração de firewall. Recibo de baseline marcado PARTIAL.
