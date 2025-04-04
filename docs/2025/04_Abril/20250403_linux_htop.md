---
tags:
  - Linux
---

# Linux htop

- Visto no [Course Linux for Noobs (Hands-on) | Display user and group information](20250402_course_linux_for_noobs_hands_on_display_user_and_group_information.md)
- `htop` is a tool that allows you to monitor system resources and processes.
- It provides a more detailed and user-friendly interface compared to traditional tools like `top`.
- `htop` is a graphical interface for managing processes and system resources.

- In htop, the top portion of the display provides an overview of system resource usage.
Here's a breakdown of what the information typically shows:

    - **CPU Usage**:
        - `0[ |||| 15%]` represents the first CPU core.
        - The number `0` indicates the CPU core number.
        - The bar (e.g., `||||`) visually represents the CPU usage on that core.
        - The percentage `15%` shows the actual CPU utilization for that core.
        - If you have multiple CPU cores, you'll see similar entries for each core (e.g., `1[ ||| 10%]` for the second core, etc.).

    - **Memory Usage**:
        - Below the CPU usage, you'll usually see a line for RAM usage, indicating total, used, and available memory.

    - **Swap Usage**:
        - This shows information about swap memory, similar to RAM.

    - **Load Average**:
        - The load average might also be displayed, showing the system load averaged over 1, 5, and 15 minutes.

    - **Process Count**:
        - The number of tasks currently running, sleeping, etc.

- Para matar um processo usando `htop` basta usar a techa ++f9++. Selecione o processo com a tecla ++f3++ (1) para localizar o processo desejado. Com ele selecionado, basta apertar ++f9++ e ++enter++ (2).
{ .annotate }

    1. :man_raising_hand: Setas para cima ++up++ ou para baixo ++down++ também funcionam.
    2. :man_raising_hand: Lembro que quando estava tentando [configurar o metabase](https://github.com/splor-mg/projetos/issues/18) tive dificuldade de achar o processo `java` que estava rodando. Com este conhecimento teria sido mais fácil.
