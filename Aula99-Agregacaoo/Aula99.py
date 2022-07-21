"""
Agregação
Apropriação

"""

from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()
p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('Caneca', 15)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)


carrinho.lista_produto()
print(f'Total {carrinho.soma_total()}')
