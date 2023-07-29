from erros_forca import desenha_forca
from funcoes import *
import os


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
                os.system('cls' if os.name == 'nt' else 'clear')
            except:
                print("O usuário interrompeu o programa.")
                return

            # Verifica se a letra já foi digitada antes
            if letra_digitada in letras_digitadas:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Você já digitou essa letra.")
                print(f"As letras digitadas foram: ", letras_digitadas)

            # Adiciona a letra à lista de letras acertadas, caso ela esteja na palavra
            elif letra_digitada in fruta_selecionada:
                os.system('cls' if os.name == 'nt' else 'clear')
                letras_acertadas.append(letra_digitada)
                letras_digitadas.append(letra_digitada)
                print(f"As letras digitadas foram: ", letras_digitadas)

            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("A letra não faz parte da palavra.")
                num_erros += 1
                desenha_forca(num_erros)
                letras_digitadas.append(letra_digitada)
                print(f"As letras digitadas foram: ", letras_digitadas)


# Executa o jogo
jogo_da_forca()
