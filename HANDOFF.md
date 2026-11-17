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
