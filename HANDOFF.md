# Continuidade em outro computador

O projeto canônico é este repositório, MSR-BR/lafmat-revisao, branch main.
O conteúdo editável e publicado fica em dist/. A Vercel publica a branch main, com Root Directory dist, no projeto lafmat-revisao do time msr-brs-projects. A branch gh-pages conserva uma publicação de contingência.
Não trabalhar na antiga cópia temporária em /tmp.

A versão pública canônica é https://lafmat.com/.
A Vercel foi reativada em 19/11/2026, com certificado emitido para lafmat.com e www.lafmat.com. A migração para Vercel foi expressamente autorizada pelo usuário após o bloqueio de emissão no GitHub Pages.
A conferência 2023 está preservada no próprio site, sem depender do WordPress para imagens, PDF ou ZIP. O usuário confirmou que não há e-mail nem encaminhamento @lafmat.com em uso. Não cancelar a hospedagem antiga ou o registro do domínio.

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
https://lafmat.com/verification.json
e confirme que o último deploy de produção da Vercel terminou com sucesso.

Para continuar no Codex, abra a pasta do projeto e peça para ler HANDOFF.md e README.md.
Após alterações, regenere o manifesto antes de publicar uma nova versão.
A branch main guarda o projeto completo e dispara a publicação Vercel pela integração Git. Não publique a raiz completa como conteúdo estático: a pasta pública é dist/. A branch gh-pages é histórica/de contingência.

## Atualização de 18/11/2026 — arquivo 2023 preparado

As 11 páginas públicas da conferência de 2023 foram copiadas para dist/conferences/2023/, com 11 rotas legadas em dist/home/. A entrada Conferências do site aponta ao arquivo local. Fontes públicas, inventário, testes e limitações: docs/conference-2023-validation.md. Um logotipo que já estava ausente na origem foi substituído por versão da biblioteca do WordPress; dois vídeos permanecem externos.

O grupo aprovou a migração do domínio. O DNS público usa ns4928/ns4929.banahosting.com. MX e mail apontam para o domínio principal: não trocar o A sem resolver antes eventual dependência de e-mail. Plano em docs/domain-migration-plan.md. Nenhum DNS alterado, nenhum CNAME de produção ativado, nenhum serviço cancelado.

Publicação do arquivo de 2023 e do submenu anual autorizada pelo usuário em 18/11/2026. O menu Conferências abre uma lista expansível; 2023 abre o arquivo em outra aba. Novos anos são acrescentados em siteContent.conferences. Próxima ação após a publicação: coordenar o DNS com o colega, confirmando primeiro o uso de e-mail.

PO_MAGICO_SOURCE: ../po-magico (somente leitura)
PO_MAGICO_VERSION_USED: v20261111.001
PO_MAGICO_LAST_CHECKED: 2026-11-18
PO_MAGICO_CHECKPOINT: delivery (candidato local do arquivo 2023)
PO_MAGICO_DELTA_ADOPTED: no
PO_MAGICO_LESSON_CANDIDATE: MX e mail podem depender do mesmo A que o site; preservar o valor do MX sem revisar a resolução não preserva o e-mail.
Pó Mágico local bb32f274 e remoto 3a50be1d diferiam na conferência anterior desta sessão. Sem atualização do arquivo ou declaração de conformidade integral. Rota SITE_EXISTING_REVISION + SITE_STATIC, overlay S0_STATIC. Modelo efetivo informado pelo runtime: gpt-6.1-sol; esforço e custo não expostos.

Publicação concluída em 18/11/2026: fonte 4417590; gh-pages 5fcff81662a12e00062edafa99e1d6164eade2ca; build 44301750393 com sucesso. Código local/público LAFMAT-20261118-43C708ED85A2, 39 arquivos novos/alterados conferidos byte a byte por SHA-256 na produção. Conferências → 2023 publicado; arquivo e site abertos em abas separadas. Recibo completo: docs/deployment-2026-11-18.md. Próxima ação: preparar a mudança de domínio com a revisão de e-mail descrita no plano; domínio ainda não alterado.


## Migração de domínio autorizada e aplicada — 18/11/2026

O usuário confirmou que não há caixas de e-mail nem encaminhamentos @lafmat.com em uso. Nameservers alterados para Namecheap BasicDNS (dns1/dns2.registrar-servers.com) na conta existente darkger, sem transferência de titularidade. Os quatro A do GitHub, www CNAME msr-br.github.io e cpanel/webmail/ftp no IP antigo foram salvos e conferidos. Mail Settings: No Email Service. Hospedagem antiga mantida.

