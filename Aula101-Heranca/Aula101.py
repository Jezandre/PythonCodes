"""
Herança

"""
from classes import *

c1 = Cliente('Luiz',45)
print(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria',30)
print(a1.nome)
c1.falar()
a1.estudar()