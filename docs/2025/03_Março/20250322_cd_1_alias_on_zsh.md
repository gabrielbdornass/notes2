---
tags:
  - Linux
  - Zsh
---

# cd -1 alias on zsh

Durante o registro do vídeo [This may be my favorite CLI tool ever fzf](./20250321_youtube_this_may_be_my_favorite_cli_tool_ever_fzf.md) percebi que tenhos aliases que vão de 1 a 9:

```
(notes-py3.13) ➜  notes git:(main) ✗ alias
-='cd -'
...=../..
....=../../..
.....=../../../..
......=../../../../..
1='cd -1'
2='cd -2'
3='cd -3'
4='cd -4'
5='cd -5'
6='cd -6'
7='cd -7'
8='cd -8'
9='cd -9'
```

Perguntando ao [chatGPT](https://chatgpt.com/share/67def7ba-1e28-8003-9ade-985845f9fdab) descobri que in Zsh, `cd -<number>` move para para um diretório específico registrado no histórico de movimentações.
Para acessar este histórico, basta rodar o comando `dirs -v`:

```
$ dirs -v

0  /home/gabriel/projects
1  /etc/nginx
2  /var/log
3  /usr/local/bin
```

Neste exemplos:

  - `cd -1` me moverá para `/etc/nginx` (o segundo caminho da lista).
  - `cd -2` me moverá para `/var/log`, e assim por diante.
