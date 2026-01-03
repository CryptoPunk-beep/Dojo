# Este código demonstra a diferença entre complexidade de tempo O(n) e O(n²). 
# A função O(n) realiza uma operação linear, enquanto a função O(n²) realiza 
# operações quadráticas em relação ao tamanho da entrada. Vamos comparar o tempo 
# de execução de ambas as funções para diferentes tamanhos de entrada.

import time

def funcao_O_n(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma

def funcao_O_n2(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += i + j
    return soma

tamanhos = [10, 100, 200]

for tamanho in tamanhos:
    inicio = time.time()
    funcao_O_n(tamanho)
    tempo_O_n = time.time() - inicio
    
    inicio = time.time()
    funcao_O_n2(tamanho)
    tempo_O_n2 = time.time() - inicio
    
    print(f"Tamanho: {tamanho} - O(n): {tempo_O_n:.6f}s, O(n²): {tempo_O_n2:.6f}s")