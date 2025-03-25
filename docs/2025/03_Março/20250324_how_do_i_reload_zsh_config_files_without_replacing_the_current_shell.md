# How do I reload ZSH config files without replacing the current shell?

[Esta resposta Stackoverflow](https://stackoverflow.com/a/73895726/11755155) mostra o comando `omz reload`.
Também passou o caminha para este [Cheatsheet amz](https://github.com/ohmyzsh/ohmyzsh/wiki/Cheatsheet).

Achei interessante que o Cheatsheet fala para não usar `source ~/.zshrc:

> To apply changes made to .zshrc: omz reload (this just runs exec zsh). Do NOT run source ~/.zshrc

[Este faq](https://github.com/ohmyzsh/ohmyzsh/wiki/FAQ#how-do-i-reload-the-zshrc-file) explica melhor porque.
