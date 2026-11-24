# LAFMAT — perfil de segurança

Atualizado em 24/11/2026 para candidato SEO 003+004. Classe S0_STATIC: HTML/CSS/JS públicos, sem servidor de aplicação, autenticação própria, persistência, upload ou Analytics. Formulário de contato abre mailto local; nada é enviado pelo site. Vercel/GitHub/Namecheap são controles administrativos externos.

Fonte e destino: repositório MSR-BR/lafmat-revisao, projeto Vercel lafmat-revisao do time msr-brs-projects, produção https://lafmat.com/, raiz pública dist. Fontes WXR e backups em .private-backups são privados e ignorados. output/ não faz parte deste release. Nenhum env, .vercel ou backup deve ser incluído em staging/deploy. O CLI de link criou credencial efêmera .env.local; arquivo removido sem ler seus valores; .env* ignorado.

Controles verificados localmente: fontes e HTML com hashes; escape de dados nos cartões; scripts sem dependências de produção; redirects limitados a destinos locais constantes, sem proxy/catch-all; 404 dedicado; noindex condicional em hosts não canônicos; JSON-LD somente Organization factual; manifesto de publicação. Security fast check worktree: PASS, sem achados. Configuração dist/vercel.json revisada como superfície sensível.

Baseline de produção anterior: commit cd4d110, implantação lafmat-revisao-m3cqnmy2r-msr-brs-projects.vercel.app, manifesto LAFMAT-20261123-BCB04519421A. Proteção de previews e domínios individuais mantida conforme configuração anterior; revalidar no release. Não baixar variáveis de produção para teste estático. Build --prod --yes foi recusado por auto-review; validação alternativa lê somente schema público, arquivos locais e padrões de rotas, sem contornar a recusa.

Limites: não audita permissões administrativas completas das contas nem configura GA4. Não garante disponibilidade do YouTube ou indexação Google. Revisão externa de invasão não executada; testes restritos aos endereços conhecidos do próprio projeto. Resultado de publicação e identidade exata devem ficar em docs/seo/release-validation.md; este perfil não declara deploy concluído.
