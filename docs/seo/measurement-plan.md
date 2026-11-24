# Change 005 — plano de medição e privacidade

Estado em 24/11/2026: serviço GA4 criado/configurado e candidato local preparado com G-R5KQ774N5V; ainda não publicado. Produção continua no release SEO 003+004, manifesto LAFMAT-20261124-20C36699ED23. Ingestão real e comportamento de rede aguardam ativação autorizada e teste pós-release.

## Conta e fluxo confirmados

Responsável autorizado: mario.reis.junior@gmail.com. Usuário também autorizou explicitamente os termos de serviço para Brasil/processamento. Conta LAFMAT 417343930, propriedade LAFMAT — lafmat.com 565753617, fluxo web 16408359562 em https://lafmat.com, measurement ID G-R5KQ774N5V. IDs conferidos na UI, sem copiar configurações de outros projetos. Fuso São Paulo, BRL, categoria Science, objetivos tráfego/engajamento. Porte obrigatório Small 1–10 como aproximação da equipe mantenedora, não censo de membros. Compartilhamentos opcionais desmarcados. Nenhuma chave de Measurement Protocol criada.

## Coleta mínima aprovada

Basic opt-in: antes de aceitar, não carregar Google tag nem enviar eventos Analytics. Recusar não carrega tag; rever decisão no rodapé sempre disponível. Retirar consentimento desabilita eventos, remove cookies _ga acessíveis e recarrega para descarregar o runtime; a escolha se propaga entre abas. Não desfaz dados previamente consentidos. Preferência local e cookies configurados para até 180 dias. Retenção de eventos e usuários salva/conferida em 2 meses no GA4, reset por atividade off. O Google informa efeito das alterações após 24h; relatórios agregados seguem regras próprias.

Publicidade: ad_storage, ad_user_data e ad_personalization negados no código. Signals e dados fornecidos pelo usuário não ativados; localização/dispositivo granular off; personalização de anúncios permitida em 0 de 307 regiões. Sem User-ID enviado, remarketing ou ligação Ads/outra propriedade. Filtro Internal Traffic em Testing, sem exclusão permanente ativa. Dimensões de evento app_surface, app_language e app_action_category registradas. Recibo: analytics-service-validation-2026-11-24.json.

## Eventos e significado

| Evento | Significado | Categorias |
|---|---|---|
| page_view | Uma página/idioma canônico visto após consentimento | app_surface e app_language |
| video_outbound_click | Clique de saída para canal/gravação, não reprodução | network, gimatefun, recording, channel |
| file_download_click | Clique em PDF/ZIP, não conclusão do download | pdf, zip |
| contact_click | Clique em link de email/telefone, não envio | email, phone |
| contact_draft_open | Formulário abre rascunho mailto, sem enviar conteúdo ao GA | email |
| outbound_click | Saída para redes/Scholar/outros destinos, sem URL completa | facebook, scholar, other |
| conference_archive_open | Abertura do arquivo histórico | 2023 |

Registrar no GA4 apenas dimensões de evento de baixa cardinalidade: app_surface, app_language, app_action_category. Não registrar títulos, emails, buscas, nomes, telefone, mensagem, IDs de pessoas ou URL de clique. Não marcar cliques/rascunhos como key events/conversão de envio; o site não comprova email enviado ou vídeo reproduzido.

Um page_view por rota/idioma; âncoras/queries não criam page_view adicional. `send_page_view:false` na tag e Enhanced Measurement desativado no fluxo (incluindo histórico, formulário, buscas, vídeos, outbound e downloads), para impedir duplicação e captura automática de campos/queries. Enhanced Measurement foi desativado e o estado off conferido nos detalhes do fluxo.

## Dados enviados e limites de atribuição

Endereços de páginas são reconstruídos exclusivamente a partir das rotas conhecidas em https://lafmat.com, sem query, hash, credenciais ou endereço arbitrário. Título vem dos rótulos públicos fixos; campos de formulários não entram no rastreador. Referrer interno somente para rotas conhecidas; externo limitado a origens de busca/plataformas conhecidas e sem caminho/query. UTMs arbitrários e origens privadas não são encaminhados. Isso reduz detalhe de atribuição e não é uma solução de campanhas pagas. Google ainda processa dados técnicos e identificadores pseudônimos conforme consentimento; não chamar coleta de anônima.

O parâmetro de QA `lafmat_analytics_test=1` ativa debug_mode e traffic_type=internal; não é encaminhado na page_location. Filtros devem começar em Testing, nunca em exclusão ativa sem evidência e decisão específica. Não coletar IP pessoal para criar regra interna por suposição. DebugView/Realtime e payload real ainda pendentes.

## Site e arquivo

Três páginas de privacidade novas: /privacy/, /pt/privacy/, /es/privacy/. Total derivado passa a 45 páginas e sitemap a 57. Menu principal permanece nas sete seções, política no rodapé. No arquivo 2023, apenas HEAD de 12 canônicos recebe CSS e seis scripts locais necessários; texto, tabelas, mídias e aliases não são alterados. Script URLs estáveis evitam mudanças recorrentes no arquivo ao sincronizar vídeos. Verificador de paridade foi ampliado para permitir somente esses scripts defer no HEAD e continua rejeitando scripts arbitrários/formulários.

Players YouTube incorporados antigos têm comportamento e política próprios; a preferência controla Analytics, não esses players. Isso está divulgado na política, sem reescrever o conteúdo histórico. Páginas 404/endereços desconhecidos não são medidos para evitar captura de caminhos livres/PII.

## Validação já feita e pendente

PASS local: unit tests com transporte simulado (sem rede Google), aceite/recusa/revogação, propagação entre abas, cookies funcionais preservados, URLs/referrers sanitizados, uma contagem, eventos limitados, rascunho sem campos. HTML/SEO 45/57, galeria 306/273, oito testes sync, paridade de 22 arquivos de conferência e dez assets preservados. Navegador local: recusa persiste após reload, revisão por teclado, política PT/ES, mobile 390 sem overflow, zero elemento Google tag antes/na recusa. O teste local não carrega Google porque o hostname não é o canônico; ele não comprova ingestão no GA4.

Faltam: revisão do candidato exato e publicação autorizada; payload real/DebugView/Realtime, duplicação e revogação na versão publicada. Não marcar Change concluída apenas pelo código/serviço.

## Referências primárias consultadas em 24/11/2026

- https://developers.google.com/tag-platform/security/concepts/consent-mode
- https://developers.google.com/analytics/devguides/collection/ga4/views
- https://developers.google.com/analytics/devguides/collection/ga4/single-page-applications
- https://developers.google.com/analytics/devguides/collection/ga4/reference/config
- https://support.google.com/analytics/answer/13296761
- https://support.google.com/analytics/answer/9267744

Plano técnico, sem declaração de conformidade legal universal ou garantia de indexação.