GitHub Pages: cname lafmat.com; fonte 2eca68c; publicação 5c6d8c2ebfc24ee576ea183a35438d86dfec385d; build 44410633742 success. Manifesto LAFMAT-20261118-F6344655EC91. Oito aliases de navegação antiga foram acrescentados, incluindo /home/. Detalhes e rollback: docs/domain-cutover-2026-11-18.md.

ESTADO: DNS_APPLIED_HTTPS_PENDING. A confirmação do certificado e HTTPS obrigatório é a próxima etapa, já autorizada. Consultar GET repos/MSR-BR/lafmat-revisao/pages e /pages/health. Quando o certificado estiver approved, ativar https_enforced=true e validar os domínios raiz e www, manifesto, submenu e conferência. Não finalizar como sucesso integral antes desses testes. O DNS público já está correto; o resolvedor do GitHub e o resolvedor local ainda mostraram cache antigo na última consulta. Nunca contornar validação de certificado.

PO_MAGICO_CHECKPOINT: change (migração DNS autorizada)
PO_MAGICO_LAST_CHECKED: 2026-11-18
PO_MAGICO_DELTA_ADOPTED: no


Retomada de finalização HTTPS, 18/11/2026: reaplicado domínio e executado um ciclo de remoção/reinserção recomendado pelo GitHub. Publicação mais recente 372167a36e14b472278609383e1dbf5ca691dc23, run 44414783704 success, mesma árvore validada de dist. Ativação explícita de HTTPS obrigatório retornou HTTP 404 “The certificate does not exist yet”; certificado ainda null após o deploy. Não repetir ciclos de domínio sem nova evidência. Consultar o estado e concluir quando o provedor emitir o certificado. Detalhes em docs/https-activation-attempt-2026-11-18.json.

### Retomada de finalização — 18/11/2026 20h

- Corrigida a omissão de `/home/__trashed/index.html` causada pelo processamento Jekyll: `dist/.nojekyll` presente.
- Main `b6d4baa`; publicação `8c3f7b223e03b49d3ce978906f294eaf4979792d`; deploy `44417044929` concluído com sucesso.
- Manifesto atual `LAFMAT-20261118-6D2C6003288B`. Os 281 arquivos públicos conferidos por HTTP com Host lafmat.com têm os hashes locais; CNAME e .nojekyll são metadados conferidos na árvore Git.
- Google, Cloudflare e OpenDNS retornam os quatro IPs novos. O resolvedor local e o diagnóstico do GitHub ainda retornam os dados antigos. A zona antiga BanaHosting continua respondendo IP antigo, TTL 14400. Cache de delegação/resolução é a hipótese sustentada pela divergência; não afirmar que é possível limpá-lo remotamente no GitHub.
- HTTPS continua pendente de emissão. PUT https_enforced=true retorna 404 The certificate does not exist yet. Não anunciar conclusão e não reiniciar domínio repetidamente. Finalização permanece autorizada sem nova confirmação.

### Nova tentativa — 19/11/2026

O resolvedor local agora retorna os quatro IPs do GitHub e o CNAME correto. Seis arquivos críticos passaram por HTTP normal, sem IP forçado, incluindo entrada, JavaScript, conferência, rota com sublinhado, PDF e ZIP. Reaplicado o domínio e solicitada reconstrução; depois removido e reinserido uma vez para reiniciar a solicitação TLS. Árvore estática exata preservada; publicação `fa0f7f80c330539d8bf019fb1ec495f873704709`, deploy `44518203082` concluído com sucesso. Monitorado após a publicação: certificado ainda ausente, ativação HTTPS recusada com 404 The certificate does not exist yet, TLS normal falha nos dois nomes. O diagnóstico GitHub ainda indica IP externo e MX presente, divergindo da zona pública atual. Não considerar concluído. Evidências em `docs/domain-retry-2026-11-19.json`.

## Produção Vercel operacional — 19/11/2026

Autorização: migrar para Vercel e concluir HTTPS sem aviso. Projeto lafmat-revisao reativado; implantação dpl_5BWBA9U68jsLrhWep2fDnoCHDSfR testada e promovida. Certificado Let's Encrypt válido para lafmat.com e www.lafmat.com, até 17/02/2027, renovação gerenciada pela Vercel. Os quatro acessos HTTP/HTTPS, com e sem www, passaram por resolução normal, com redirecionamento ao domínio canônico e validação TLS habilitada. Cache local macOS foi limpo sem alteração de rede.

