import random
import string

# Gera um número inteiro entre A e B
inteiro1 = random.randint(10, 20)

print(inteiro1)

# Gera um número aleatório usando a função range()
inteiro2 = random.randrange(900, 1000, 10)
print(inteiro2)

# Gera um número aletório usando a função range
flutuante1 = random.uniform(10, 20)

print(flutuante1)

# Gera um número aleatório de ponto flutuante de 0,1
flutuante2 = random.random()

print(flutuante2)

# Sorteio de int

lista = ['Luiz', 'Jezandre', 'Thais', 'Ronilda', 'Lorena', 'Jucelio']

# Selelciona um item
sorteio = random.choice(lista)
print(sorteio)

# Seleciona k quantiades de itens que podem ser repetidos
sorteio = random.choices(lista, k=3)
print(sorteio)

# Seleciona k quantiades de itens sem se repetir
sorteio = random.sample(lista, k=3)
print(sorteio)

# Embaralhar a lista
random.shuffle(lista)
print(lista)

# Gerar senha aleatória

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*_=-'
geral = letras + digitos + caracteres

senha = ''
tentativas = 0
alfa ='3578p'
# senha = "".join(random.choices(geral, k=8))
while senha is not alfa:
    senha = "".join(random.choices(geral, k=5))
    if senha == alfa:
        tentativas += 1
        break
    print(tentativas, senha)

print(senha)