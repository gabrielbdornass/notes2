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

??? note "Mudando mensagem de um commit vazio `--allow-empty` "
    Ao tentar modificar a mensagem de um commit vazio recebi o seguinte erro:

    ```
    (notes-py3.13) ➜  notes git:(main) git rebase -i HEAD~4
    interactive rebase in progress; onto 8733d2a
    Last command done (1 command done):
      reword 476c93b 447-start # empty
    Next commands to do (3 remaining commands):
      pick 02c43ee Try fix git-commiters error message
      pick 41935e1 Update poetry packages
      (use "git rebase --edit-todo" to view and edit)
    You are currently editing a commit while rebasing branch 'main' on '8733d2a'.

    No changes
    You asked to amend the most recent commit, but doing so would make
    it empty. You can repeat your command with --allow-empty, or you can
    remove the commit entirely with "git reset HEAD^".
    You can amend the commit now, with

      git commit --amend

    Once you are satisfied with your changes, run

      git rebase --continue
    ```

    Para solucioná-lo:

    ```
    # para abrir
    git commit --allow-empty --amend

    # Após modificar a mensagem
    git rebase --continue
    ```

    **O erro aconteceu, principalmente, pois estava testando a metodologia [start-stop](./20250315_metodologia_start_stop.md)**.


!!! Warning

    [Cuidado ao modificar commits já enviados para GitHub](./20250317_cuidado_ao_modificar_commits_ja_enviados_para_github.md), pois será necessário realizar `pull/push` com a flag `--force`.

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
