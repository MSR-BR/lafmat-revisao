# Migração para Vercel — 19/11/2026

O usuário autorizou expressamente migrar a hospedagem, configurar lafmat.com e concluir HTTPS sem avisos no navegador. O domínio permanece registrado na Namecheap, com BasicDNS e os mesmos nameservers dns1/dns2.registrar-servers.com. O usuário confirmou anteriormente que não há caixas de e-mail nem encaminhamentos em uso. Hospedagem antiga, renovação do domínio e registros cpanel/ftp/webmail não foram cancelados.

## Publicação e acesso

- Time: msr-brs-projects; projeto: lafmat-revisao, prj_ERGGYeDVgxuIo9wDkeo0CxGXfzzc.
- Projeto existente reativado. O conector tinha acesso limitado; a operação foi concluída pelo CLI Vercel 66.2.0, autenticado como msr-br.
- Fonte da implantação preparada: 5127226dff71607a6e376c68edcd30199f92e16e, pasta dist.
- Implantação testada e promovida sem reconstrução: dpl_5BWBA9U68jsLrhWep2fDnoCHDSfR.
- Código: LAFMAT-20261118-6D2C6003288B. Os 281 arquivos públicos passaram na comparação SHA-256 pelo endereço https://lafmat.com, com TLS normal. CNAME e .nojekyll são metadados de hospedagem histórica e não fazem parte dessa conferência HTTP.
- Domínio de produção público; autenticação Vercel mantida em previews e URLs individuais de implantação (prod_deployment_urls_and_all_previews). Credencial temporária criada pelo CLI para testar a implantação protegida foi revogada após os testes. Nenhuma credencial foi incluída no repositório.
- Integração Git conectada a MSR-BR/lafmat-revisao; produção main, Root Directory dist, framework Other e arquivos externos à pasta de build desabilitados. Futuras publicações vêm do repositório canônico.

## DNS e certificado

Registros fornecidos pela Vercel para este projeto, TTL 300:

- A @: 216.198.79.1 e 64.29.17.1.
- CNAME www: 0986d6ca91bddc7d.vercel-dns-017.com.
- Dois TXT _acme-challenge e _acme-challenge.www foram publicados para emissão antecipada do certificado, sem trocar os nameservers.

Certificado Let's Encrypt emitido cobrindo lafmat.com e www.lafmat.com, válido até 17/02/2027; renovação gerenciada pela Vercel. TLS foi validado antes do apontamento diretamente nos dois IPs com SNI e validação de certificado habilitada. A configuração dos dois nomes foi aprovada pela Vercel, com desafio HTTP-01 aceito para a hospedagem final. www é configurado como redirecionamento permanente 308 para lafmat.com.

## Verificação e contingência

Manifesto, entrada, JavaScript, conferência, rota com sublinhado, PDF e ZIP foram testados antes da promoção. Os 281 arquivos passaram novamente em HTTPS no domínio canônico. Navegação principal em português e submenu Conferências → 2023 foram exercitados no navegador; a edição abre em outra aba no próprio lafmat.com, com suas onze páginas. Vídeos YouTube e referências institucionais permanecem serviços externos, conforme o arquivo original.

Evidências detalhadas: vercel-https-validation-2026-11-19.json. Não declarar teste de envio de e-mail: o contato continua abrindo mailto e não há backend de envio.

Para falha futura de conteúdo, usar rollback de implantação na Vercel, preservando DNS e certificado. A implantação testada acima fica como versão recuperável. A cópia local e a branch gh-pages também foram preservadas. O apontamento anterior do GitHub tinha quatro A 185.199.108–111.153 e www CNAME msr-br.github.io; não restaurá-lo automaticamente, pois o certificado do GitHub continuava pendente.

Release gate: PASS para a publicação estática S0, com verificações locais de manifesto e paridade das 22 páginas, configuração de produção restrita à pasta pública, proteção de previews preservada, certificado validado e 281 arquivos conferidos. Não há alteração de autenticação da aplicação, backend, banco de dados ou dependências de produção.

Verificação final: HTTP e HTTPS, com e sem www, terminam em https://lafmat.com/ com status 200 e validação TLS 0. Um PDF solicitado via www também termina no mesmo caminho do domínio canônico. O cache DNS local macOS foi limpo com dscacheutil -flushcache; a resolução normal passou a retornar os IPs da Vercel. Estado: HTTPS_OPERATIONAL.
