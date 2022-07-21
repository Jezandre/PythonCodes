"""
Trabalhar com data e hora em Python
"""
from datetime import datetime, timedelta

"""formatar data """

# data = datetime(2019, 4, 20, 10, 53, 20)
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

""" criar data a partir de uma string"""

# data = datetime.strptime('20/04/2019', '%d/%m/%Y')
# print(data.timestamp())

"""formatar do timestamp """

# data = datetime.fromtimestamp(1555729200.0)
# print(data)

"""contas simples com horas"""
# data = datetime.strptime('20/04/1987 20:00:00','%d/%m/%Y %H:%M:%S')
# data = data + timedelta(seconds=59*60)
#
# print(data.strftime('%d/%m/%Y %H:%M:%S'))

"""Comparar datas, contas"""
d1 = datetime.strptime('20/04/1987 20:00:00','%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00','%d/%m/%Y %H:%M:%S')

dif =d2-d1

print(d1.time())