---
tags:
  - Frictionless
---

# Frictionless - Leitura documentação

- [Specs](https://datapackage.org/overview/software/).
- Na página de [software](https://datapackage.org/overview/software/) encontrei referência para o [open data editor](https://opendataeditor.okfn.org/), não cheguei a testar.
- Na página de [software](https://datapackage.org/overview/software/) encontrei uma boa referência para um aplicativo chamado [dataflows](https://github.com/datahq/dataflows).
    - Ele pode ser uma boa alternativa para Airflow, e já usa o padrão frictionless.
    - Pode ser rodado usando `dataflows init <github-raw-content>`.
    - Usei `pipx` como teste para baixar um recurso e funcionou:

    ```
    pipx run dataflows init https://raw.githubusercontent.com/splor-mg/dados-sisor-2025/refs/heads/main/data/base_orcam_receita_fiscal.csv
    ```
- Achei interessante esta estrutura de [governança](https://datapackage.org/overview/governance/) criada.
- Ideia de como [novas versões são publicadas](https://datapackage.org/overview/contributing/#branching-and-releasing) podem ser aproveitadas em algum momento. Exemplo: `main` para o que está no site e `next` para o que está em desenvolvimento.
- [Releasing model](https://datapackage.org/overview/contributing/#releasing-model) mostra como é o fluxo de publicação de novas versões, onde é ulizado a estratégia "Squash and merge" durante o merge dos PRs.
    - Todos as branchs são mergiadas na `next` e somente depois esta é mergiada na `main` utilizando a estratégia "Create a merge commit".
    - Seria interessante entender porque as estrétégias `squash` e `merge commit` são utilizadas para cada um dos pontos do fluxo.
    TODO: Entender melhor a diferença entre "Squash and merge" e "Create a merge commit" e qual a melhor situação para utilizar cada uma delas.


- Parei na parte [Codebase contribution](https://datapackage.org/overview/contributing/#codebase-contribution).
