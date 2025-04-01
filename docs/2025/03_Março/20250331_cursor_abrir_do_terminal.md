# Cursor - abrir do terminal

Após a instalção do [cursor](./20250331_cursor_instalacao.md), precisei pesquisar como abrir um projeto via terminal (`cursor .`).

[Este auxílio chatGPT](https://chatgpt.com/share/67eb1456-8458-8003-9cb7-8a0d1696cda7) sugeriu criar a seguinte função no arquivo `zshrc` (1):
{ .annotate }

1. :man_raising_hand: A nota [How do I reload ZSH config files without replacing the current shell?](./20250324_how_do_i_reload_zsh_config_files_without_replacing_the_current_shell.md) mostra que a melhor maneira de reiniciar o terminal `zsh` é usando o comando `omz reload`.

```
cursor() {
    nohup /opt/cursor.AppImage "$@" > /dev/null 2>&1 &!
}
```

??? note "Entenda todo comando"

    ### 1. **`nohup`**
    - **`nohup`** stands for **no hang-up**. It is used to run a command and **keep it running** even after the terminal is closed.
    - Normally, when you run a command and close the terminal, the command would be terminated (because the terminal is its parent process). `nohup` prevents this termination by **detaching the command from the terminal**.
    - It also redirects the standard output to a file (`nohup.out` by default), but we’ll override that with our own redirection.

    ### 2. **`/opt/cursor.AppImage "$@"`**
    - **`/opt/cursor.AppImage`** is the actual executable for Cursor that you want to run.
    - **`"$@"`** is a special syntax in the shell that **passes all arguments** provided to the function (in this case, `cursor`) directly to the command being executed (the `cursor.AppImage` file).
      - For example, if you run `cursor .`, then `"$@"` passes `.` (the current directory) as an argument to `cursor.AppImage`.

    ### 3. **`> /dev/null 2>&1`**
    - **`> /dev/null`**: Redirects **standard output (stdout)** to `/dev/null`, which is a special file that **discards** any output. This prevents any regular output (like log messages) from showing up in the terminal.
    - **`2>&1`**: Redirects **standard error (stderr)** to the same place as standard output.
      - `2` refers to stderr (error messages).
      - `>&1` says, “redirect stderr to the same place as stdout.”
    - So, **both stdout and stderr** are discarded, ensuring no output or error messages are shown in the terminal.

    ### 4. **`&!`**
    - **`&`**: Puts the command in **background**. This means the terminal is free to run other commands immediately while `cursor.AppImage` runs in the background.
    - **`!`**: In **zsh**, this is a special operator that tells the shell to **not print job information** (like the job ID and PID) when a background process is started. It effectively **suppresses job reporting**.
      - Without `!`, you'd see a message like `[1] 53921`, which shows the background job’s ID and its process ID. The `!` ensures this doesn’t appear in the terminal.

    ### ✅ **Summary of What Happens:**
    1. **`nohup`** keeps the `cursor.AppImage` process running even after the terminal is closed.
    2. **`"$@"`** passes the arguments (like `.`) to `cursor.AppImage`.
    3. **`> /dev/null 2>&1`** ensures **no output** (including error messages) is shown in the terminal.
    4. **`&!`** runs the process in the background and **prevents job reporting**, keeping the terminal clean.

    This setup ensures that the **Cursor app** runs **in the background**, **without producing any output**, and **without blocking your terminal** or showing any job-related information.

Uma resposta IA Google me sugeriu criar um item no Desktop, **mas não achei a ideia interessante**.
Cheguei a testar achando que o `code .` funcionaria, mas não funcionou.
Deveria criar o arquivo `/usr/share/applications/cursor.desktop`, com o conteúdo (1):
{ .annotate }

1. :man_raising_hand: O vídeo [Master Cursor AI: EASY Step-by-Step Tutorial (Ubuntu, Linux)](https://www.youtube.com/watch?v=EX-0ui_hQMo) também me deu esta sugestão.


```
[Desktop Entry]
    Name=Cursor
    Exec=/opt/cursor.AppImage
    Icon=/opt/cursor.png  # Replace with the path to your icon if needed
    Type=Application
    Categories=Development;
```

## Outras referências

- [How to open cursor from terminal](https://forum.cursor.com/t/how-to-open-cursor-from-terminal/3757).
- [Master Cursor AI: EASY Step-by-Step Tutorial (Ubuntu, Linux)](https://www.youtube.com/watch?v=EX-0ui_hQMo).
