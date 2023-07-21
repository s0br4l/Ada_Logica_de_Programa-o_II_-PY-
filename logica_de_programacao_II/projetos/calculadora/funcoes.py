def soma(a: int or float, b: int or float):
    try:
        result = a + b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser uma int ou float, recebido a = {a}, {type(a)}, b = {b}, {type(b)})")
    else:
        return result


def subtracao(a, b):
    try:
        result = a - b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser uma int ou float, recebido a = {a}, {type(a)}, b = {b}, {type(b)})")
    else:
        return result


def divisao(a, b):
    try:
        result = a / b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser uma int ou float, recebido a = {a}, {type(a)}, b = {b}, {type(b)})")
    except ZeroDivisionError:
        print(f"O input 'b' deve ser diferente de ZERO")
    else:
        return result


def multiplicacao(a, b):
    try:
        result = a * b
    except TypeError:
        print(f"O input 'a' e 'b' devem ser uma int ou float, recebido a = {a}, {type(a)}, b = {b}, {type(b)})")
    else:
        return result
