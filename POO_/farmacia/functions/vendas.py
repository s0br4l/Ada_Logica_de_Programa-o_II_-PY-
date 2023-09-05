class Venda:
    lista_vendas = {}
    n_vendas = 0

    def __int__(self, data: str, hora: str, produtos: dict, valor: float):
        self.data = data
        self.hora = hora
        self.produtos = produtos
        self.valor = valor

    def registrar(cliente):
        data = VendaTemp.lista_vendas[cliente]["data"]
        hora = VendaTemp.lista_vendas[cliente]["hora"]
        produtos = VendaTemp.lista_vendas[cliente]["produtos"]
        valor = VendaTemp.lista_vendas[cliente]["valor"]
        Venda.lista_vendas[cliente] = {"cliente": cliente, "data": data, "hora": hora,
                                       "produtos": produtos, "valor": valor}
        Venda.n_vendas += 1
        VendaTemp.lista_produtos.clear()

    def listar():
        lista_ordenada = dict(sorted(Venda.lista_vendas.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada


class VendaTemp(Venda):
    lista_vendas = {}
    lista_produtos = {}

    def __int__(self, data: str, hora: str, produtos: dict, valor: float):
        super().__int__(self, data, hora, produtos, valor)

    def registrar(cliente, data, hora, produto, quantidade, valor):
        VendaTemp.lista_produtos[produto] = quantidade
        VendaTemp.lista_vendas[cliente] = {"cliente": None, "data": None, "hora": None,
                                           "produtos": None, "valor": None}
        VendaTemp.lista_vendas[cliente]["cliente"] = cliente
        VendaTemp.lista_vendas[cliente]["data"] = data
        VendaTemp.lista_vendas[cliente]["hora"] = hora
        VendaTemp.lista_vendas[cliente]["produtos"] = VendaTemp.lista_produtos
        VendaTemp.lista_vendas[cliente]["valor"] = valor

    def listar():
        lista_ordenada = dict(sorted(VendaTemp.lista_vendas.items(), key=lambda item: item[0], reverse=False))
        return lista_ordenada

    def buscar(cpf):
        if cpf in VendaTemp.lista_vendas:
            return VendaTemp.lista_vendas[cpf]
        else:
            return 'CPF não tem compras em aberto'




