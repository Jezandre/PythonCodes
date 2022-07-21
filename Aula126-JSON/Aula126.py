from dados import *
import json

# lista = [1,2,3,4,5,6]
# dados_json = json.dumps(clientes_dicionario, indent=4)
#
# print(dados_json)

# dicionario =json.loads(clientes_json)
#
# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)


with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)

print(dados)