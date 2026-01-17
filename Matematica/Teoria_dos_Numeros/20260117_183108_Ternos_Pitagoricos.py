"""
Este script explora os Ternos Pitagóricos, que são conjuntos de três números inteiros (a, b, c) que satisfazem a equação a² + b² = c². 
A parametrização completa dos ternos pitagóricos é dada por a = m² - n², b = 2mn, c = m² + n², onde m e n são inteiros positivos com m > n > 0. 
Este script utiliza SymPy para manipulação simbólica, NumPy para computação numérica e Matplotlib para visualizações.
"""

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, simplify, Eq, init_printing

# Inicializa a impressão do SymPy
init_printing()

def parametrize_pythagorean_triplets(m, n):
    """
    Gera um terno pitagórico (a, b, c) a partir de m e n.
    
    :param m: inteiro positivo, m > n
    :param n: inteiro positivo, n > 0
    :return: tupla (a, b, c)
    """
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    return a, b, c

def demonstrate_pythagorean_theorem(a, b, c):
    """
    Demonstra o teorema de Pitágoras para os valores dados de a, b e c.
    
    :param a: lado a do triângulo
    :param b: lado b do triângulo
    :param c: hipotenusa
    """
    lhs = a**2 + b**2
    rhs = c**2
    equation = Eq(lhs, rhs)
    simplified_eq = simplify(equation)
    print(f"Demonstração do Teorema de Pitágoras: {simplified_eq}")

def plot_pythagorean_triplet(a, b, c):
    """
    Plota um triângulo retângulo baseado nos lados a, b e c.
    
    :param a: lado a do triângulo
    :param b: lado b do triângulo
    :param c: hipotenusa
    """
    plt.figure()
    plt.plot([0, a], [0, 0], 'b-', label='Lado a')
    plt.plot([0, 0], [0, b], 'g-', label='Lado b')
    plt.plot([0, a], [0, b], 'r-', label='Hipotenusa c')
    plt.xlim(-1, a + 1)
    plt.ylim(-1, b + 1)
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    plt.title('Triângulo Retângulo')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

# Exemplo de uso da parametrização
m = 3
n = 2
a, b, c = parametrize_pythagorean_triplets(m, n)
print(f"Terno Pitagórico gerado: (a, b, c) = ({a}, {b}, {c})")

# Demonstração do Teorema de Pitágoras
demonstrate_pythagorean_theorem(a, b, c)

# Plotando o triângulo
plot_pythagorean_triplet(a, b, c)