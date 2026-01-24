# Este código simula um sistema de multisig onde uma transação requer N de M assinaturas para ser considerada válida. 
# Vamos definir 3 chaves públicas e exigir 2 assinaturas para aprovar a transação. 
# O código verifica se as assinaturas necessárias estão presentes. 
# Para rodar, não são necessárias bibliotecas externas.

def verificar_multisig(assinaturas, chaves_publicas, n):
    return len(set(assinaturas) & set(chaves_publicas)) >= n

# Definindo chaves públicas e assinaturas
chaves_publicas = ['chave1', 'chave2', 'chave3']
assinaturas = ['chave1', 'chave2']  # Assinaturas coletadas
n = 2  # Número mínimo de assinaturas necessárias

# Verificando se a transação é válida
if verificar_multisig(assinaturas, chaves_publicas, n):
    print("Transação válida: assinaturas suficientes.")
else:
    print("Transação inválida: assinaturas insuficientes.")