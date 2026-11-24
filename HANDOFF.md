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

## Facebook oficial no rodapé — 19/11/2026

Usuário forneceu os links do perfil Red Lafmat e autorizou inclusão, commit e deploy na produção existente. O link compartilhado redirecionou ao perfil 61583070328062; a forma curta https://www.facebook.com/61583070328062 retornou HTTP 200, título Open Graph Red Lafmat e o mesmo endereço canônico fornecido pelo usuário. Não foi identificado um nome de usuário curto personalizado; não inventar um alias. URL sem parâmetros de compartilhamento salva em siteContent.facebook e exibida ao lado do YouTube no rodapé de todas as páginas/idiomas, com noopener noreferrer. Cache atualizado para content.js/site.js. Manifesto LAFMAT-20261119-8A801A13DAB6, 589 arquivos conferidos; sintaxe JS, renderização do rodapé EN/PT/ES e verificação rápida de segurança PASS, sem gatilhos sensíveis. Alteração estática S0; reversão por revert deste commit. Arquivos locais output/ não fazem parte desta publicação. Destino autorizado: main → Vercel lafmat-revisao, msr-brs-projects → https://lafmat.com/.

PO_MAGICO_CHECKPOINT: change/delivery (Facebook autorizado)
PO_MAGICO_LAST_CHECKED: 2026-11-19 (regras da sessão reutilizadas; divergência do arquivo registrada acima)
PO_MAGICO_DELTA_ADOPTED: no

## Agenda atualizada — 22/11/2026

Lista fornecida pelo usuário incorporada: 33 sábados de 28/11/2026 a 10/07/2027. Título e afiliação UFRJ de Debora Vasconcelos corrigidos; Gema Monserrate Zambrano Baque, título e moderação de Juan Primera inseridos em 12/12. 26/06 e 03/07 sem programação definida; 10/07 reservado sem palestra para possível Fórum em Lima, a confirmar, nos três idiomas. Demais palestrantes, moderadores, convidados, indicações, feriados e pendências preservados conforme a lista. E-mails pessoais fornecidos não publicados. Verificadas 33 datas consecutivas aos sábados, estados e campos alterados; sintaxe, manifesto de 591 arquivos e segurança rápida PASS. Manifesto LAFMAT-20261122-FFA2DB95836A. Publicação autorizada no site existente, main → Vercel lafmat-revisao / msr-brs-projects. Reversão por revert do commit desta atualização. output/ mantido fora da publicação.

PO_MAGICO_CHECKPOINT: change/delivery (agenda fornecida pelo usuário)
PO_MAGICO_LAST_CHECKED: 2026-11-22 (regras da sessão reutilizadas; divergência do arquivo registrada acima)
PO_MAGICO_DELTA_ADOPTED: no

## Destaque Débora Vasconcelos — 23/11/2026

Folder original fornecido pelo usuário copiado sem edição para dist/assets/debora-vasconcelos-2026-11-28.jpg (1600×900). weeklyBanner atualizado para 28/11/2026, com texto alternativo PT/EN/ES. A home e a seção de seminários já exibem o próximo evento e seu folder correspondente; conferidos Débora como próximo evento, presença da imagem nos três idiomas e ocultação automática quando a próxima data mudar. Título, UFRJ e moderação de Isaias permanecem na agenda atualizada. Manifesto LAFMAT-20261123-BCB04519421A, 592 arquivos, sintaxe e segurança rápida PASS. Publicação solicitada no site existente via main/Vercel; reversão pelo commit desta alteração. Outros arquivos e output/ preservados.

PO_MAGICO_CHECKPOINT: change/delivery (destaque e folder autorizados)
PO_MAGICO_LAST_CHECKED: 2026-11-23 (regras da sessão reutilizadas)
PO_MAGICO_DELTA_ADOPTED: no


## Changes de SEO e medição criadas — 23/11/2026

Usuário pediu criar as Changes após a avaliação da migração. Backlog local em .specs/roadmap.md, contrato compartilhado .specs/shared/discovery-contract.md e sete Changes 001–007: inventário/baseline; posse Search Console; URLs reais/HTML estático; SEO técnico/redirects; GA4/privacidade; submissão/vínculo/validação Google; acompanhamento. Todas PLANEJADAS, sem implementação, nova automação, mutação de contas/DNS, commit, push ou deploy neste turno. Sequência nova conferida: não havia .specs/changes anterior. As entregas históricas de site permanecem concluídas; numeração refere-se somente ao novo ciclo.

