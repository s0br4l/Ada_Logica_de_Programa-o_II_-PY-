from random import choice


# Cria função que seleciona palavra aleatória da lista de nomes de frutas
def palavra_aleatoria():
    with open('frutas.txt', "r") as f:
        frutas = f.read().splitlines()
        frutas.remove('')
    fruta = choice(frutas)
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
