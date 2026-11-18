# Continuidade em outro computador

O projeto canônico é este repositório, MSR-BR/lafmat-revisao, branch main.
O conteúdo editável e publicado fica em dist/. A publicação usa a branch gh-pages, com os arquivos de dist/ na raiz.
Não trabalhar na antiga cópia temporária em /tmp.

A versão pública é https://msr-br.github.io/lafmat-revisao/.
A Vercel está pausada. O domínio lafmat.com continua no WordPress.
A migração do domínio depende de acesso autorizado à Namecheap/BanaHosting e da aprovação do grupo.
Antes da migração, preservar a conferência 2023, que ainda aponta ao WordPress, e confirmar uso de e-mail @lafmat.com.

O idioma inicial é inglês, com preferência de idioma salva no navegador.
O cartaz atual é de Johan Triana, 21/11/2026. O destaque depende da data da agenda.
Contato prepara mailto para ld301@cam.ac.uk. A busca de artigos abre Google Scholar.
Não há backend de envio nem busca automática de publicações.

No outro computador, clone o repositório ou use a pasta sincronizada do Dropbox.
Confira a pasta de trabalho e execute:

    git pull --ff-only origin main
    python3 scripts/verify.py
    git status --short

O verificador deve retornar PASS e o código registrado em dist/verification.json.
O status Git deve estar limpo. Compare o mesmo código com
https://msr-br.github.io/lafmat-revisao/verification.json
e confirme que o último build de Pages terminou com sucesso.

Para continuar no Codex, abra a pasta do projeto e peça para ler HANDOFF.md e README.md.
Após alterações, regenere o manifesto antes de publicar uma nova versão.
A branch main guarda o projeto completo. Publique dist/ na raiz da branch gh-pages.

## Atualização de 18/11/2026 — arquivo 2023 preparado

As 11 páginas públicas da conferência de 2023 foram copiadas para dist/conferences/2023/, com 11 rotas legadas em dist/home/. A entrada Conferências do site aponta ao arquivo local. Fontes públicas, inventário, testes e limitações: docs/conference-2023-validation.md. Um logotipo que já estava ausente na origem foi substituído por versão da biblioteca do WordPress; dois vídeos permanecem externos.

O grupo aprovou a migração do domínio. O DNS público usa ns4928/ns4929.banahosting.com. MX e mail apontam para o domínio principal: não trocar o A sem resolver antes eventual dependência de e-mail. Plano em docs/domain-migration-plan.md. Nenhum DNS alterado, nenhum CNAME de produção ativado, nenhum serviço cancelado.

Próxima ação: revisar e autorizar a versão preparada para publicação no GitHub Pages existente. Depois conferir a publicação e coordenar o DNS com o colega, confirmando primeiro o uso de e-mail.

PO_MAGICO_SOURCE: ../po-magico (somente leitura)
PO_MAGICO_VERSION_USED: v20261111.001
PO_MAGICO_LAST_CHECKED: 2026-11-18
PO_MAGICO_CHECKPOINT: delivery (candidato local do arquivo 2023)
PO_MAGICO_DELTA_ADOPTED: no
PO_MAGICO_LESSON_CANDIDATE: MX e mail podem depender do mesmo A que o site; preservar o valor do MX sem revisar a resolução não preserva o e-mail.
Pó Mágico local bb32f274 e remoto 3a50be1d diferiam na conferência anterior desta sessão. Sem atualização do arquivo ou declaração de conformidade integral. Rota SITE_EXISTING_REVISION + SITE_STATIC, overlay S0_STATIC. Modelo efetivo informado pelo runtime: gpt-6.1-sol; esforço e custo não expostos.
