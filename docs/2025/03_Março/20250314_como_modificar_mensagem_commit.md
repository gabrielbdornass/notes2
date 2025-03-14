---
tags:
  - git
  - github
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

??? warning "Atenção para commits já enviados para o GitHub:"

    Será necessário realizar `pull/push` com a flag `--force`.
    Lembre-se que isso é especialmente perigoso quando estamos trabalhando em equipe.
    Alguém que tenha realizado um `pull` antes do seu `--force` terá um conflito com o novo código, pois seu histórico de commits ficará diferente do histórico do repositório.

    **Nunca realize um `--force` sem antes conversar com os colegas e entender as implicações desta ação.**

    > If you've already pushed your commit up to your remote branch, then, after amending your commit locally, you'll also need to force push the commit with:
    >
    >```
    >git push <remote> <branch> --force
    ># Or
    >git push <remote> <branch> -f
    >```

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
