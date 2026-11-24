# Superfícies concretas — preparação local

- Novos: dist/assets/analytics-config.js, analytics-core.js, analytics.js, analytics.css, privacy.js; scripts/test_analytics.cjs; docs/seo/measurement-plan.md e analytics-local-validation-2026-11-24.json.
- Alterados: routes.js, i18n.js (rótulo Privacy), site-render.js, site.js (eventos sem dados de formulário), seo.js, templates/site.html e scripts/build_site.cjs.
- 45 HTML gerados, três rotas de privacidade, sitemap/recibo/manifesto; 12 HEADs canônicos de conferência somente com scripts/CSS locais, sem editar conteúdo. Verificador verify_conference.py permite apenas scripts defer conhecidos no HEAD; paridade preservada.
- Nenhuma dependência nova ou Measurement Protocol secret.
- Medição mantém enabled=false/ID vazio. Sem conta Google criada ou configuração de outra propriedade alterada. Rascunho nativo Google aberto, aguardando confirmação para continuar.

Operações externas futuras: criar/configurar conta e fluxo LAFMAT após confirmação e eventual aceite de termos no momento; publicar tag/privacidade só após validação e revisão exatas. Google account/choices não se inferem de ID de outro projeto.
