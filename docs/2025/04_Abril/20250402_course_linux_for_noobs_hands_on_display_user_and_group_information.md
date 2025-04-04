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
      - `htop`:
          - [Linux htop](20250403_linux_htop.md)
          - Top: CPU and memory usage, as well as **how long your computer has been running (uptime)**.
          - Middle: A list of all the running programs (processes).
          - Bottom: Options for interacting with htop.

  - **Package managers** are similar to app stores for your phone. They simplify the process of finding and installing software.
  - `apt` is a widely used package manager for Debian-based systems, such as Ubuntu.
  - With `sudo apt update` we update the list of available packages. This ensures we're installing the latest version of a package.
  - `sudo` stands for "SuperUser DO." It allows you to execute commands with administrator privileges (temporarily).




- TODO: O que significa o usuário daemon? Descobri que existe este usuário quando rodei `cat /etc/passwd
