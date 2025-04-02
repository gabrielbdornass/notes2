---
tags:
  - Linux
---

# fzf aliases

Após iniciar estudo da ferramenta [fzf](https://github.com/junegunn/fzf) com auxílio do vídeo [YouTube | This may be my favorite CLI tool ever fzf](./20250321_youtube_this_may_be_my_favorite_cli_tool_ever_fzf.md) resolvi criar alguns aliases:

- `fcode`: Pesquisa por algum arquivo e, ao encontrar (olhando conteúdo ao lado esquerdo da tela de pesquisa), abre o mesmo usando VsCode (`code`):
    - Atua como `fzf search + code .`.
    - `alias fcode='code $(fzf -m --preview="bat --color=always {}")'` configurado no arquivo `/home/gabrielbdornas/code/gabrielbdornas/dotfiles/aliases`.

- `cdh`: Pesquisa por algum diretório a partir da pasta home (`~/`) e, ao encontrar, abre o mesmo usando VsCode (`code`):
    - `cdh notes`.
    - `cdh dados-arm`.

- `cda`: Pesquisa por algum diretório em todo computador () e, ao encontrar, abre o mesmo usando VsCode (`code`):
    - `cda bin`.
    - `cda usr`.

??? note "Configurações que aprimoraram `cdh` e `cda`"

    - Instalção da ferramenta `fd` que, segundo [chatGPT](https://chatgpt.com/share/67defe4a-20e4-8003-b854-d66745edd913), é mais eficiente que `find`:

        - O primeiro script sugerido (`cd "$(fd --type d --hidden "$1" ~ | fzf)"`) não funcionou pois em minha máquina já existia um comando `fd` (1). Como no Ubuntu/Debian o pacote `fd` é instalado como `fdfind`, não precisei acabar com o alias `fd` (2).
        { .annotate }

            1. :man_raising_hand: Alias `fd='find . -type d -name'`.
            2. :man_raising_hand: Comando `unalias fd` não é definitivo. O alias retorna ao abrir outro terminal.

        - Quando fui instalar em meu wsl da CAMG, tive que instalar a ferramenta [fd](https://github.com/sharkdp/fd?tab=readme-ov-file#on-ubuntu) usando o comando `apt install fd-find`.

    - Configuração `export FD_OPTIONS="--ignore-file=$HOME/.ignore"`:

        - Durante os testes iniciais identifiquei o retorno do diretório `gabrielbdornas/.cache` ao buscar a pasta `notes`. `fdfind` automaticamente respeita configurações incluídas em arquivos `.gitignore`, mas como a pasta home (`/home/gabrielbdornas`) não possui arquivo `.gitignore` ela continuaria entrando nas pesquisas. **Para solucionar o problema criei o arquivo `~/.ignore` e adicionei `.cache` no mesmo**. Por fim, para que este arquivo fosse lido, tive que incluir a linha `export FD_OPTIONS="--ignore-file=$HOME/.ignore"` antes da criação dos comandos `cdh` e `cda`.

    ```
    # Arquivo `/home/gabrielbdornas/code/gabrielbdornas/dotfiles/zshrc`

    export FD_OPTIONS="--ignore-file=$HOME/.ignore"

    cdh() {
        cd "$(fdfind --type d --hidden "$1" ~ | fzf)"
    }

    cda() {
        cd "$(fdfind --type d --hidden "$1" / | fzf)"
    }
    ```



## Outras referências

- [chatGPT](https://chatgpt.com/share/67defe4a-20e4-8003-b854-d66745edd913).
