# Cursor - instalação

No [site oficial](https://www.cursor.com/) já aparece o link para o Download.
Ao clicar duas vezes no arquivo não consegui realizar a instalação.
Tentei executar o arquivo via `./<nome-arquivo>`, mas recebi os erros abaixo:

```
➜  Downloads ./Cursor-0.47.9-x86_64.AppImage
zsh: permission denied: ./Cursor-0.47.9-x86_64.AppImage
➜  Downloads sudo ./Cursor-0.47.9-x86_64.AppImage
[sudo] password for gabrielbdornas:
sudo: ./Cursor-0.47.9-x86_64.AppImage: command not found
```

Então lembrei que teria que liberar o arquivo como executável via `chmod 777`:

```
chmod 777 Cursor-0.47.9-x86_64.AppImage
```

Então a instalação funcionou:

```
Downloads ./Cursor-0.47.9-x86_64.AppImage
```
