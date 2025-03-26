---
tags:
  - Python
  - FastApi
---

# Curso fastApt 2 | Introdução ao desenvolvimento WEB

- [Link aula](https://fastapidozero.dunossauro.com/02/).

- O Uvicorn no seu PC também pode servir o FastAPI na sua rede local:

```
fastapi dev fast_zero/app.py --host 0.0.0.0

task run --host 0.0.0.0
```

- Caso não esteja familiarizado com o terminal ou ferramentas para descobrir seu endereço IP:

```
>>> import socket
>>> s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
>>> s.connect(("8.8.8.8", 80))
>>> s.getsockname()[0]
'192.168.0.100'

# Servidor local
http://192.168.0.100:8000
```

- `task run` nos dá documentação automática em `http://127.0.0.1:8000/docs`.

- **Pydantic**: No universo de APIs e contratos de dados, especialmente ao trabalhar com Python, o [Pydantic](https://docs.pydantic.dev/latest/) se destaca como uma ferramenta poderosa e versátil.
Essa biblioteca, altamente integrada ao ecossistema Python, especializa-se na criação de schemas de dados e na validação de tipos. Com o Pydantic, é possível expressar schemas JSON de maneira elegante e eficiente através de classes Python, proporcionando uma ponte robusta entre a flexibilidade do JSON e a segurança de tipos do Python.

- Nossa estrutura de mensagem ficaria:

```
# {'message': 'Olá Mundo!'}

from pydantic import BaseModel


class Message(BaseModel):
    message: str
```
