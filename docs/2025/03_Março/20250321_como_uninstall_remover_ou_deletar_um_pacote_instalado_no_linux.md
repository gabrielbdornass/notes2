---
tags:
  - Linux
---

# Como uninstall remover ou deletar um pacote instalado no linux

To remove the binaries, but not the configuration or data files of the package packagename use the `remove` command.
It will also leave dependencies.

```
sudo apt-get remove <package name>
```

To remove about everything regarding the package packagename, but not the dependencies installed with it on installation.

```
apt-get remove --purge packagename
```

## Outras referências

- [Resposta stackoverflow consultada](https://askubuntu.com/a/187891/1075583).
