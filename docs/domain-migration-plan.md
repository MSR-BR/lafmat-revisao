# lafmat.com — preparação, sem alteração de DNS

Consulta pública em 18/11/2026:

| Registro | Valor observado |
| --- | --- |
| NS | ns4928.banahosting.com; ns4929.banahosting.com |
| A do domínio | 66.225.201.137 |
| CNAME de www | lafmat.com |
| MX | prioridade 0, lafmat.com |
| mail.lafmat.com | CNAME para lafmat.com |
| SPF | Usa `a`, `mx`, um IP explícito e relay.mailchannels.net |
| AAAA do domínio | Nenhuma resposta observada |

Isso confirma que os servidores DNS publicados pertencem à BanaHosting. Não confirma a conta de hospedagem, o titular registral ou a existência de caixas de e-mail.

## Dependência de e-mail antes da troca

O MX e o nome `mail` acompanham o endereço do site. Se apenas o A do domínio for trocado, esses destinos passarão a resolver para o GitHub Pages, que não recebe correio. Preservar o texto atual do MX é insuficiente. O SPF também utiliza `a` e `mx`.

Confirmar com o administrador se há caixas, encaminhamentos ou clientes de e-mail em uso. Se houver, obter o destino correto do servidor de correio e configurar seus registros independentes do domínio principal, com o administrador do provedor. Revisar MX, mail, SPF, DKIM, DMARC e autoconfiguração, sem presumir que o IP observado é o destino correto para todos esses serviços. Testar envio/recebimento antes e depois. Não cancelar hospedagem durante essa etapa.

## Sequência a executar depois da revisão do arquivo

1. Publicar e conferir o arquivo da conferência no GitHub Pages, incluindo `/home/program/` e as outras dez URLs antigas.
2. Exportar a zona DNS atual com o administrador e confirmar plano de e-mail e rollback.
3. Verificar o domínio na conta GitHub MSR-BR por TXT e configurar `lafmat.com` em Settings → Pages na janela combinada de troca. Manter o TXT de verificação.
4. Só então aplicar no DNS os quatro A de `@` para o GitHub Pages e CNAME `www` → `msr-br.github.io`, preservando os demais registros conforme o plano de e-mail. Conferir/remover apenas apontamentos web conflitantes. Não trocar nameservers sem necessidade.
5. Guardar `lafmat.com` em `dist/CNAME` para futuras publicações. Ainda não criado: ativá-lo agora anteciparia a mudança do endereço público.
6. Conferir DNS, certificado HTTPS, domínio raiz, www, navegação, arquivo de 2023, PDFs/ZIP e funcionamento dos e-mails. Ativar HTTPS obrigatório quando o certificado estiver disponível.

Valores documentados pelo GitHub em 18/11/2026 para o passo 4:

| Tipo | Nome | Valor |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | msr-br.github.io |

Fonte: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

Rollback de DNS: reaplicar os apontamentos web anteriores, conferir o plano de e-mail e remover o domínio personalizado do Pages quando necessário. Manter a hospedagem antiga até a validação da troca.

Nenhuma alteração de domínio, DNS, e-mail ou hospedagem foi executada nesta preparação.

## Atualização de execução — 18/11/2026

Este documento foi o plano anterior à troca. A migração foi autorizada e os apontamentos DNS já foram aplicados na Namecheap após o usuário confirmar ausência de e-mail e encaminhamentos. A conclusão técnica e o rollback estão em `domain-cutover-2026-11-18.md`; snapshots anterior/posterior e validação HTTP estão no mesmo diretório. A emissão do certificado e a ativação de HTTPS obrigatório ainda estão pendentes na última conferência. As afirmações de “nenhuma alteração executada” acima descrevem a preparação inicial, não o estado atual.
