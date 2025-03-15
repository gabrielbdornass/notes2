---
tags:
  - git
  - github
---

# Como inverter a ordem de commits

A nota [Como modificar a mensagem de um commit](./20250314_como_modificar_mensagem_commit.md) mostra como usar o comando `rebase` no modo interativo `-i`, mais especificamente para mudar a mensagem de commits.

A lógica para inverter a ordem de um commit é a mesma.

```
// n is the number of commits up to the last commit you want to be able to edit
git rebase -i HEAD~n
```

Será aberta uma lista com os `n` commits desejados.
Basta inverter a ordem dos commits no arquivo aberto, salvar e fechar.

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
- [chatGPT](https://chatgpt.com/c/67d5ed24-7a94-8003-b360-b11219c99a64).
