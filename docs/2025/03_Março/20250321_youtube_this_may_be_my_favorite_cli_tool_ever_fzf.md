---
tags:
  - Linux
---

# YouTube | This may be my favorite CLI tool ever fzf

??? note "Assita o vídeo na íntegra"

    ![type:video](https://www.youtube.com/embed/oTNRvnQLLLs)

## Instalação

Instalando via [git](https://github.com/junegunn/fzf?tab=readme-ov-file#using-git). (1)
{ .annotate }

1. :man_raising_hand: Vídeo instala via [Linux packages](https://github.com/junegunn/fzf?tab=readme-ov-file#installation).

```
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

Para configurar integração com shell incluir no arquivo `~/.zshrc`

```
# Set up fzf key bindings and fuzzy completion
source <(fzf --zsh)

# Após inclusão é necessário
source ~/.zshrc
```

??? note "Erro `unknown option: --zsh` ao rodar `source ~/.zshrc`"

    Tentei instalar da primeira vez, conforme mostrado no vídeo, via [Linux packages](https://github.com/junegunn/fzf?tab=readme-ov-file#installation):

    ```
    sudo apt install fzf
    ```


    [A própria documentação](https://github.com/junegunn/fzf?tab=readme-ov-file#installation:~:text=fish%20%7C%20source-,Note,-%2D%2Dbash%2C%20%2D%2Dzsh) estava dizendo que a opção `--zsh` só estava disponível na versão `0.48` ou superior

    > --bash, --zsh, and --fish options are only available in fzf 0.48.0 or later. If you have an older version of fzf, or want finer control, you can source individual script files in the /shell directory. The location of the files may vary depending on the package manager you use. Please refer to the package documentation for more information. (e.g. apt show fzf)

    E a versão instalada com `sudo apt install fzf` foi a `0.29`.

    ```
    ➜  notes git:(main) ✗ fzf --version
    0.29 (devel)
    ```

    Rodei o comando `sudo apt upgrade fzf` para tentar atualizar a versão `fzf`, mas não funcionou.
    Acredito que este comando fez um upgrade em todos os pacotes/programas do computador elegíveis para, mas como o `fzf` já estava em sua última versão disponível, ele não foi atualizado.

    A solução foi dada [nesta resposta stackoverflow](https://askubuntu.com/a/1515772/1075583), instalando usando git, **opção final de instalação documentada no início da nota**.

## Utilização

- Basta utilizar o comando `fzf` para iniciar o modo de pesquisa de arquivos.
- Percebi que rodando dentro de uma pasta, por exemplo `code/` a pesquisa vai mais rápido, evitando ter que olhar os arquivos de toda máquina.
- Comando `fzf --preview="cat {}"` para apresentar um preview do arquivo.
- Depois o preview foi utilizado com `bat` (`fzf --preview="cat {}"`).
Mas como eu não tinha o programa insalado tive que realizar a instalação com `sudo apt install bat`.(1)
{ .annotate }

1.


## Investigações

- Percebi que `fzf` está buscando todos os arquivos, inclusive os dos ambientes virtuais Python (`venv` ou `.venv`).
Seria interessante ter um `.ignore` para estas pastas.
