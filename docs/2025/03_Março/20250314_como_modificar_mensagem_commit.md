---
tags:
  - Git
  - GitHub
---

# Como modificar a mensagem de um commit

[Esta resposta Stackoverflow](https://stackoverflow.com/a/179147/11755155) me mostrou que devo usar o comando `rebase` no modo interativo `-i`:

```
// n is the number of commits up to the last commit you want to be able to edit
git rebase -i HEAD~n
```

Será aberta uma lista com os `n` commits desejados.
Basta trocar `pick` por `r`.
Ao fechar o arquivo, todos os commits selecionados para troca da mensagem serão abertos, um após o outro, em seu editor de preferência.

!!! Warning

    [Cuidado ao modificar commits já enviados para GitHub](./20250317_cuidado_ao_modificar_commits_ja_enviados_para_github.md), pois será necessário realizar `pull/push` com a flag `--force`.

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
