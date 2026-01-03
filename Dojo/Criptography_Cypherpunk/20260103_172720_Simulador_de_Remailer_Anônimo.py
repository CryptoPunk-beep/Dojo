# Este código simula um remailer anônimo que remove metadados do remetente antes de reenviar uma mensagem. 
# Ele utiliza a biblioteca 'email' para manipular mensagens de e-mail. 
# Para instalar a biblioteca necessária, use: pip install secure-smtplib
# O código demonstra como criar uma mensagem anônima e reenviá-la sem informações do remetente.

import smtplib
from email.mime.text import MIMEText

def remailer_anônimo(remetente, destinatario, mensagem):
    # Cria uma mensagem de e-mail
    msg = MIMEText(mensagem)
    msg['Subject'] = 'Mensagem Anônima'
    msg['From'] = 'anon@remailer.com'  # Remetente anônimo
    msg['To'] = destinatario

    # Simula o envio do e-mail
    print(f"Enviando e-mail para {destinatario}...")
    print(f"Conteúdo:\n{msg.as_string()}\n")
    
# Exemplo de uso
remetente = 'usuario@exemplo.com'
destinatario = 'destinatario@exemplo.com'
mensagem = 'Esta é uma mensagem anônima.'

remailer_anônimo(remetente, destinatario, mensagem)