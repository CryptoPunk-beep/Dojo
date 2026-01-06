# Este código simula a validação anônima de uma nota digital usando o conceito de Chaumian Cash. 
# Ele gera uma nota digital, a assina e valida a assinatura sem revelar a identidade do portador. 
# Para executar, não são necessárias bibliotecas externas, apenas o Python padrão.

import hashlib
import random

class DigitalNote:
    def __init__(self, value):
        self.value = value
        self.serial_number = random.randint(1000, 9999)
        self.signature = self.sign()

    def sign(self):
        # Simula a assinatura da nota digital
        return hashlib.sha256(f"{self.value}{self.serial_number}".encode()).hexdigest()

    def validate(self, signature):
        # Valida a assinatura da nota digital
        return signature == self.sign()

# Criando uma nota digital de valor 100
note = DigitalNote(100)

# Exibindo informações da nota digital
print(f"Nota Digital: {note.value}, Serial: {note.serial_number}, Assinatura: {note.signature}")

# Validando a assinatura
is_valid = note.validate(note.signature)
print(f"Validação da assinatura: {'Válida' if is_valid else 'Inválida'}")