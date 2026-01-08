# Este código demonstra como criar um circuito quântico básico usando o framework Cirq do Google. 
# Ele cria um qubit, aplica uma porta Hadamard para criar superposição e mede o resultado.
# Para executar este código, instale a biblioteca Cirq com o comando: pip install cirq

import cirq

# Criação de um qubit
qubit = cirq.GridQubit(0, 0)

# Criação de um circuito quântico
circuit = cirq.Circuit(
    cirq.H(qubit),  # Porta Hadamard
    cirq.measure(qubit)  # Medida do qubit
)

# Simulação do circuito
simulator = cirq.Simulator()
result = simulator.run(circuit)

# Impressão do resultado
print("Resultado da medição:", result)