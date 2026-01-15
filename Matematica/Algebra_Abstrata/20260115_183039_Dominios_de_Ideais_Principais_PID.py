# Este script explora a caracterização de Domínios de Ideais Principais (PID) na Álgebra Abstrata. 
# Um domínio de ideais principais é um anel em que todo ideal é gerado por um único elemento. 
# Usaremos a biblioteca SymPy para manipulação simbólica e visualização de conceitos, 
# além de exemplos numéricos para ilustrar a teoria.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Inicializa a impressão de resultados em LaTeX
sp.init_printing()

def is_pid(ring):
    """
    Verifica se um anel é um domínio de ideais principais (PID).
    
    Parameters:
    ring (list): Lista de elementos do anel.

    Returns:
    bool: True se o anel é um PID, False caso contrário.
    """
    for ideal in generate_ideals(ring):
        if len(ideal) > 1:
            return False
    return True

def generate_ideals(ring):
    """
    Gera todos os ideais de um anel dado.
    
    Parameters:
    ring (list): Lista de elementos do anel.

    Returns:
    list: Lista de ideais gerados.
    """
    ideals = []
    for element in ring:
        ideal = {element * r for r in ring}
        ideals.append(ideal)
    return ideals

def demonstrate_pid():
    """
    Demonstra a caracterização de um PID usando um exemplo numérico.
    """
    # Exemplo: O anel Z (números inteiros)
    Z = list(range(-10, 11))  # Números inteiros de -10 a 10
    ideals = generate_ideals(Z)
    
    print("Ideais gerados em Z:")
    for i, ideal in enumerate(ideals):
        print(f"Ideal gerado por {Z[i]}: {ideal}")
    
    is_pid_result = is_pid(Z)
    print(f"\nO anel Z é um PID? {is_pid_result}")

def visualize_ideals():
    """
    Visualiza a estrutura dos ideais em um anel simples.
    """
    # Exemplo: Ideais gerados por 2 em Z
    Z = np.arange(-10, 11)
    ideal_2 = np.array([2 * n for n in Z])
    
    plt.figure(figsize=(10, 5))
    plt.plot(Z, np.zeros_like(Z), 'ro', label='Z')
    plt.plot(ideal_2, np.zeros_like(ideal_2), 'bo', label='Ideal gerado por 2')
    plt.title('Visualização dos Ideais em Z')
    plt.xlabel('Elementos do Anel Z')
    plt.ylabel('Ideais')
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.legend()
    plt.grid()
    plt.show()

# Executa a demonstração e visualização
demonstrate_pid()
visualize_ideals()