class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            printa('Saldo insulficiente')
            return

        self.saldo -= valor
        self.detalhes()
