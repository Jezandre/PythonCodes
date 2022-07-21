"""
Metaclasses

EM PYTHON TUDO É UM OBJETO: Incluindo classes
Metaclasses são as "classes" que criam classes.
type é uma metaclasse
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'attr_classe' in namespace:
            del namespace['attr_classe']
        # if 'b_fala' not in namespace:
        #     print(f'Oi, você precisa criar o método de b_fala em {name}')
        #
        # else:
        #     if not callable(namespace['b_fala']):
        #         print(f'b_fala precisa ser um método, não um atributo em {name}')

        return type.__new__(mcs, name, bases, namespace)


# class A(metaclass=Meta):
#     # def fala(self):
#     #     self.b_fala()
#
#
# class B(A):
# teste  = 'valor'
# b_fala = 'wow'
# pass
# def b_fala(self):
#     print('Oi')
# def sei_la(self):
#     pass


# b = B()

class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


b = B()
print(b.attr_classe)
