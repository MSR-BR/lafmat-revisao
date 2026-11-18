# Migração de lafmat.com — 18/11/2026

Autorização: usuário autorizou conduzir a migração e confirmou explicitamente que não há caixas de e-mail nem encaminhamentos @lafmat.com em uso.

Destino: site existente no GitHub Pages, repositório MSR-BR/lafmat-revisao, domínio canônico lafmat.com. DNS de destino: Namecheap BasicDNS na conta atualmente acessível, darkger. Esta operação não transfere a titularidade do domínio nem cria uma conta pessoal nova.

Snapshot anterior: dns-before-migration-2026-11-18.json. É um levantamento público dos registros conhecidos, não uma exportação integral da zona. DNSSEC: nenhuma delegação DS observada. Nameservers anteriores: ns4928.banahosting.com e ns4929.banahosting.com; IP web anterior 66.225.201.137. Hospedagem antiga e renovação do domínio serão mantidas.

Zona preparada em uma única operação DNS/Host Records, somente lafmat.com, TTL 300:
- @ A 185.199.108.153
- @ A 185.199.109.153
- @ A 185.199.110.153
- @ A 185.199.111.153
- www CNAME msr-br.github.io
- cpanel A 66.225.201.137
- webmail A 66.225.201.137
- ftp A 66.225.201.137

Não há serviço de e-mail a migrar conforme confirmação do usuário. Os registros históricos de e-mail estão guardados no snapshot; não se declara preservação de caixas ou encaminhamentos que não existem no escopo confirmado.

Publicação preparada com dist/CNAME e oito rotas antigas de navegação, além das 11 rotas completas da conferência. Testes locais: 282 arquivos no manifesto, igualdade de texto e links do arquivo 2023, JavaScript e diff sem erros. Verificação de segurança do diff: PASS. Destino de publicação: raiz da branch gh-pages.

Rollback: restaurar os dois nameservers da BanaHosting e, conforme o estado, remover o domínio personalizado do Pages e republicar a árvore de 5fcff81662a12e00062edafa99e1d6164eade2ca. Não apagar a história Git. Aguardar caches DNS antes de concluir falha ou sucesso global.

Estado deste registro: candidato preparado; conclusão e evidências serão acrescentadas depois da execução.
