---
tags:
  - Python
  - FastApi
---

# Curso fastApt 4 | Configurando o Banco de Dados e Gerenciando Migrações com Alembic

- [Link aula](https://fastapidozero.dunossauro.com/04/).

- **ORM** significa Mapeamento Objeto-Relacional.
É uma técnica de programação que vincula (ou mapeia) objetos a registros de banco de dados.
Em outras palavras, um ORM permite que você interaja com seu banco de dados, como se você estivesse trabalhando com objetos Python.

- O primeiro passo é instalar o SQLAlchemy, um ORM que nos permite trabalhar com bancos de dados SQL de maneira Pythonica. Além disso, o Alembic, que é uma ferramenta de migração de banco de dados, funciona muito bem com o SQLAlchemy e nos ajudará a gerenciar as alterações do esquema do nosso banco de dados.

- SQLAlchemy é constituída por duas partes principais: o Core e o ORM.
    - Core: O Core do SQLAlchemy disponibiliza uma interface SQL abstrata, que possibilita a manipulação de bancos de dados relacionais de maneira segura, alinhada com as convenções do Python.
    Através do Core, é possível construir, analisar e executar instruções SQL, além de conectar-se a diversos tipos de bancos de dados utilizando a mesma API.

    - ORM: ORM, ou Mapeamento Objeto-Relacional, é uma técnica que facilita a comunicação entre o código orientado a objetos e bancos de dados relacionais.
    Com o ORM do SQLAlchemy, os desenvolvedores podem interagir com o banco de dados utilizando classes e objetos Python, eliminando a necessidade de escrever instruções SQL diretamente.

- A 'Engine' do SQLAlchemy é o ponto de contato com o banco de dados.

- Quanto à persistência de dados e consultas ao banco de dados utilizando o ORM, a Session é a principal interface.

- Parei em Configuração do ambiente do banco de dados
