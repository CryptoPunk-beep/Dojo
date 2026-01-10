# Este script explora o conceito de equações de congruência da forma ax ≡ b (mod m).
# As equações de congruência são fundamentais na teoria dos números e têm aplicações em criptografia, algoritmos e resolução de problemas discretos.
# Vamos usar a biblioteca SymPy para manipulação simbólica e demonstrações, NumPy para computação numérica, e Matplotlib para visualizações.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, init_printing, mod_inverse

# Inicializa a impressão em LaTeX
init_printing()

def solve_congruence(a, b, m):
    """
    Resolve a equação de congruência ax ≡ b (mod m) e retorna a solução.
    
    Parameters:
    a (int): Coeficiente da variável x.
    b (int): Termo constante.
    m (int): Módulo da congruência.
    
    Returns:
    list: Lista de soluções para a equação de congruência.
    """
    x = symbols('x')
    # Cria a equação de congruência
    congruence_eq = Eq(a * x % m, b % m)
    
    # Resolve a equação
    solutions = []
    for k in range(m):
        if (a * k) % m == b % m:
            solutions.append(k)
    
    return solutions

def demonstrate_congruence(a, b, m):
    """
    Demonstra a resolução da equação de congruência ax ≡ b (mod m) usando SymPy.
    
    Parameters:
    a (int): Coeficiente da variável x.
    b (int): Termo constante.
    m (int): Módulo da congruência.
    """
    x = symbols('x')
    congruence_eq = Eq(a * x % m, b % m)
    
    # Exibe a equação
    print("Equação de Congruência:")
    display(congruence_eq)

    # Resolve a equação simbolicamente
    solution = solve(congruence_eq, x)
    print("Solução simbólica:")
    display(solution)

def plot_congruence(a, b, m):
    """
    Plota a função y = ax (mod m) e a linha y = b (mod m) para visualizar as soluções.
    
    Parameters:
    a (int): Coeficiente da variável x.
    b (int): Termo constante.
    m (int): Módulo da congruência.
    """
    x_values = np.arange(0, m)
    y_values = (a * x_values) % m
    b_line = np.full_like(x_values, b % m)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, label=f'y = {a}x (mod {m})', marker='o')
    plt.plot(x_values, b_line, label=f'y = {b} (mod {m})', linestyle='--', color='red')
    plt.title('Visualização da Equação de Congruência')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xticks(np.arange(0, m))
    plt.yticks(np.arange(0, m))
    plt.grid()
    plt.legend()
    plt.show()

# Exemplo de uso
a = 3
b = 4
m = 7

# Resolvendo a equação de congruência
solutions = solve_congruence(a, b, m)
print(f"Soluções para a equação {a}x ≡ {b} (mod {m}): {solutions}")

# Demonstração da equação de congruência
demonstrate_congruence(a, b, m)

# Plotando a função
plot_congruence(a, b, m)

def solve_system_of_congruences(congruences):
    """
    Resolve um sistema de equações de congruência usando o Teorema Chinês dos Restos.
    
    Parameters:
    congruences (list of tuples): Lista de tuplas (a, b, m) representando as equações ax ≡ b (mod m).
    
    Returns:
    int: A solução do sistema de congruências.
    """
    from sympy.ntheory.modular import solve_congruence

    return solve_congruence(*congruences)

# Exemplo de sistema de congruências
congruences = [(2, 3), (3, 4), (2, 5)]
solution_system = solve_system_of_congruences(congruences)
print(f"Solução do sistema de congruências: {solution_system}")