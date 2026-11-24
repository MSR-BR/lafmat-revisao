# Requisitos

- Implementar redirects HTTP 301/308 na Vercel, não apenas meta refresh/JavaScript; preservar significado.
- Definir canonical, hreflang recíproco e x-default quando aplicável; título/descrição específicos.
- Criar robots.txt e sitemap.xml somente com URLs canônicas indexáveis e lastmod significativo.
- Adicionar Open Graph e imagem de compartilhamento com origem conhecida; JSON-LD Organization e Event somente quando elegível e factual.
- Manter 404 real para URL inexistente; usar 410 apenas para remoção deliberada sem substituto.
- Não enviar todas as URLs antigas à home, nem colocar hashes/redirects/noindex no sitemap.
- Garantir canonical de host HTTPS e não indexação de previews. Sem cancelamento de hospedagem ou alteração de DNS web.

Fora de escopo: trocar domínio/hospedagem, campanhas pagas e alterações editoriais não solicitadas.