Próxima Change: 001-inventory-and-seo-baseline. Plano de rota standard/medium (modelo concreto a confirmar no runtime). Publicação de URLs reais e redirects prevista em candidato integrado 003+004; não deixar sitemap ou destino apontar para páginas ainda ausentes. Alterações na geração HTML dos vídeos devem considerar o escopo restrito da automação atual. Conteúdo da conferência 2023, WordPress antigo e dados privados preservados. Memória continua neste HANDOFF; sem novo project-state.md.

PO_MAGICO_SOURCE: ../po-magico (somente leitura)
PO_MAGICO_VERSION_USED: v20261111.001
PO_MAGICO_LAST_CHECKED: 2026-11-23
PO_MAGICO_CHECKPOINT: classification/change/delivery (backlog SEO solicitado)
PO_MAGICO_DELTA_ADOPTED: no
PO_MAGICO_LESSON_CANDIDATE: em migração no mesmo domínio, redirects pertencem ao servidor atual; HTML derivado exige sincronização com a rotina de vídeos.
Regras da sessão e blueprint site/segurança reutilizados. Divergência do método local/remoto anteriormente registrada permanece; sem declaração de conformidade integral. Modelo efetivo: Codex; ID/razão/token/custo não expostos ou medidos neste registro.


## Change 001 concluída — 23/11/2026

Após "segue", executado inventário local e amostra pública somente leitura: docs/seo/baseline.md, CSVs e recibos. 1.672 URLs, 1.125 entradas no mapa, 31 páginas/posts publicados e 512 registros de mídia cobertos. 50 consultas: 27 finais 200, 18×404 e 5×403. Há 12 páginas/posts antigos 404, incluindo galerias anuais 2022–2026; oito aliases gerais 200/noindex/meta refresh. 18 mídias têm hash idêntico a binário do dist. Restam 1.035 decisões justificadas de revisão (principalmente páginas de anexos e mídias), não falhas HTTP presumidas.

Scripts seo_inventory.py, seo_probe.py e verify_seo_inventory.py reproduzem e validam a coleta com backup privado local; não copiam corpos/contatos para docs e não baixam mídias. Manifesto público igual ao local LAFMAT-20261123-BCB04519421A; dist inalterado. Testes de inventário e segurança rápida PASS. Sem commit/push/deploy, alteração Google/DNS/WordPress ou reauditoria editorial da conferência 2023.

Próxima Change canônica: 002-search-console-ownership; requer acesso à conta/propriedade correta. Rota prevista tier standard/medium, runtime específico a confirmar. Modelagem de URLs e implementação permanecem 003/004; não publicar redirecionamentos genéricos antes de resolver equivalências. Nenhuma nova automação criada.

PO_MAGICO_CHECKPOINT: delivery (Change 001 concluída)
PO_MAGICO_LAST_CHECKED: 2026-11-23
PO_MAGICO_DELTA_ADOPTED: no


## Change 002 iniciada — 23/11/2026

Search Console oficial aberto no Chrome autenticado de Mario; lafmat.com não listado nessa conta. Preparado fluxo de propriedade de domínio até diálogo TXT, sem clicar Verify. Namecheap Login aberta, requer intervenção do usuário; não tentar senhas antigas ou contornar autenticação. Abas marcadas para handoff. Nenhum TXT/DNS alterado ou controle de propriedade concedido. Antes de verificar posse, obter confirmação no momento da ação para a conta Google concreta, conforme política do navegador. Registro em docs/seo/search-console.md. Métricas LAFMAT ainda não verificadas. Próximo passo: usuário autentica Namecheap, conferir domínio/DNS, preparar TXT e finalizar verificação autorizada. Não avançar como se Change concluída.

PO_MAGICO_CHECKPOINT: resume/change (Change 002 em andamento)
PO_MAGICO_LAST_CHECKED: 2026-11-23
PO_MAGICO_DELTA_ADOPTED: no


Retomada Change 002 no Safari: usuário já autenticado na Namecheap, domínio lafmat.com e Advanced DNS confirmados. Registro TXT ainda não inserido; Google permanece no diálogo de verificação na conta Mario do Chrome. Ação nativa no botão Add New Record não disponível por célula AX sem ação; tentativa por coordenadas falhou noWindowsAvailable. Pedido pontual de clique manual enviado. Antes de salvar TXT que concede posse à conta Google concreta, confirmar a ampliação de acesso no momento da ação conforme política do navegador. Não houve qualquer edição DNS ou credencial.


