---
tags:
  - Git
  - GitHub
---

# Como mudar datetime de um commit


Durante a inversão da ordem de dois commits (1), percebi que fica estranho um commit mais recente com o horário anterior ao seu predecessor.
{ .annotate }


1. :man_raising_hand: [Como inverter a ordem de commits](./20250315_como_inverter_a_ordem_de_commits.md).

[Esta resposta Stackoverflow](https://stackoverflow.com/a/5017265/11755155) me mostrou algumas maneiras de modificar estes horários (timestamp ou datetime), inclusive, utilizando o comando `rebase`.

No meu caso em questão, como se tratava do commit mais recente preferi utilizar o `--amend` no lugar do `rebase`:

```
# --date=now will use the current time.
git commit --allow-empty --amend --date=now --no-edit

# Othe datetime then now
git commit --amend --date="Wed Feb 16 14:00 2011 +0100" --no-edit
```

Quando rodei o comando pela primeira vez, não inclui a flag `--allow-empty`, e como se tratava do último commit `--amend` recebi a sugestão de refazer o último commit por inteiro usando o comando `reset` (`git reset HEAD^`).

```
(notes-py3.13) ➜  notes git:(main) git commit --amend --date=now --no-edit
On branch main
No changes
You asked to amend the most recent commit, but doing so would make
it empty. You can repeat your command with --allow-empty, or you can
remove the commit entirely with "git reset HEAD^".
```

!!! Warning

    [Cuidado ao modificar commits já enviados para GitHub](./20250317_cuidado_ao_modificar_commits_ja_enviados_para_github.md), pois será necessário realizar `pull/push` com a flag `--force`.

## Outras referências

- [7.6 Git Tools - Rewriting History](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History).
