# Este código utiliza a biblioteca NumPy para simular o processamento em lote de múltiplas amostras simultaneamente. 
# Ele gera um conjunto de dados aleatórios e aplica uma operação (soma) em cada amostra. 
# Para executar este código, instale a biblioteca NumPy com: pip install numpy

import numpy as np

# Gerar 5 amostras de dados aleatórios de 1000 elementos cada
batch_size = 5
data = np.random.rand(batch_size, 1000)

# Processar cada amostra: calcular a soma de cada linha
results = np.sum(data, axis=1)

# Imprimir os resultados
for i, result in enumerate(results):
    print(f"Soma da amostra {i + 1}: {result:.2f}")