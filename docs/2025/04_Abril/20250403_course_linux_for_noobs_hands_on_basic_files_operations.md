---
tags:
  - Roadmap.sh
  - Linux
---

# Course Linux for Noobs (Hands-on) | Basic files operations

- In Linux, each user typically has a home directory, represented by `~`(1).
{ .annotate }

    1. :man_raising_hand: You can also use `~` to represent the home directory of another user. For example, `~gabrielbdornas` would take you to the home directory of the user `gabrielbdornas`. `echo ~` would display the home directory of the current user.

- `pwd` stands for "print working directory". It displays your current location in the file system.
- `ls` lists the files and directories in the current directory. `ls ~` would list the files and directories in the home directory of the current user. `ls -la` would list all files and directories in the current directory, including hidden ones, and in a long format.
- `cd` stands for "change directory". It allows you to navigate through the file system. `cd ~` would take you to the home directory of the current user.
- `cd ..` would take you to the parent directory of the current directory. The `..` means "the directory above".
- `cd foldername` would take you to the foldername directory.
- `cd /home/user/gabrielbdornas` would take you to the `gabrielbdornas` directory in the `home` directory. The `/home/user/gabrielbdornas` is an **absolute path** because it starts from the root directory.
- The `touch` (1) command is used to create an empty file. **If the file already exists, it updates the file's timestamp without changing its content**. It's a simple way to create new, empty files.
{ .annotate }

    1. :man_raising_hand: [Esta discussão](https://unix.stackexchange.com/questions/355168/what-does-touch-stand-for) foi interessante para entender porque o comando `touch` é chamado de "touch". A melhor resposta foi: 'When you touch a file, you're "putting fresh fingerprints on it", updating its last-modified date (or creating it if it did not yet exist)'. Mas eu gostei bastante da explicação: 'I suppose one could ask "when was the file last touched?" to mean when it was last changed (e.g. by writing to it), or "the file hasn't been touched in years". The touch command simulates the effect, hence the name'.

- The command `echo "Hello, Linux" > file2.txt` creates a new file named `file2.txt` and writes the text "Hello, Linux" into it. If the file already exists, it will be overwritten. The `>` symbol redirects the output of echo into a file named `file2.txt`. If the file doesn't exist, it's created. If it does exist, its content is replaced.
- In Linux, any file or directory name that starts with a dot (.) is considered hidden ()`echo "Hello, Linux" > .file2.txt`).
- The `mkdir` command (short for "make directory") creates a new directory.

- Parei em `Copying Files and Directories`.
