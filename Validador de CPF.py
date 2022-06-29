"""
funções (def) em Python - *args **kwargs
aula 16 (parte 3)

"""

def func(*args, **kwargs):
    print(args)

    idade= kwargs.get('idade')

    if idade is not None:
        print(idade)

lista = [1,2,3,4,5]
lista2= [10,20,30,40,50]
func(*lista, *lista2, nome='Luiz', sobrenome='miranda', idade = 30)

