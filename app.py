import os
import smtplib
from email.message import EmailMessage
from senhas import senha
import messages

#Configurar Email e senha

EMAIL_ADDRESS = 'email'
EMAIL_PASSWORD = senha

#Criar um e-mail
msg = EmailMessage()
msg['Subject'] = 'no-reply'
msg['From'] = 'email'
msg['To'] = 'destinatario'
msg.set_content(messages.Mensagem_2)

#enviar o email
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)