24/11/2026 — Usuário confirmou explicitamente a conta Google Mario (mesma conta apresentada na pergunta) para posse Search Console. Não pedir novamente autorização dessa mesma concessão. Linha nova DNS ainda vazia/A Record observada no Safari; nenhuma gravação. Uso simultâneo do Safari interrompeu seleção de TXT e mudou de aba; solicitado estabilizar Advanced DNS. Não ler conteúdo de outras abas. Continuar da linha existente, sem criar duplicata; salvar só TXT @ exato do diálogo Google, conferir DNS e Verify.


24/11/2026, retomada com controle exclusivo: campos TXT @ / valor Google preenchidos corretamente; botão salvar por coordenada completa do screenshot retornou Failed to save record. Refresh levou ao login Namecheap, comprovando sessão expirada. Usuário solicitado a entrar de novo no Safari. Não pedir autorização Google novamente. Após autenticação, conferir TXT existente para evitar duplicata e salvar em painel fresco. Não clicar centro da célula AX Save/Cancel (aciona Cancel); usar marca de salvar da imagem. Nenhum registro DNS alterado ou verificação Google concluída.


## Change 002 — posse Google concluída, 24/11/2026

Após login renovado Namecheap no Safari, salvo um único TXT @ Google (Automatic). Cloudflare e Google DNS retornaram o valor. A/CNAME/www e NS permanecem iguais, manifesto HTTPS público igual ao local. Google mostrou Ownership verified; propriedade sc-domain:lafmat.com acessível. Settings: verified owner; Users (1): Mario Reis, Owner Verified, conta expressamente autorizada pelo usuário. Não pedir de novo autorização dessa mesma conta/operação. Manter TXT para preservar posse.

Desempenho e Pages ainda processam; não há dados históricos exportáveis confirmados. Sitemaps 0; ações manuais/segurança sem problemas. Relatório HTTPS atualizado 23/11 tem 14 URLs HTTPS e 1 HTTPS not evaluated (não equivale a falha TLS atual); URL específica pendente para 004/006. Exportação CSV HTTPS tentada, mas download não retornou arquivo e controle CUA reiniciou; não afirmar CSV exportado. Baseline observada estruturada em docs/seo/search-console-baseline-2026-11-24.json; recibo DNS em search-console-dns-2026-11-24.json. Screenshot: pasta de visualizações, lafmat-search-console-verified.jpg.

Estado: posse/acessos concluídos; exportações aguardam Google. Próxima Change canônica 003-indexable-static-routes, rota planejada standard/medium, sem implementação iniciada. Manter release integrado 003+004. Sem WordPress/conferência, GA4, envio sitemap ou Change of Address; nenhum commit/push/deploy de site.

PO_MAGICO_CHECKPOINT: delivery (Change 002: posse comprovada com limites de dados)
PO_MAGICO_LAST_CHECKED: 2026-11-24
PO_MAGICO_DELTA_ADOPTED: no


## 24/11/2026 — Change 003: HTML e rotas, candidato local

Usuário autorizou especificamente executar a Change 003. Implementada e testada localmente: 42 páginas (sete seções × três idiomas + sete anos de vídeos × três idiomas), sem novo framework/dependência. Fontes editoriais, catálogo 306, conferência e aliases intactos. Renderizador comum ao build/navegador, links reais, compatibilidade hash, no-JS, filtros/idiomas/submenu preservados. Ver `docs/seo/route-contract.md` e recibos `static-build.json`, `static-http-validation-2026-11-24.json`, `static-browser-validation-2026-11-24.json`.

Candidato: LAFMAT-20261124-B80A75C9CAC0, SHA256 b80a75c9cac0adcf71039cc52264cbf848e6dda8f25fdf85398231ed775b0c79, 635 arquivos. Manifesto público confirmado anterior LAFMAT-20261123-BCB04519421A. Nenhum commit/push/deploy. Próxima é 004: integrar SEO técnico e redirecionamentos com esse candidato antes de publicar. Não confundir novo manifesto local com identidade pública.

Build: `node scripts/build_site.cjs`; verificar com `node scripts/verify_static_site.cjs`, depois `python3 scripts/update_manifest.py` e `python3 scripts/verify.py`. update_manifest agora bloqueia fonte/HTML divergentes. Testes locais: 42 HTTP 200 idênticos ao arquivo, 404 real, 2.952 links/assets, 306 gravações, 33 datas, rebuild determinístico, fixture obsoleta bloqueada, vídeos/8 testes de sync/conferência/inventário/security fast check/diff check PASS. Navegador desktop/tablet/celular e com CSP script-src none conferidos. Formulário só rascunho, sem envio externo.

