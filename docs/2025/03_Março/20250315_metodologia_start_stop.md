---
tags:
  - Office like code
---

# Metodologia start stop

Acredito que amadureci alguns pontos sobre a lógica para [calcular tempo gasto para finalizar um issue](https://github.com/meadapt/planner/issues/25).
A ideia de registrar o início e fim do trabalho ficou um pouco mais clara ao tentar implementá-la[^1].

Pensei em criar a lógica start-stop:

- Sempre ao iniciar a resolução de um Issue devemos criar um `--allow-empty` commit `start`:

```
git commit --allow-empty
```

- A flag `-m` não deverá ser utilizada pois escreveremos mais do que somente a mensagem do commit.
Deveremos registar:

```
# commit file

<issue-number>-start

See #<issue-number>
```

- Desta maneira o início do trabalho ficará ligado diretamente ao Issue.

- Da mesma forma, sempre ao finalizar a resolução de um Issue, ou sendo necessário parar sem a resolução completa, devemos criar um `--allow-empty` commit `stop` sem a flag `-m`:

```
# commit file

<issue-number>-stop

See #<issue-number>
```

## Reflexões

- Esta lógica serviria mais como uma vontade individual de entender o tempo gasto e sua divisão entre tarefas do que uma ferramenta de gestão de equipe.
- Como ferramenta de gestão de equipe seria suficiente a pactuação de Issues no Board do Projeto da equipe por mês.
- Poderíamos pensar algo menos custoso, como a inclusão de `See #<issue-number>` diretamente na mensagem do commit.
Vi que o [link entre commit e o Issue](https://github.com/gabrielbdornass/frictionless-drescribe-tutorial/issues/1) funciona perfeitamente.
Poderia ser algo:
    - `git commit --allow-empty -m "start see #<issue-number>"` e `git commit --allow-empty -m "stop see #<issue-number>"`.
    - Seria mesmo necessário `start` e `stop` na mensagem? Um commit `--allow-empty` não seria suficiente para marcar início e fim da atividade?
    Neste cenário, commits em pares, seria utilizados para o cálculo.
- A gestão de board de projeto de equipe seria mais importante, do ponto de vista de gestão de time do que acompanhar estes indicadores.

## Atualização 20/03/2024

- Com auxílio do [chatGPT](https://chatgpt.com/c/67da1c49-4f24-8003-8bbc-1cc5a1188f8a) criei uma função para simplificar o processo start-stop:

```
nano ~/.bashrc  # or ~/.zshrc if you're using Zsh

# ~/.zshrc

start() {
    if [ -z "$1" ]; then
        echo "Usage: start <issue_number>"
        return 1
    fi
    git commit --allow-empty -m "$1-start" -m "See #$1"
    echo "Started tracking Issue #$1"
}

stop() {
    if [ -z "$1" ]; then
        echo "Usage: stop <issue_number>"
        return 1
    fi
    git commit --allow-empty -m "$1-stop" -m "See #$1"
    echo "Stopped tracking Issue #$1"
}
```

Com isso basta rodar `start <issue-number>` e `stopt <issue-number>` para registrar o tempo gasto entre os commits responsáveis pela finalização de um Issue.

[^1]: Realmente [não é muito fácil no início](https://github.com/meadapt/planner/issues/25#issuecomment-2387357354), mas a maturidade e a vontade de dar certo fazem um pouco de difirença.
