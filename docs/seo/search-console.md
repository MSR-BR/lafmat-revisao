# Search Console — Change 002

Data: 23/11/2026. Estado atual em 24/11/2026: POSSE VERIFICADA e acessos conferidos; desempenho/indexação ainda processando. As seções abaixo preservam o histórico das tentativas; o resultado final está ao fim.

## Evidência observada

A interface oficial do Google Search Console foi aberta no Chrome em uma conta Google autenticada de Mario Reis. O seletor de propriedades dessa conta não apresentou lafmat.com. Isso não prova ausência de propriedade em outras contas ou do antigo responsável; não foram consultados os dados de outros projetos.

Foi iniciado o fluxo Add property → website → Domain, informando lafmat.com. O Google apresentou o diálogo de verificação via TXT. A posse ainda NÃO foi verificada, e não foi aberto um painel de relatórios LAFMAT. Não se afirma criação de propriedade verificada nem coleta de métricas.

O usuário autenticou a Namecheap no Safari. Conferidos domínio lafmat.com ativo, Namecheap BasicDNS e painel Advanced DNS. A sessão Chrome Namecheap não é necessária. Foram observados os A de produção 216.198.79.1 e 64.29.17.1 e os A legados cpanel/ftp/webmail. A tabela mostra inicialmente cinco linhas e possui Show More; demais registros ainda precisam ser expandidos antes de afirmar inventário completo do painel. Nenhum registro DNS alterado. O botão Add New Record é apresentado dentro de célula sem ação acessível e o controle por coordenadas retornou noWindowsAvailable. Foi solicitado apenas o clique manual para abrir o editor, sem pedir senhas ou resets.

## Próximos passos concretos

1. Login já concluído no Safari; abrir editor Add New Record (intervenção manual solicitada para esse botão).
2. Conferir domínio e painel DNS correto; preparar exclusivamente um novo TXT de verificação no host @, sem substituir TXT existentes.
3. Antes de efetivar a comprovação de posse, confirmar a conta Google destinatária e a concessão de controle no Search Console. A política de uso do navegador exige confirmação no momento de criação/ampliação de acesso sensível.
4. Salvar o TXT, conferir resolução autoritativa/pública e executar Verify.
5. Só após prova de sucesso, registrar propriedade sc-domain:lafmat.com e consultar configurações, acessos, desempenho, indexação, sitemaps e segurança da LAFMAT.
6. Se houver propriedade antiga em outra conta, pedir compartilhamento ao responsável por mensagem apenas preparada, não enviada automaticamente. Não criar propriedades de prefixo redundantes sem necessidade.

## Limites e autorização

Usuário autorizou continuar a Change 002. Operações ainda não executadas: alteração DNS, verificação de posse, convite de usuários, submissão de sitemap, ligação ao Analytics. Nenhum contrato/assinatura pago solicitado. Não houve commit, push ou deploy. O TXT exibido não é senha; o valor exato permanece no diálogo do Google, evitando duplicação desnecessária nos registros do projeto.

Pontos de continuação: aba Chrome Search Console com diálogo TXT e Safari Advanced DNS de lafmat.com. Não é necessário autenticar novamente no Chrome Namecheap. Relatórios históricos ainda NOT_CHECKED, nunca zero presumido. Não usar Change of Address para esta mudança de hospedagem/caminhos no mesmo domínio.

## Editor aberto pelo usuário

O usuário confirmou abertura de Add New Record no Safari. Screenshot mostrou linha nova ainda no tipo A Record, campos vazios e seletor de tipo aberto. O controle nativo do Safari deixou de expor o conteúdo web na árvore AX durante a edição; teclado e foco não produziram mudança verificável. Não foi preenchido nem salvo nenhum valor. Valor TXT continua conferido no diálogo Google. Solicitada confirmação explícita da conta Google destinatária no momento da concessão de posse, conforme política do navegador. A continuação depende de preenchimento manual desta linha ou sessão autenticada em navegador controlável; não declarar TXT aplicado até prova DNS/UI.

## Autorização da conta — 24/11/2026

Usuário respondeu explicitamente "Sim, confirmar essa conta" à pergunta sobre vincular lafmat.com à conta Google mario.reis.junior@gmail.com e conceder condição de proprietário verificado no Search Console. Não repetir essa confirmação para a mesma operação/conta. A autorização não comprova aplicação do TXT.

Na retomada, a Namecheap ainda mostrava a nova linha vazia no tipo A Record; não havia TXT Google salvo na tabela. Durante tentativa de selecionar TXT, o navegador sinalizou intervenção do usuário e troca de aba. A ação foi interrompida sem salvar. Solicitado deixar a aba Advanced DNS estável para continuar. Não inspecionar ou registrar conteúdo de outras abas pessoais. A consulta ao servidor autoritativo por nome falhou por resolução local; isso não demonstra ausência de registro. Nenhuma alteração foi aplicada neste turno até esse checkpoint.

