"""
Relação de associação de classe

"""
from calsses import Escritor
from calsses import Caneta
from calsses import MaquinaDeEscrever


escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
# print(escritor.nome)
# print(caneta.marca)
# maquina.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever