---
tags:
  - Git
---

# Como criar uma branch vazia

[Esta resposta stackoverflow](https://stackoverflow.com/a/34100189/11755155) mostrou que basta usar a flag `--orphan` no comando `switch`:

```
git switch --orphan <new branch>
```

Se deseja enviar esta branch para o GitHub será necessário ter, ao menos, um commit:

```
git switch --orphan <new branch>
git commit --allow-empty -m "Initial commit on orphan branch"
git push -u origin <new branch>
```

## Outras referências

- [Creating Orphan branches in Git](https://medium.com/@salmankhan_27014/creating-orphan-branches-in-git-853eb8f7c9c6): Mostra a utilização da flag `--orphan` no comando `checkout` e `git rm -rf .` para limpar o conteúdo da nova branch.
- [Why use 'git rm' to remove a file instead of 'rm'?](https://stackoverflow.com/questions/7434449/why-use-git-rm-to-remove-a-file-instead-of-rm): If you just use rm, you will need to follow it up with `git add <fileRemoved>`. `git rm` does this in one step. You can also use `git rm --cached` which will remove the file from the index (staging it for deletion on the next commit), but keep your copy in the local file system.

