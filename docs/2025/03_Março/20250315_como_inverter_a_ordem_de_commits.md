---
tags:
  - Git
  - GitHub
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

!!! Warning

    [Cuidado ao modificar commits já enviados para GitHub](./20250317_cuidado_ao_modificar_commits_ja_enviados_para_github.md), pois será necessário realizar `pull/push` com a flag `--force`.

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
- [chatGPT](https://chatgpt.com/c/67d5ed24-7a94-8003-b360-b11219c99a64).
