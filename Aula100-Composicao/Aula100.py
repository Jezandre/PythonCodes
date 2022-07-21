"""
Composição uma classe pertence a outra ou seja se um objeto em uma classe for apagada os da outra classe também serão


"""

from classe import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte,', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Jezandre', 29)
cliente2.insere_endereco('Salvador,', 'BA')
cliente2.insere_endereco('Rio de Janeiro,', 'RJ')
print(cliente2.nome)
cliente2.lista_enderecos()
del cliente2
print()

cliente3 = Cliente('Thais', 32)
cliente3.insere_endereco('São Paulo,', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
del cliente3

