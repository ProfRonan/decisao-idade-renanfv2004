[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10704073&assignment_repo_type=AssignmentRepo)
# Exercício que testa idade

O script principal de vocês deve estar no arquivo `main.py`.

O testador automático vai rodar o comando `python main.py` para rodar o script.

## 📝 Instruções

- Faça um programa que recebe um valor digitado pelo usuário.
- Esse valor deve ser convertido em inteiro.
- Se o usuário digitar um número negativo: o programa deve imprimir `impossível!`
- Se o usuário digitar um número menor que 18: o programa deve imprimir `não precisa se alistar.`
- Se o usuário digitar um número maior que 18 e menor do que 65: o programa deve imprimir `Não esqueça de votar na próxima eleição.`
- Se o usuário digitar um número maior do que 65: o programa deve imprimir `Vá descansar.`
- Se nada disso acontecer, o programa deve imprimir `eita!`

Exemplos:

- Se o usuário digitar `-1`, o programa deve imprimir

  ```
  impossível!
  não precisa se alistar.
  ```

- Se o usuário digitar `18`, o programa deve imprimir

  ```
  eita!
  ```

- Se o usuário digitar `65`, o programa deve imprimir

  ```
  eita!
  ```

- Se o usuário digitar `64`, o programa deve imprimir

  ```
  Não esqueça de votar na próxima eleição.
  ```
