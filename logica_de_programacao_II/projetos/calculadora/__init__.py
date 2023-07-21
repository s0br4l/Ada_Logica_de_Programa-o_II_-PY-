from funcoes import soma, subtracao, divisao, multiplicacao


def calcule():
    a = float(input("Digite o 1o numero da operacao"))
    b = float(input("Digite o 2o numero da operacao"))
    operacao = input("Digite a operacao (soma ou + | subtracao ou - | divisao ou / | multiplicacao ou * )")
    if operacao == "+" or "soma":
        calc = soma(a, b)
    elif operacao == "-" or "subtracao":
        calc = subtracao(a, b)
    elif operacao == "/" or "divisao":
        calc = divisao(a, b)
    elif operacao == "*" or "multiplicacao":
        calc = multiplicacao(a, b)
    else:
        calc = "Tente novamente, digitando uma operacao válida"

    return calc

