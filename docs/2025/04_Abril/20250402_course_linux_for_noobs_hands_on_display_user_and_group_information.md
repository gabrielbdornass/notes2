---
tags:
  - Roadmap.sh
  - Linux
---

# Course Linux for Noobs (Hands-on) | Display user and group information

  - The best way to learn Linux (and programming in general) is by doing.
  - Linux is case-sensitive: `echo`, `Echo`, and `ECHO` are all different.
  - Comandos:
      - `echo`: Displays text or variables to the terminal output.
      - `whoami`: Shows the current logged in username.
      - `id`: Displays user and group information for a specified user or the current user if none specified (1).
      { .annotate }

        1. :man_raising_hand: You can also use `id root` to look up other users. The `root` is the superuser, like the administrator of the system.


        ```
        uid: Your User ID (a unique numerical identifier).
        gid: Your primary Group ID.
        groups: All the groups you are a member of.
        uid=1000(gabrielbdornas) gid=1000(gabrielbdornas) groups=1000(gabrielbdornas),4(adm),27(sudo),123(lpadmin),138(libvirt),999(docker)
        ```

      - `cat /etc/passwd`: This will display a list of all users along with their information.
      - `htop` shows:
          - Top: CPU and memory usage, as well as **how long your computer has been running (uptime)**.
          - Middle: A list of all the running programs (processes).
          - Bottom: Options for interacting with htop.

  - **Package managers** are similar to app stores for your phone. They simplify the process of finding and installing software.
  - `apt` is a widely used package manager for Debian-based systems, such as Ubuntu.
  - With `sudo apt update` we update the list of available packages. This ensures we're installing the latest version of a package.
  - `sudo` stands for "SuperUser DO." It allows you to execute commands with administrator privileges (temporarily).

  ??? notes "top htop"

      In htop, the top portion of the display provides an overview of system resource usage. Here's a breakdown of what the information typically shows:

      CPU Usage:
      0[ |||| 15%] represents the first CPU core.
      The number 0 indicates the CPU core number.
      The bar (e.g., ||||) visually represents the CPU usage on that core.
      The percentage (15%) shows the actual CPU utilization for that core.
      If you have multiple CPU cores, you'll see similar entries for each core (e.g., 1[ ||| 10%] for the second core, etc.).

      Memory Usage:

      Below the CPU usage, you'll usually see a line for RAM usage, indicating total, used, and available memory.
      Swap Usage:

      This shows information about swap memory, similar to RAM.
      Load Average:

      The load average might also be displayed, showing the system load averaged over 1, 5, and 15 minutes.
      Process Count:

      The number of tasks currently running, sleeping, etc.
      This overview helps you quickly assess the performance and resource utilization of your system. If you need more specific details about each component, feel free to ask!

- TODO: O que significa o usuário daemon? Descobri que existe este usuário quando rodei `cat /etc/passwd
- TODO: Como matar um processo usando F9 no `htop` (documentar). Basta selecionar o processo com setinhas para cima ou para baixo, ou até usar o F3 para localizar o processo desejado. Com ele selecionado, basta apertar F9 e enter. Lembro que quando estava tentando usar o metabase tive dificuldade de achar o processo java que estava rodando. Com este conhecimento teria sido mais fácil.
