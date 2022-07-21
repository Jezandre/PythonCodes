""""
https://rszalski.github.io/magicmethods
"""


class A:
    # def __new__(cls, *args, **kwargs):
    #     if not hasattr(cls, '_jaexiste'):
    #         cls._jaexiste = object.__new__(cls)
    #     return cls._jaexiste

    # def __init__(self):
    #     pass
    #
    # def __call__(self, *args, **kwargs):
    #     resultado = 1
    #
    #     for i in args:
    #         resultado *= i
    #     return resultado
    #
    # utilizado para settar
    # def __setattr__(self, key, value):
    #     print(key, value)
    #


a = A()
a.nome = 'Luiz Otávio'
print(a.nome)
