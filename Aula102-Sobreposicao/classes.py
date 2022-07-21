 # Superclasse
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse =self.__class__.__name__
    def falar(self):
        print(f'{self.nomeclasse} Falando...')


# subclasses
class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print(f'{self.nomeclasse} Falando.1023132..')

class ClienteVIP(Cliente):
    def __init__(self,nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome
    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print (f'{self.nome} {self.sobrenome}')



class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclasse} estudando...')
