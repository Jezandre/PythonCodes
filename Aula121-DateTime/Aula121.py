from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays, monthrange

setlocale(LC_ALL, 'pt_BR.utf-8')

# Sexta, 13 de junho e 2018

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))
formatacao1 = dt.strftime('%A, %d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y  %H:%M:%S')
print(formatacao1)
print(formatacao2)
print(mes_atual, mdays[mes_atual])
print(monthrange(2020, 2))