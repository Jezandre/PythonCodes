"""
Classes - Programação orientada objetos
"""
from pessoa import Pessoa
p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Paulo', 29)
p1.comer('maçã')
p2.falar('POO')
p1.parar_comer()
p2.falar('POO')
p1.comer('aluminio')

print(p1.get_ano_nascimento())

#
# p1.nome = 'Luiz'
# p2.nome = 'João'
# print(p1.nome)

