---
tags:
  - GitHub
---

# GitHub cli issue create error Your token has not been granted the required scopes to execute this query

Durante o trabalho com o CLI do GitHub para criação de issue (`gh issue create`) tentei incluir `Projects` como metadata do mesmo:

```
leiloes git:(main) ✗ gh issue create

Creating issue in gabrielbdornas/leiloes

? Title Realizar setup inicial do projeto
? Body <Received>
? What's next? Add metadata
? What would you like to add? Projects
? Projects Planner
? What's next? Submit
```

Mas recebi o seguinte erro:

```
GraphQL: Your token has not been granted the required scopes to execute this query.
The 'addProjectV2ItemById' field requires one of the following scopes:
['project'], but your token has only been granted the: ['admin:public_key', 'codespace', 'gist', 'read:org', 'read:project', 'repo', 'user:email'] scopes.
Please modify your token's scopes at: https://github.com/settings/tokens.
```

O erro indicava que meu token do GitHub não possuia a permissão necessária para adicionar a issue a um projeto (project scope).

A primeira sugestão do chatGPT foi acessar meus tokens e incluir esta permissão.
Ocorre que, como me lembrava, eu não criei este token, ele foi criado durante meu primeiro login no CLI.

Para confirmar, foi explicado que o CLI do GitHub usa autenticação OAuth no lugar de criar o token manualmente.

> That makes sense! When you first logged in with gh auth login, GitHub CLI likely used OAuth authentication instead of a manually created Personal Access Token (PAT).

Sendo assim, o comando sugerido para adicionar o escopo necessário foi:

```
# flag -s adiciona scopo project via OAuth authentication (autorização via browser)
gh auth refresh -h github.com -s project
```


## Outras referências

- [chatGPT](https://chatgpt.com/share/67d96f7f-a2c4-8003-8661-a4f4b908486b).
