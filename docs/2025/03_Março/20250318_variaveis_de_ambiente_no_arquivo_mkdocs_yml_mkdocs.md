---
tags:
  - Material-Mkdocs
---

# Variáveis de ambiente no arquivo mkdocs.yml - mkdocs

Durante a correção [deste Issue](https://github.com/gabrielbdornas/notes/issues/447) descobri que é possível incluir a flag `enabled: !ENV [CI, false]` no plugin [mkdocs-git-committers-plugin-2](https://github.com/ojacques/mkdocs-git-committers-plugin-2).

Isso se mostrou bastante útil, principalmente para o ambiente local, uma vez que o plugin faz a busca dos autores de todos os documentos. (1)
{ .annotate }

1. :man_raising_hand: No longo prazo isso poderia levar a uma demora execessiva para ligar o servidor de desenvolvimento.

A [documentação mkdocs](https://www.mkdocs.org/user-guide/configuration/#environment-variables) mostra como passar essas variáveis de ambiente para o arquivo `mdkdocs.yaml`:

```
# Devendo SITE_NAME ser definido no .env ou como variável de ambiente
site_name: !ENV SITE_NAME

# Sendo SITE_NAME definido no próprio arquivo mkdocs.yml`
site_name: !ENV [SITE_NAME, 'My default site name']
```

No caso da construção deste repositório de notas, preferi incluir o valor da variável `ALLOW_GIT_COMMITTERS_BUILD`[^1]:

  - Ambiente de desenvolvimento: no arquivo `.env`.
  - Produção: Variável de ambiente (GitHub actions secret).

```
# mkdocs.yml
- git-committers:
    repository: gabrielbdornas/notes
    branch: main
    enabled: !ENV ALLOW_GIT_COMMITTERS_BUILD
    token: !ENV ['GH_TOKEN']
```


## Outras referências

[^1]: [Permalink](https://github.com/gabrielbdornas/notes/blob/acd1fa98ae6ad7487673694399476660e99b3d2e/mkdocs.yml#L15-L19).
