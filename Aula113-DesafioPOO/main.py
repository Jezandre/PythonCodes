from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()
cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Jezndre', 28)
cliente3 = Cliente('Thais', 25)

conta1 = ContaPoupanca(1111, 485685, 0)
conta2 = ContaCorrente(2222, 123456, 0)
conta3 = ContaPoupanca(1204, 485685, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(50)
    cliente1.conta.sacar(20)
    print('##############################')

else:
    print('Cliente não autenticado')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(50)
    cliente2.conta.sacar(100)
    print('##############################')
else:
    print('Cliente não autenticado')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(50)
    cliente3.conta.sacar(20)
    print('##############################')

else:
    print('Cliente não autenticado')