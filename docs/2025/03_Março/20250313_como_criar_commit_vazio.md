---
tags:
  - Git
---

# Como criar um commit vazio

[Este post](https://graphite.dev/guides/empty-commit) mostrou que basta usar a flag `--allow-empty` no comando `commit`:

```
git commit --allow-empty -m "Your commit message"
```

Se deseja escrever uma mensagem de commit mais longa, basta retirar a flag `-m`.
Isso abrirá um arquivo para inserção da mensagem do commit no seu editor padrão.

```
git commit --allow-empty
```

## Outras referências

- [Como criar branch vazia](./20250311_como_criar_branch_vazia.md): Mostra como criar branch vazia e realizar o primeiro commit, também vazio, para marcar o início do trabalho.