PENDÊNCIA DE RELEASE: autorização atual da automação diária ainda limita-se catálogo/miniaturas/manifesto. Não foi alterada. Antes de ativar 003+004, obter autorização específica para build/validação e outputs HTML/recibo derivados e atualização diária mesmo sem vídeo novo; atualizar automação pela ferramenta própria. JS usa data corrente; HTML sem JS usa data do build. Não publicar candidato parcial ou ignorar a divergência de escopo na rotina.

PO_MAGICO_SOURCE: ../po-magico
PO_MAGICO_VERSION_USED: v20261111.001
PO_MAGICO_LAST_CHECKED: 2026-11-24
PO_MAGICO_CHECKPOINT: change/delivery — 003 local
PO_MAGICO_DELTA_ADOPTED: yes — blueprint SITE_EXISTING_REVISION + STATIC + ROUTE_PRESERVATION, overlay S0; mesma stack, conteúdo comum e prova de paridade
PO_MAGICO_LESSON_CANDIDATE: guard do manifesto deve rejeitar outputs HTML derivados obsoletos e expansão de manutenção recorrente deve ser autorizada antes da ativação
Divergência local/remoto anteriormente registrada permanece; não houve sincronização nem declaração de conformidade integral. Modelo efetivo: Codex, identificador exato/reasoning/custos não expostos neste registro.


## 24/11/2026 — Change 004, candidato integrado preparado (não publicado)

Usuário autorizou executar 004, consolidar os 11 aliases de conferência e ampliar manutenção recorrente para HTML/sitemap/recibo. Implementado SEO compartilhado (seo.js), canonical/idiomas/OG/Organization, PNG social original, robots/sitemap 54 entradas, Vercel 121 redirects e 149 padrões incluindo headers; canonical de arquivo via Link HTTP. Nenhum arquivo editorial de conferência alterado. Oito wrappers gerais apontam rotas reais como fallback estático. 1.672 decisões em docs/seo/migration-decisions.csv, com exceções para recursos antigos sem equivalente; sem publicar backups.

Candidato local: LAFMAT-20261124-C125577914F0, SHA256 c125577914f0324a44e7a33a6113540606d322cb46c680aaec1320a1a5d238f9, 641 arquivos. verify_static 42/3.204 links, verify_seo 54 sitemap/121 rules/1.672 decisões, vídeos/sync/conferência/inventário/security fast check PASS. Schema público compatibilizado e padrões compilados por dependências já no cache de ferramentas, sem dependência nova do projeto. Não é prova do runtime Vercel. Estado em docs/seo/release-validation.md e .specs/004.

Vercel CLI 66.2.0 confirmou projeto prj_ERGGYeDVgxuIo9wDkeo0CxGXfzzc, time msr-brs-projects, root dist, Git main. Conector retornou 404 na conta desta sessão; não criar projeto novo. Link local criou .env.local com credencial efêmera; removida sem leitura; .env* ignorado. Auto-review recusou vercel build --prod --yes por poder baixar variáveis de produção, portanto não executar nem contornar. Usar testes estáticos ou implantação autorizada sem puxar env.

Baseline HEAD: 1.722 URLs, 629×200/519×404/574×403; resultados 403 reclassificados como UNVERIFIED porque GET/HEAD depois mostraram Vercel Security Checkpoint e x-vercel-mitigated challenge. Parar varreduras; não tratar challenge como mídia inexistente e não bypass/mudar firewall. scripts/probe_seo_release.py agora para em challenge/429. Navegador público também mostrou verificação de navegador; não afirmar acesso operacional por cliente automatizado nesse momento. Ver recibo pre-release-http-2026-11-24.json.

AUTOMAÇÃO PENDENTE: id antigo atualizar-v-deos-lafmat não tem automation.toml local. View renderiza card, sem expor configuração ao agente. Updates parciais via tool foram rejeitados por schema (nenhuma mudança aplicada). Ferramenta exige kind/model/rrule/projectId/etc para cron; não inventar configuração anterior. Foi perguntado se pode substituir por heartbeat vinculado a este chat às 09h de Brasília, failed_runs_only, escopo ampliado; resposta ainda pendente neste checkpoint. Prompt salvo em .specs/changes/004.../automation-prompt.md. Não criar duplicata nem declarar atualização ativa antes de ferramenta bem-sucedida.

PO_MAGICO_SOURCE: ../po-magico
PO_MAGICO_VERSION_USED: v20261111.001
PO_MAGICO_LAST_CHECKED: 2026-11-24
PO_MAGICO_CHECKPOINT: change — 004 preparação local
PO_MAGICO_DELTA_ADOPTED: yes — manter evidência de challenge distinta de 404; decisão por URL; fonte comum e autorização recorrente específica
PO_MAGICO_LESSON_CANDIDATE: sondagem de migração deve parar em x-vercel-mitigated=challenge e não apenas em HTTP 429
Divergência do arquivo local/remoto do método previamente registrada continua; não houve sincronização nem declaração de conformidade integral.

