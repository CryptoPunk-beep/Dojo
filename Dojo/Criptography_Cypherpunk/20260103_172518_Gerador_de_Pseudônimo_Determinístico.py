# Este código gera um pseudônimo determinístico e um avatar a partir de uma semente fornecida pelo usuário. 
# O pseudônimo é criado combinando palavras aleatórias, enquanto o avatar é gerado a partir de um hash da semente. 
# Para executar, não são necessárias bibliotecas externas. 
# O código utiliza apenas a biblioteca padrão do Python.

import random
import hashlib

def gerar_pseudonimo(seed):
    random.seed(seed)
    nomes = ["Lobo", "Falcão", "Tigre", "Urso", "Serpente"]
    adjetivos = ["Sábio", "Valente", "Astuto", "Feroz", "Misterioso"]
    
    nome = random.choice(nomes)
    adjetivo = random.choice(adjetivos)
    pseudonimo = f"{adjetivo} {nome}"
    
    avatar = hashlib.sha256(seed.encode()).hexdigest()[:8]  # Gera um hash e pega os primeiros 8 caracteres
    
    return pseudonimo, avatar

# Exemplo de uso
seed = "minha_semente_unica"
pseudonimo, avatar = gerar_pseudonimo(seed)
print(f"Pseudônimo: {pseudonimo}, Avatar: {avatar}")