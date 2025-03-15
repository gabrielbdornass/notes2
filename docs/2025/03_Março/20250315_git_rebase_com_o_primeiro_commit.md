---
tags:
  - git
---
# git rebase com o primeiro commit

A nota [Como modificar a mensagem de um commit](./20250314_como_modificar_mensagem_commit.md) mostra como usar o comando `rebase` no modo interativo `-i`.
Em um repositório com apenas 2 commits utilizei o comando `git rebase -i HEAD~2` (1) para modificar o primeiro commit, mas recebi o erro `fatal: invalid upstream 'HEAD~2'`.
{ .annotate }

1.  :man_raising_hand: O comando `git rebase -i HEAD~2` inicia o rebase, no mode iterativo, a partir do "pai" dos dois últimos commits.

Neste caso, a flag `--root` deveria ter sido utilizada no lugar de `HEAD~2`:

```
git rebase -i --root
```

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
- [chatGPT](https://chatgpt.com/c/67d5ed24-7a94-8003-b360-b11219c99a64).
