# Este código gera senhas descartáveis baseadas em tempo (TOTP - Time-based One-Time Password). 
# Para executar este código, você precisará instalar a biblioteca `pyotp`. 
# Você pode instalá-la usando o comando: pip install pyotp
# O código irá gerar e imprimir uma senha TOTP a cada execução.

import pyotp
import time

# Cria um objeto TOTP com uma chave secreta
secret = 'JBSWY3DPEHPK3PXP'  # chave secreta base32
totp = pyotp.TOTP(secret)

# Gera e imprime a senha TOTP atual
print("Senha TOTP atual:", totp.now())

# Para demonstrar a mudança de senha após 30 segundos
print("Aguarde 30 segundos para a próxima senha...")
time.sleep(30)
print("Nova senha TOTP:", totp.now())