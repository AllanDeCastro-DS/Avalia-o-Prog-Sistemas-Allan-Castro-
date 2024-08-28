class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def valor_total(self):
        return self.quantidade * self.preco


class Inventario:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def exibir_produtos(self):
        for produto in self.produtos:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}, Preço Unitário: R${produto.preco:.2f}")

    def calcular_valor_total_estoque(self):
        total = sum(produto.valor_total() for produto in self.produtos)
        print(f"Valor total do estoque: R${total:.2f}")
        return total


# Exemplo de uso
inventario = Inventario()

# Adicionando produtos
inventario.adicionar_produto(Produto("Camiseta", 50, 29.90))
inventario.adicionar_produto(Produto("Calça", 30, 89.90))
inventario.adicionar_produto(Produto("Tênis", 20, 199.90))

# Exibindo produtos
inventario.exibir_produtos()

# Calculando valor total do estoque
inventario.calcular_valor_total_estoque()
