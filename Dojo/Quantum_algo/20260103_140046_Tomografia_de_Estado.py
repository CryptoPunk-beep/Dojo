# Este código utiliza a biblioteca Qiskit para realizar a tomografia de estado quântico, que é o processo de reconstruir um estado quântico a partir de medições. Para rodar este código, instale o Qiskit usando: pip install qiskit. O exemplo cria um estado quântico, realiza medições e reconstrói a matriz de densidade correspondente ao estado medido.

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector
import numpy as np

# Criar um circuito quântico com um qubit
qc = QuantumCircuit(1)
qc.h(0)  # Aplica uma porta Hadamard para criar um estado superposto
qc.measure_all()

# Simular o circuito
backend = Aer.get_backend('qasm_simulator')
job = execute(qc, backend, shots=1024)
result = job.result()
counts = result.get_counts()

# Exibir resultados das medições
print("Resultados das medições:", counts)

# Reconstruir a matriz de densidade
p0 = counts.get('0', 0) / 1024
p1 = counts.get('1', 0) / 1024
density_matrix = np.array([[p0, 0], [0, p1]])

print("Matriz de densidade reconstruída:")
print(density_matrix)

# Visualizar o estado no Bloch Sphere
statevector = np.sqrt([p0, p1])
plot_bloch_multivector(statevector)