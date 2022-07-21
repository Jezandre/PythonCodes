from string import Template
from datetime import datetime
from dado_email import meu_email, minha_senha


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luiz otávio', data=data_atual)
msg = MIMEMultipart()
msg['from'] = 'Jezandre do Nascimento Tiago'
msg['to'] = 'jezandre_tiago@hotmail.com'
msg['subject'] = 'Atenção este é um e-mail de testes.'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('c:\CursoPython\Aula130-CriarE-mail\Imagem.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado')
        print('E-mail:', e)

print(corpo)
