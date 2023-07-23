# Projeto Lógica de programação II

## Jogo da forca

Nome: <br>
Marco de Pereira Binda <br>
Leandro Coutinho Cesário Júnior <br>
Rhuan Victor Santos Lopes <br>
Lucas Sobral <br>

Turma:<br>
Grupo 03


Nesse projeto iremos focar no conhecimento adquirido durante os módulos de lógica de programação I e II.

Utilizaremos as estruturas de dados (tuplas, listas, dicionários) além da lógica de programação (if/else, while, e for), lembre-se das compreensões de listas e dicionários. E utilize as técnicas e algoritmos que achar necessário para realizar o projeto


### Dados

Será utilizado os dados (dataset) de frutas (`frutas.txt`) disponível em um arquivo separado.

Nesse arquivo, cada linha representa uma palavra correspondente a uma fruta distinta.

### O problema

Nesse projeto você deverá desenvolver um programa que permita aceitar ações da pessoa usuária (`input`).

Nesse processo, o programa deve selecionar uma palavra aleatória do arquivo `frutas.txt`.

A partir da palavra aleatória, crie um jogo da forca, em que a pessoa usuária pode inserir um caracter, e se tiver acerto, a palavra será preenchida. Em caso de erro, será retirada uma "vida" da pessoa usuária e o desenho da pessoa na forca deve ser preenchida.

Na tela, teremos:
- Desenho da forca
- Letras já escolhidas
- Uma linha mostrando a palavra.
  - No inicio cada letra da palavra a ser adivinhada é representada com `_`
  - Ao acertar a letra presente na palavra, as posições referentes a essa letra serão substituidas e mostrada para a pessoa usuária.

Para auxiliar no desenvolvimento, podemos dividir o projeto nas seguintes fases:
- Escolha da palavra aleatória
- Representar essa palavra com `_`
- Ao acertar uma letra substituir o `_` pela letra nas posições corretas
- Ao chegar no máximo de erros, encerrar o jogo
- Ao acetar a palavra, finalizar o jogo
- Ao errar uma letra, apresentar essas para a pessoa usuária
- Ao errar uma letra, modificar o desenho da forca

### Critérios de avaliação

Os seguintes itens serão avaliados:

1. Reprodutibilidade do código: seu código será executado e precisa gerar os mesmos resultados apresentados por você;

2. Clareza: seu código precisa ser claro e deve existir uma linha de raciocínio direta. Comente o código em pontos que julgar necessário para o entendimento total;

3. Utilize funções para melhorar a clareza do código!


### Informações gerais

- O projeto pode ser desenvolvido em grupo

- Pelo github

Anexar, na entrega, o código (notebook ou script python) desenvolvido.


```
erro_0 = """
   |-------
   |      |
   |
   |
   |
   |
   |
___|___
"""
erro_1 = """
   |-------
   |      |
   |      _
   |     |_|
   |
   |
   |
___|___
"""

erro_2 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |      |
   |      |
   |
___|___
""")

erro_3 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|
   |      |
   |
___|___
""")

erro_4 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |
___|___
""")

erro_5 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     /
___|___
""")

erro_6 = ("""
   |-------
   |      |
   |      _
   |     |_|
   |    --|--
   |      |
   |     / \\
___|___
""")
```

```
import os
def main():
  end = False
  while not end:
      # for windows
      if os.name == 'nt':
          _ = os.system('cls')

      # for mac and linux(here, os.name is 'posix')
      else:
          _ = os.system('clear')
```