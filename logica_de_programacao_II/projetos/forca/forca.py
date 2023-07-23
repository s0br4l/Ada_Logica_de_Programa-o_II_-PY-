from erros_forca import desenha_forca
import random


# pip install python-math

# Possíveis funções a serem criadas:

# Ok - Importar lista de frutas de arquivo
# Ok - Escolha da palavra aleatória
# Ok - Representar essa palavra com `_`
# Ok Ao acertar uma letra substituir o `_` pela letra nas posições corretas
# - Ao chegar no máximo de erros, encerrar o jogo
# - Ao acetar a palavra, finalizar o jogo
# - Ao errar uma letra, apresentar essas para a pessoa usuária
# - Ao errar uma letra, modificar o desenho da forca


# Cria função que carrega os dados do arquivo de texto
def carregar_arquivo():
    arquivo = open("/content/sample_data/frutas.txt", "r")
    frutas = arquivo.read()
    frutas = frutas.split()
    return frutas


# Cria função que seleciona palavra aleatória da lista de nomes de frutas
def palavra_aleatoria():
    frutas = carregar_arquivo()
    fruta = frutas[random.randint(0, len(frutas) - 1)]
    return fruta


# Cria função que desenha os subscritos para cada letra da palavra selecionada
def desenha_subscrito(palavra, letras_acertadas):
    for letra in palavra:
        if letra in letras_acertadas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()


def check_win(palavra, letras_acertadas):
    for letra in palavra:
        if letra not in letras_acertadas:
            return False
    return True


# Função para verificar se todas as letras foram acertadas
def todas_letras_acertadas(palavra, letras_acertadas):
    for letra in palavra:
        if letra not in letras_acertadas:
            return False
    return True


def verificar_erros(num_erros, max_erros, fruta_selecionada):
    if num_erros >= max_erros:
        print("Você perdeu! A palavra correta era:", fruta_selecionada)
        return False
    else:
        return True


def jogo_da_forca():
    fruta_selecionada = palavra_aleatoria()
    letras_acertadas = []  # Lista para armazenar as letras acertadas
    max_erros = 6
    num_erros = 0
    venceu = False
    continua_jogo = True
    letra_digitada = None

    letras_digitadas = []

    while continua_jogo:
        # Desenha os subscritos da palavra atual, considerando as letras acertadas
        desenha_subscrito(fruta_selecionada, letras_acertadas)
        continua_jogo = verificar_erros(num_erros, max_erros, fruta_selecionada)

        # Verifica se todas as letras foram acertadas
        if todas_letras_acertadas(fruta_selecionada, letras_acertadas):
            print("Parabéns! Você acertou a palavra!")
            venceu = True
            continua_jogo = False


        elif not continua_jogo:
            print("Fim do jogo")


        else:
            # Pede ao jogador para digitar uma letra
            try:
                letra_digitada = input("Digite uma letra: ").lower()
            except:
                print("O usuário interrompeu o programa.")
                return

            # Verifica se a letra já foi digitada antes
            if letra_digitada in letras_digitadas:
                print("Você já digitou essa letra.")


            # Adiciona a letra à lista de letras acertadas, caso ela esteja na palavra
            elif letra_digitada in fruta_selecionada:
                letras_acertadas.append(letra_digitada)
                letras_digitadas.append(letra_digitada)

            else:
                print("A letra não faz parte da palavra.")
                num_erros += 1
                desenha_forca(num_erros)
                letras_digitadas.append(letra_digitada)

# Executa o jogo
# jogo_da_forca()
