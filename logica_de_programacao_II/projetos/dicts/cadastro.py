# Desafio
#
# Modifique a função cadastrar_usuario abaixo em que serão coletados as seguintes informações
# a partir da entrada da pessoa usuária:
#
# CPF (essa será a chave)
# Nome
# Idade
# Sexo
# Renda
# Estado
# 1-) Agora crie uma função que permita descobrir a idade média de pessoas cadastradas pelo sexo
# (para manter simples, masculino e feminino, representado por m e f,
# respectivamente (output: (('m', media_masc), ('f', media_fem))).
#
# 2-) Crie uma função que mostre a quantidade de pessoas por sexo (output: (('m', media_masc), ('f', media_fem))).
#
# 3-) Crie uma função que filtre os dados por estado (output: cadastros filtrado)
#
# 4-) Crie uma função que permita deletar um cadastro por CPF (output: cadastros)

from collections import namedtuple

Pessoa = namedtuple('Pessoa', ['cpf', 'nome', 'idade', 'sexo', 'renda', "estado"])


def cadastrar_usuario():
    continuar_cadastro = True

    cadastros = {}

    while continuar_cadastro:
        cadastrar = input('Deseja inserir um novo cadastro?')
        if cadastrar.lower() in ['sim', 's', 'yes', 'y']:
            cpf = input('Insira o cpf: ')
            nome = input('Insira o nome: ')
            idade = int(input('Insira a idade: '))
            sexo = input("Insira o sexo: ('M' para Masculino, 'F' para Feminino)")
            renda = float(input('Insira a renda: '))
            estado = input('Insira o estado: ')
            cadastro = Pessoa(cpf=cpf, nome=nome, idade=idade, sexo=sexo.lower(), renda=renda, estado=estado)
            cadastros[cpf] = cadastro
        elif cadastrar.lower() in ['não', 'n', 'nao', 'no']:
            print(f'Cadastro finalizado, inserido {len(cadastros)} novos')
            continuar_cadastro = False
        else:
            print(f'Opção invalida. Foi inserido "{cadastrar}",escolha entre [sim, s, yes, y] para cadastrar uma nova '
                  f'pessoa ou [não, nao, n, no] para parar')
    return cadastros


def calcule_media_idade_por_sexo(cadastros):
    idades_m = []
    idades_f = []
    idades_x = []
    for pessoa in cadastros:
        if pessoa.sexo == 'm':
            idades_m.append(pessoa.idade)
        elif pessoa.sexo == 'f':
            idades_f.append(pessoa.idade)
        else:
            idades_x.append(pessoa.idade)
    if len(idades_m) != 0:
        media_m = sum(idades_m) / len(idades_m)
    else:
        media_m = 0
    if len(idades_f) != 0:
        media_f = sum(idades_f) / len(idades_f)
    else:
        media_f = 0
    media_x = sum(idades_x) / len(idades_x)
    return ('m', media_m), ('f', media_f), ('X', media_x)


def conte_quantidade_por_sexo(cadastros):
    cpfs_m = []
    cpfs_f = []
    cpfs_x = []
    for pessoa in cadastros:
        if pessoa.sexo == 'm':
            cpfs_m.append(pessoa.cpf)
        elif pessoa.sexo == 'f':
            cpfs_f.append(pessoa.cpf)
        else:
            cpfs_x.append(pessoa.cpf)
    qntd_x = len(cpfs_x)
    qntd_m = len(cpfs_m)
    qntd_f = len(cpfs_f)
    return ('m', qntd_m), ('f', qntd_f), ('X', qntd_x)


def filtre_dados(cadastros, estado):
    ...


def delete_cadastro(cadastros, cpf):
    ...


cadastros = cadastrar_usuario()
print(cadastros)
print(calcule_media_idade_por_sexo(cadastros))
print(conte_quantidade_por_sexo(cadastros))
print(filtre_dados(cadastros, estado=...))
print(delete_cadastro(cadastros, ...))
