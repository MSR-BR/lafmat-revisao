# Estado e decisões — 24/11/2026

PUBLICATION_STATE: PUBLISHED_VALIDATED
GOOGLE_ACCOUNT_STATE: conta/propriedade criadas; termos e configuração mínima autorizados
GA4_ACCOUNT_ID: 417343930
GA4_PROPERTY_ID: 565753617
GA4_STREAM_ID: 16408359562
GA4_MEASUREMENT_ID: G-R5KQ774N5V
COLLECTION_ENABLED: true em HTTPS lafmat.com, após consentimento

Formulário preparado no Chrome nativo (browser connector Chrome indisponível); perfil Mario e conta pretendida conferidos na UI, não há criação concluída. Usuário confirmou mario.reis.junior@gmail.com e coleta após aceite, recusa/revisão, retenção de 2 meses, sem anúncios/Signals/User-ID/campos de contato/buscas livres. Compartilhamentos opcionais desmarcados no rascunho. Create abriu o diálogo Google Analytics Terms of Service Agreement; região Brazil selecionada, checkbox dos termos de processamento desmarcado e I Accept ainda não acionado. Confirmação específica solicitada ao usuário para esse aceite legal; não tratar aprovação técnica como aceite de termos.

O rascunho de política descreve configurações pretendidas (2 meses etc.) e só pode ser publicado após aplicação/prova real. Origem/IDs de outros projetos não foram usados/copied para LAFMAT. Três rotas de privacidade geradas; coleta mínima com basic opt-in, preferência revisável e payloads limitados. Instrumentação histórica apenas HEAD, sem reescrever conteúdo; não há alteração de aliases nem WordPress.

Rollback futuro: desativar tag, preservar propriedade/histórico; reverter integração sem apagar conteúdo ou dados posteriores. Coleta já realizada não se desfaz por revert. Produção ainda é manifesto 20C36699ED23 / código d45f880 + documentação 067a5de.

## Serviço configurado e conferido na UI

Usuário autorizou especificamente os termos para Brasil/processamento. Na retomada, o assistente já mostrava Account/Property creation Completed; não houve novo aceite duplicado. Conta LAFMAT e propriedade LAFMAT — lafmat.com verificadas no seletor, responsável Mario Reis confirmado na UI. Fuso São Paulo e BRL; Science; porte obrigatório Small 1–10 usado como aproximação da equipe mantenedora, não cadastro de membros. Fluxo https://lafmat.com, Enhanced Measurement off, zero connected site tags. Nenhuma API secret criada.

Retenção de eventos e usuários: 2 meses; reset por atividade off; sucesso salvo e reabertura conferida. Signals e user-provided data não ativados; localização/dispositivo granular off; anúncios permitidos em 0/307 regiões. Quatro compartilhamentos opcionais da conta desmarcados. Filtro Internal Traffic existente em Testing, nenhuma exclusão ativa criada. Dimensões de evento cadastradas: app_surface, app_language, app_action_category. Sem ligação a Ads ou outra propriedade.

Chrome connector ficou disponível durante a execução. Aba dedicada LAFMAT criada; aba pertencente a outra sessão não foi tomada. A integração pública usa somente o measurement ID deste fluxo, não o snippet GTM sugerido pelo assistente. Falta candidato exato/revisão/autorização de publicação e prova real de ingestão/negação/revogação após publicação.

## Conclusão / checkpoint de entrega

Publicação exata 5c69d78 autorizada pelo usuário, push main concluído. Manifesto LAFMAT-20261124-9CB50AF756EB / 649 arquivos. Implantação evdur21w5 READY e promovida. Teste revelou page_view automático da nova inicialização Google; houve dois rollbacks imediatos conforme autorização (segundo teste usou tag antiga em cache). Correção publicada no próprio container GTM-558VTRFD versão2: bloqueio de pageview automático, flags/cookies mínimos e rótulos fixos seguros na inicialização. Artefato público atualizado conferido, cache desativado no teste e mesmo commit re-promovido.

PASS real: uma page_view204 limpa, parâmetros no DebugView e clique video_outbound_click categoria network, ES/privacy e videos recebidos; recusa persiste, retirada/reload e outra página sem tag, zero collect após retirada. Busca na galeria não gerou evento de busca. Não afirmar que histórico de testes foi apagado; não houve exclusão. 45 páginas +6artefatos bytes exatos,308 esperados e404 normal. urllib não seguiu308 automaticamente; checagem retomada somente para destinos/final404, sem repetir lote.

Rotina diária atualizada com test_analytics.cjs; ACTIVE,09h,failed_runs_only preservados. Sem mutações de conta Google pela rotina. Próxima Change006 depende de nova solicitação. Checkpoints históricos acima descrevem preparação, não estado atual.
