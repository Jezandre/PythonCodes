class Pessoa:
    # getter
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return nome

    @property
    def idade(self):
        return idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


