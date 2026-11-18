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

## Execução confirmada

- Nameservers alterados para dns1.registrar-servers.com e dns2.registrar-servers.com. A operação em lote inicial não provisionou a zona; a troca foi concluída no controle direto e os registros foram gravados no editor Advanced DNS.
- Os oito registros preparados foram conferidos após recarregar e expandir “Show More”: quatro A de @, CNAME de www e A de cpanel/webmail/ftp. TTL de 300 segundos. Nenhum URL Redirect de estacionamento permaneceu.
- Mail Settings definido como No Email Service, conforme confirmação de ausência de contas e encaminhamentos.
- GitHub Pages configurado com cname lafmat.com. Fonte 2eca68c; publicação 5c6d8c2ebfc24ee576ea183a35438d86dfec385d. Build 44410633742: success.
- Novos servidores autoritativos e resolvedores 1.1.1.1/8.8.8.8 conferidos. Snapshot posterior em dns-after-migration-2026-11-18.json.
- Nove arquivos de produção conferidos pelo domínio, diretamente no IP do GitHub por HTTP, com hashes iguais aos locais: entrada, aliases antigos, arquivo de 2023, PDF, ZIP e JavaScript. O CNAME foi conferido na árvore Git publicada; é metadado de hospedagem, não um download servido pelo Pages. Evidências em domain-http-validation-2026-11-18.json.
- Manifesto LAFMAT-20261118-F6344655EC91, SHA-256 f6344655ec910f9b11002b23c54fe5870e88dd37fee4e6bcf1b9a3d3fa4022e7.

## Pendência externa

Na conferência posterior à troca, o diagnóstico DNS do GitHub ainda retornava a resolução antiga e nenhum certificado emitido. HTTPS obrigatório ainda não pode ser ativado. Uma tentativa de TLS diretamente no GitHub confirmou certificado sem lafmat.com; a verificação de TLS não foi desativada. A resolução local também manteve o IP antigo em cache, embora os dois resolvedores públicos já apresentassem os quatro IPs novos.

Estado: DNS_APPLIED_HTTPS_PENDING. Não considerar a migração integralmente concluída até o certificado cobrir lafmat.com e www.lafmat.com, HTTPS obrigatório estar ativo e as duas URLs públicas passarem nos testes normais. Não solicitar nova autorização para concluir essa etapa já autorizada; consultar o estado e ativar HTTPS assim que disponível. Não cancelar a hospedagem antiga nem a renovação do domínio.


## Nova tentativa de finalização de HTTPS — 18/11/2026

A pedido do usuário, a configuração do domínio foi reaplicada e depois removida/reinserida uma vez, conforme o procedimento oficial de solução de problemas de HTTPS do GitHub. O CNAME foi restaurado à formatação exata do manifesto validado, sem mudar o conteúdo do site. A publicação resultante é 372167a36e14b472278609383e1dbf5ca691dc23; build/deploy 44414783704 concluído com sucesso. Um build intermediário obsoleto foi cancelado para liberar a fila.

A tentativa explícita de ativar https_enforced=true foi recusada pelo GitHub com HTTP 404 e “The certificate does not exist yet”. Após a nova publicação, https_certificate continua null e https_enforced=false. DNS público e os dois servidores oficiais permanecem corretos, mas a validação do GitHub ainda retornou a resolução antiga. A verificação TLS não foi desativada. Estado continua HTTPS_PENDING_PROVIDER; não anunciar conclusão integral. Evidência estruturada em https-activation-attempt-2026-11-18.json.

## Verificação integral e rota histórica

A verificação HTTP dos 281 arquivos públicos detectou que `/home/__trashed/index.html` não era servido por causa do processamento padrão Jekyll. Adicionado `dist/.nojekyll` para publicar o conteúdo estático sem excluir diretórios com sublinhado. Manifesto atualizado: `LAFMAT-20261118-6D2C6003288B`. As 22 páginas de arquivo/rotas da conferência passaram novamente na verificação local. A emissão HTTPS continua pendente e é acompanhada nesta execução.
