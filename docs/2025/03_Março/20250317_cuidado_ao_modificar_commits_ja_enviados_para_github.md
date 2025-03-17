---
tags:
  - git
  - github
---

# Cuidado ao modificar commits já enviados para GitHub

:material-alert: Cuidado ao modificar commits já enviados para GitHub

Será necessário realizar `pull/push` com a flag `--force`.
Lembre-se que isso é especialmente perigoso quando estamos trabalhando em equipe.
Alguém que tenha realizado um `pull` antes do seu `--force` terá um conflito com o novo código, pois o histórico de commits de sua máquina ficará diferente do histórico do repositório.

**Nunca realize um `--force` sem antes conversar com os colegas e entender as implicações desta ação[^1]:**

> If you've already pushed your commit up to your remote branch, then, after amending your commit locally, you'll also need to force push the commit with:
>
>```
>git push <remote> <branch> --force
># Or
>git push <remote> <branch> -f
>```

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
- [Como modificar a mensagem de um commit](./20250314_como_modificar_mensagem_commit.md).
- [Como inverter a ordem de commits](./20250315_como_inverter_a_ordem_de_commits.md).
- [git rebase com o primeiro commit](./20250315_git_rebase_com_o_primeiro_commit.md).
- [Como mudar datetime de um commit](./20250317_como_mudar_datetime_de_um_commit.md).

[^1]: [Changing the message of a commit that you've already pushed to your remote branch](https://stackoverflow.com/questions/179123/how-to-modify-existing-unpushed-commit-messages/179147#179147:~:text=not%20get%20committed.\)-,Changing,-the%20message%20of).
