# Suspensão reversível do WordPress antigo — 19/11/2026

Autorização explícita do usuário: entrar no WordPress e suspender a página completa, sem apagar conteúdo. Escopo: instalação antiga em /home/ na hospedagem anterior, não o site Vercel.

## Cópia preservada

Exportação nativa WXR (2.898.367 bytes), validada como XML, com 29 páginas, 2 entradas, 512 anexos, menus, layouts Divi e outros objetos de conteúdo. Os 512 arquivos de mídia foram copiados da origem antiga, sem falhas, totalizando 555.440.046 bytes. Hashes SHA-256 dos arquivos e CRC do ZIP foram conferidos.

Backup privado local: `.private-backups/wordpress-content-and-media-2026-11-19.zip` (558.627.916 bytes). A pasta detalhada está em `.private-backups/wordpress-2026-11-19/`. Esses caminhos estão excluídos do Git e fora da pasta pública dist. A exportação nativa original também ficou em Downloads.

É uma cópia de conteúdo WXR e mídias; não é um dump SQL nem uma cópia integral de WordPress, plugins e tema. O original completo permanece no servidor, sem exclusão. O arquivo privado README.txt descreve o escopo e a restauração.

## Alteração e verificação

Instalado e ativado somente Slim Maintenance Mode 1.4.6, do diretório oficial WordPress.org. Código revisado: não contém exclusão de conteúdo; mostra manutenção/HTTP 503 aos visitantes e mantém a visualização para administradores. Pacote oficial revisado SHA-256: 1a60cfbaea8fad92c3433e77e3e493cb4660ebc0c5684d10e4cb2e075139613a.

Após a ativação, o painel confirmou manutenção ativa e os mesmos 29 páginas e 2 entradas. Requisições anônimas à origem antiga para /home/, /home/know-us/, /home/program/ e /home/feed/ retornaram 503 com mensagem de manutenção, usando TLS válido. Os dois nomes públicos lafmat.com e www.lafmat.com continuaram respondendo 200 em HTTPS pela Vercel, sem exceção de certificado.

O acesso pontual à origem antiga usou TLS validado e uma ponte exclusivamente local com rotas de alteração limitadas à instalação/ativação/desativação desse único plugin, após verificação do backup. Essa ponte foi encerrada ao terminar; nenhuma credencial foi adicionada ao projeto ou ao Git. Não foram feitas alterações de DNS, conteúdo, tema, versão do WordPress, PHP ou hospedagem nesta suspensão.

## Reversão

Um administrador pode voltar ao painel da instalação antiga e desativar Slim Maintenance Mode. Não é necessário restaurar ou recriar páginas para reabrir o site. O domínio público permanece na Vercel; eventual administração da origem antiga exige acesso à hospedagem antiga ou roteamento temporário validado. Não cancelar BanaHosting ou registro do domínio sem instrução específica do usuário.

Release gate: PASS para a alteração limitada na origem antiga, com backup validado, ação reversível, verificação de visitante anônimo, preservação dos totais de conteúdo e site novo conferido. Evidências detalhadas e captura do painel permanecem na pasta privada do backup.