## Sessão expirada no salvamento — 24/11/2026

Após usuário liberar controle exclusivo, o tipo TXT foi selecionado e os campos @ e valor Google foram preenchidos e lidos corretamente. Clique AX na célula que agrega Save/Cancel descartou o primeiro rascunho sem criar registro; reaberta uma única linha, preenchida novamente e acionada a marca de salvar por coordenada exata do screenshot. A Namecheap retornou "Failed to save record. Please try again.". Não repetir sem corrigir a causa. Ao recarregar para renovar o estado, o servidor redirecionou ao login, comprovando sessão expirada. Nenhum TXT Google apareceu na tabela ou nas consultas públicas Cloudflare/Google feitas após a tentativa. Demais registros observados preservados.

Usuário solicitado a autenticar novamente a aba Safari. A autorização da conta Google já foi concedida; não pedir de novo. Após login, abrir painel fresco, conferir se TXT existe antes de adicionar, preencher uma única linha se ausente, salvar e confirmar no DNS antes de Verify. Coordenadas do screenshot são em pixels completos (não dividir por Retina); células AX com Save/Cancel não devem ser clicadas no centro. Esta execução segue PARTIAL, não concluída. Não houve deploy ou mudança no site.


## Resultado final — 24/11/2026

Propriedade de domínio **sc-domain:lafmat.com** verificada com sucesso via DNS TXT, após renovar a sessão expirada da Namecheap. O Google exibiu Ownership verified; Settings confirmou You are a verified owner. Users and permissions listou exatamente um usuário: Mario Reis, na conta autorizada pelo usuário, como Owner / Verified. Nenhum outro usuário foi adicionado ou removido.

Foi adicionado somente TXT @ de verificação, TTL Automatic; A de produção, www CNAME e nameservers preservados e conferidos em DNS público. O TXT deve permanecer para manter a posse. Não apagar como limpeza de migração. Manter administração futura por convites deliberados, não compartilhamento de senha.

Relatórios disponíveis consultados:

- Performance e Pages: Processing data, please check again in a day or so. Não interpretar No data como zero cliques ou zero páginas indexadas. Sem exportação histórica utilizável neste momento.
- Sitemaps: zero entradas cadastradas nessa propriedade. Nenhum sitemap enviado neste Change.
- Manual actions e Security issues: No issues detected em ambos.
- Settings: sem robots.txt, crawl stats ainda sem dados, propriedade adicionada à conta em 24/11/2026 e associação a serviço não configurada.
- HTTPS: atualização 23/11/2026, 14 URLs HTTPS e 1 URL classificada como HTTPS not evaluated, validação Not Started. URL específica ainda não obtida; conferir no Change 004/006. Isso não prova certificado inválido atual, e o HTTPS/manifesto público passou em validação normal.

Baseline estruturada em search-console-baseline-2026-11-24.json; prova DNS/web em search-console-dns-2026-11-24.json. Screenshot da conta com Owner Verified salvo na pasta de visualizações do projeto. A tentativa de exportação CSV do relatório HTTPS pelo navegador não retornou arquivo; sessão de controle reiniciou. Não se afirma que CSV foi baixado. Valores observados foram registrados no recibo JSON, sem métricas inventadas. Exportações de desempenho/indexação ficam pendentes de o Google concluir processamento e serão retomadas no acompanhamento, sem impedir a preparação local do Change 003.

Não usada a ferramenta Change of Address, não instalada tag GA4 e não feitas mudanças no WordPress/conferência de 2023. Arquivos de produção permanecem no manifesto LAFMAT-20261123-BCB04519421A. Nenhum commit/push/deploy neste turno. Próxima Change: 003-indexable-static-routes; submissão do sitemap só após geração e publicação das rotas finais.

## Change 006 — 24/11/2026

Sitemap https://lafmat.com/sitemap.xml submetido à propriedade sc-domain:lafmat.com e processado com sucesso; 57 páginas descobertas, leitura em 24/11/2026. Associação ao GA4 565753617 e fluxo LAFMAT website 16408359562 concluída após confirmação do usuário. Coleção Search Console já publicada no Analytics, Queries disponível mas sem dados processados.

Inspeções ao vivo e pedidos prioritários em docs/seo/google-validation-2026-11-24.json. O relatório indexado inicialmente ainda não contém as novas páginas: descoberta e fila de rastreamento não equivalem a indexação concluída. A página inicial foi renderizada corretamente pelo Google Inspection Tool smartphone, inclusive identidade visual e conteúdo principal. Não realizar Change of Address ou Indexing API para estas páginas comuns.
