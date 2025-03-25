# Instalação internet servidor debian camg

- [Acesso servidor debian camg](./20250325_acesso_servidor_debian_camg.md).


## Outras referências

- [conversa chatGPT](https://chatgpt.com/share/67e303ad-ac64-8003-8744-9790304c965c).
Muito complicado este tipo de trabalho.
Tenho que ficar olhando o chatGPT em uma tela (meu computador) e digitando na outra.
O ideal seria que eu conseguisse realizar um acesso ssh na máquina, mas por enquanto não consegui nem acessar a internet.
Acredito que uma saída seria tentar reformatar a máquina, já tendo ela na rede ou ligando o wifi durante processo de formatação.

Outro problema foi conseguir baixar no meu wsl os pacotes supostamente necessários para ligar o drive que faria a instalação do wifi na máquina.
Só consegui com `curl` depois de algum tempo:

```
curl -u m7522667:110715_Dias5 -x http://proxycamg.prodemge.gov.br:8080 -O "http://ftp.debian.org/debian/pool/main/m/modemmanager/libmm-glib0_1.14.12-0.2_amd64.deb"
```

Com `wget` não funcionou.
