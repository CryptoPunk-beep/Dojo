# Este código utiliza a biblioteca Qiskit para estimar a fase de um operador unitário, que é um problema fundamental em computação quântica. 
# A estimativa de fase permite encontrar autovalores de operadores unitários, o que é crucial em algoritmos quânticos como o de Shor. 
# Para executar este código, instale a biblioteca Qiskit com o comando: pip install qiskit

from qiskit import QuantumCircuit, Aer, execute
import numpy as np

# Definindo o operador unitário U
theta = np.pi / 4
U = QuantumCircuit(1)
U.ry(theta, 0)

# Criando o circuito para estimativa de fase
qc = QuantumCircuit(2, 1)
qc.h(0)  # Preparar qubit de fase
qc.append(U.to_gate(label='U'), [0])  # Aplicar U
qc.h(0)  # Aplicar Hadamard novamente
qc.measure(0, 0)  # Medir o qubit de fase

# Executar o circuito
simulator = Aer.get_backend('aer_simulator')
result = execute(qc, simulator).result()
counts = result.get_counts(qc)

# Imprimir os resultados
print("Resultados da medição:", counts)