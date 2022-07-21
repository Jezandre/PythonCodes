from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luiz otávio', data=data_atual)

print(corpo_msg)
