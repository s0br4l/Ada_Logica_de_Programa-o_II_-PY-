# Desafio

# Crie um sistema de cadastro de produtos. Neste sistema podemos:

# Adicionar um novo produto
# Remover um produto da base
# Consultar quais são os produtos cadastrados
# Consultas quais os produtos cadastrados e suas quantidades disponíveis
# Adicionar informações extras por produto (descrição por exemplo)
# Adicionar ao estoque de um produto
# Remover do estoque um produto (nota, o total em estoque não pode ser menor que 0)
# Para tal crie as seguintes funções:

# cadastre_produto
# delete_produto
# adicione_produto_estoque
# remova_produto_estoque
# consulte_produtos
# consulte_quantidade
# consulte_descricao_produto
# ative_sistema
# Essa função irá gerenciar todas as funções acima (como um sistema central)
# Os atributos possíveis são:

# Nome do produto
# Quantidade do produto
# descrição
# Informações adicionais


def cadastre_produto(nome, quantidade=0, descricao='', **kwargs):
  """Essa função cadastra um novo produto com os campos:
    - nome do produto (obrigatório)
    - quantidade (opcional)
    - descrição (opcional)
    - outros campos
    Ps: o nome do produto é único, logo podemos pensar como uma chave única
  """
  nome = input('Digite o nome do produto: ')
  quantidade = int(input('Digite a quantidade do produto: (deixe em branco para 0)'))
  descricao = input('Digite a descricao do produto: (ou deixe em branco)')
  if nome not in produtos.keys():
    produtos[nome] = {'quantidade':quantidade, 'descricao': descricao}


def delete_produto():
  """ Essa função deleta um produto da base pelo `nome do produto`
  """

def adicione_produto_estoque():
  """ Essa função adiciona ao estoque uma quantidade de um dado produto
      Nota: Não pode ser aceito quantidade negativas
  """

def remova_produto_estoque():
  """ Essa função remove do estoque uma quantidade de um dado produto
      Nota: Não pode ser aceito quantidade negativas
  """

def consulte_produtos():
  """ Essa função mostra os produtos disponíveis no sistema (somente nome)
  """

def consulte_quantidade():
  """ Essa função mostra os produtos e a quantidade disponíveis no sistema
  """

def consulte_descricao_produto():
  """ Essa função mostra a descrição e as Informações adicionais de um dado produto
  """

def ative_sistema():
  """ Essa função aceita as interações do usuário, coordenando qual ação deve ser tomada
      Cada ação refere-se as funções desenvolvidas acima.
      Nota: o que fazer se for inserida uma ação inválida?
  """