281 arquivos públicos conferidos por SHA-256 em HTTPS, mesma versão LAFMAT-20261118-6D2C6003288B. Menu principal e Conferências → 2023 testados no navegador, com arquivo na própria origem. Origem futura: GitHub main, Root Directory dist na Vercel. Produção pública, previews protegidos. Credencial temporária de teste revogada. Registro, DNS Namecheap e hospedagem antiga preservados. Estado: HTTPS_OPERATIONAL. Evidências e rollback: docs/vercel-migration-2026-11-19.md e docs/vercel-https-validation-2026-11-19.json.

PO_MAGICO_CHECKPOINT: delivery (migração Vercel autorizada)
PO_MAGICO_LAST_CHECKED: 2026-11-19 (regras já carregadas nesta sessão; divergência local/remoto registrada acima permanece)
PO_MAGICO_DELTA_ADOPTED: no
Modelo efetivo: Codex; identificador específico não exposto neste turno.

## WordPress antigo suspenso — 19/11/2026

Por instrução explícita do usuário, o WordPress da origem antiga foi colocado em manutenção reversível com Slim Maintenance Mode 1.4.6. Visitantes anônimos recebem 503; administradores mantêm acesso. As 29 páginas e 2 entradas permaneceram no painel, sem exclusão. Backup privado WXR e 512 mídias, verificado por hashes/CRC, salvo em .private-backups/wordpress-content-and-media-2026-11-19.zip; pasta excluída do Git e fora de dist. Não é backup SQL/integral de plugins e tema; o original continua preservado. Detalhes e reversão em docs/wordpress-suspension-2026-11-19.md. A ponte local temporária foi encerrada. Vercel e HTTPS do domínio público continuam operacionais. Não retomar trabalho na conferência 2023 sem nova solicitação.

PO_MAGICO_CHECKPOINT: delivery (suspensão reversível do legado autorizada)
PO_MAGICO_LAST_CHECKED: 2026-11-19 (regras da sessão reutilizadas)
PO_MAGICO_DELTA_ADOPTED: no

## Atualização contínua da galeria — 19/11/2026

Usuário forneceu e autorizou consultar ambos os canais e manter a aba de vídeos sempre atualizada. Catálogo inicial conferido: 304 vídeos públicos (67 Lafmatnetwork, 237 GI MATEFUN), de 2020 a 2026, mais recente 14/11/2026. Exibição em 272 resultados, agrupando somente cópias de título e dia iguais em canais diferentes, sem perder os dois links. Títulos/datas/identidades vêm do YouTube; o arquivo WordPress antigo permanece intacto em archive.js. Foram encontrados links repetidos atribuídos a palestrantes diferentes e um link youtu.be sem identificador na cópia antiga; a galeria agora usa os vídeos conferidos dos dois canais.

Dados: dist/assets/videos.js; miniaturas locais em dist/assets/video-thumbnails/. Coletor: scripts/sync_youtube.py (--full para todo o histórico). Dependência de manutenção fixada em requirements-youtube.txt; venv/cache ignorados pelo Git e fora da produção estática. IDs dos dois canais validados, dados escapados na interface, futuras transmissões excluídas e falhas/HTTP 429 interrompem a sincronização sem publicar catálogo parcial. Metadados conhecidos são reaproveitados; títulos/datas históricos não são reextraídos diariamente.

FOLLOW_UP_STATE: ACTIVE
AUTOMATION_ID: atualizar-v-deos-lafmat
SCHEDULED_FOR: diariamente 09:00
TIMEZONE: America/Sao_Paulo
TARGET_THREAD_OR_PROJECT: este chat / lafmat web
MUTATION_POLICY: autorização recorrente do usuário para sincronizar e publicar somente dist/assets/videos.js, dist/assets/video-thumbnails/ e dist/verification.json; preservar alterações alheias, sem WordPress, conferência 2023, DNS, provedores ou outras seções. Automação local Codex; depende do computador/app disponível. Notificações apenas em falhas.

PO_MAGICO_CHECKPOINT: change/delivery (galeria e manutenção recorrente autorizadas)
PO_MAGICO_LAST_CHECKED: 2026-11-19 (regras já carregadas e política scheduled-follow-up consultada)
PO_MAGICO_DELTA_ADOPTED: no
