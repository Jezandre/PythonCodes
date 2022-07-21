"""
Encapsulamento - esconder atributos

metodos e atributos publicos:
public, protected, private
__init__ = construtor
convenção no python

_protected - essa variavel não deve ser acessada pelo programador mesmo sendo publico
__privado - dois underlines indicam que não se deve de forma alguma acessar o atributo da classe, isto serve para funçoes

"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    # dar acesso aos valores do atributo
    @property
    def dados(self):
        self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apagar_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()

bd.inserir_cliente(1, 'Jezandre')
bd.inserir_cliente(2, 'Thais')
bd.inserir_cliente(3, 'Kevin')
bd.__dados = 'Outr Coisa'
print(bd.__dados)

# ler o atributo encapsluado de dentro da classe

print(bd._BaseDeDados__dados)
bd.dados ="outro valor"

bd.lista_clientes()