Atualização de preparação: arquivos gerados normalizados para LF/sem whitespace de fim de linha; candidato atual LAFMAT-20261124-20C36699ED23, SHA256 20c36699ed232c98379718c4fa0a9587e11bf08ab3fa34e476dc42affa911aea. Navegador público concluiu automaticamente a verificação normal da Vercel e abriu a versão de produção anterior; não houve bypass, mudança de firewall ou CAPTCHA manual. 403 do lote continuam sem provar origem/ausência.

Checkpoint final de preparação 004: commit LOCAL d45f880c2d5f2c290a9d762cdcce151fa723ae07 (164 arquivos; output/ excluído). Nenhum push/deploy. Manifesto 20C36699ED23. Perguntas pendentes no UI: substituir rotina antiga por heartbeat diário 09h e publicar revisão exata no projeto/domínio existentes. Não inferir respostas por tempo. Gate local em docs/seo/release-gate-2026-11-24.json: BLOCKED operacional até respostas/aceite real; verificações locais PASS. Antes de alterar fonte após aprovação, conferir vínculo da autorização à revisão.


## Fechamento 24/11/2026 — Changes 003+004 PUBLICADAS E VALIDADAS

Usuário autorizou expressamente publicar d45f880 em lafmat.com e substituir a rotina mantendo 09h/avisos apenas em falha. Push main concluído. Vercel READY dpl_CJWnMJJbfTAbgEnw9CUqzstuoyqg (lafmat-revisao-dzhhb4ry6-msr-brs-projects.vercel.app), implantação Git d45f880. Manifesto público e local idênticos LAFMAT-20261124-20C36699ED23 / SHA256 20c36699ed232c98379718c4fa0a9587e11bf08ab3fa34e476dc42affa911aea / 641 arquivos. Nenhum arquivo dist mudou após o commit aprovado.

Aceite real PASS: 305 requisições públicas pausadas/sequenciais, 54 páginas canônicas, 42 HTML com hash exato, 121 casos de regras permanentes com destinos/status corretos e sem loops, sitemap/robots/PNG/manifesto com bytes iguais, 404 real e HTTPS/www; dez assets incluindo PDF/ZIP com hashes preservados. Proteção individual confirmada por 302 para vercel.com/sso-api, sem desproteger previews. Navegador produção: idiomas, galeria/anos/filtros, recarga, links hash, conferência, membros, rascunho de contato (sem envio), móvel 390/desktop 1280, sem overflow/imagens quebradas observadas nem erro de aplicação. Recibos post-release-*.json e release-gate JSON PASS.

Automação antiga atualizar-v-deos-lafmat não existia no cadastro: delete retornou not_found. Substituta atualizar-v-deos-e-seo-lafmat criada e atualizada pela ferramenta, ACTIVE, heartbeat neste chat, diária 09h de Brasília, notificationPolicy failed_runs_only. Prompt aprovado/registado em .specs/004/automation-prompt.md e recibo automation-replacement-2026-11-24.json. Usa dados de agenda já cadastrados, não descobre novos seminários. Não baixa vídeos, publica só alterações relevantes após testes e preserva fontes/WordPress/DNS/conferência. output/ local não bloqueia por si só, mas nunca é lido/staged. Disparo futuro não observado; depende de disponibilidade local do Codex/computador.

Exceções históricas de mídias/páginas sem equivalente mantidas conforme autorização; não afirmar recuperação integral. 403 do lote inicial continuam inconclusivos por antigo challenge; checagens finais passaram sem challenge, sem bypass ou alteração de firewall. Nenhum GA4 instalado nem sitemap submetido ao Google: próximas Changes 005/006, sem execução automática.

PO_MAGICO_SOURCE: ../po-magico
PO_MAGICO_VERSION_USED: v20261111.001
PO_MAGICO_LAST_CHECKED: 2026-11-24
PO_MAGICO_CHECKPOINT: delivery/closure — 003+004
PO_MAGICO_DELTA_ADOPTED: yes — fonte comum, gate exato, prova do host e contrato recorrente efetivo
PO_MAGICO_LESSON_CANDIDATE: aceitar 302 para login como proteção de implantação; parar sondagem em challenge; comprovar rotina real em vez de confiar em memória de cadastro antigo
Método local/remoto permanece divergente conforme histórico, sem sincronização do arquivo de método. Modelo efetivo Codex, identificador exato/custo/latência não expostos.
