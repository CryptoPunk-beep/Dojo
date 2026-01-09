# O Teorema de Ptolomeu afirma que, para um quadrilátero cíclico (um quadrilátero cujos vértices estão em um círculo),
# a soma dos produtos das suas diagonais é igual ao produto dos seus lados opostos. 
# Matematicamente, se ABCD é um quadrilátero cíclico, então:
# AC * BD = AB * CD + AD * BC
# Este script irá demonstrar o teorema usando SymPy para manipulação simbólica e Matplotlib para visualização.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, init_printing
import sympy as sp

# Inicializa a impressão do SymPy para LaTeX
init_printing()

def ptolomeu_theorem(a, b, c, d):
    """
    Verifica o Teorema de Ptolomeu para um quadrilátero cíclico dado os lados e as diagonais.

    :param a: Lado AB
    :param b: Lado BC
    :param c: Lado CD
    :param d: Lado DA
    :return: Resultado da verificação do teorema
    """
    AC, BD = symbols('AC BD')
    
    # Equação do Teorema de Ptolomeu
    eq = Eq(AC * BD, a * c + b * d)
    
    return eq

def demonstrate_ptolomeu(a, b, c, d):
    """
    Demonstra o Teorema de Ptolomeu simbolicamente e numericamente.

    :param a: Lado AB
    :param b: Lado BC
    :param c: Lado CD
    :param d: Lado DA
    """
    # Demonstração simbólica
    eq = ptolomeu_theorem(a, b, c, d)
    print("Demonstração simbólica do Teorema de Ptolomeu:")
    display(eq)

    # Exemplo numérico
    # Definindo valores para as diagonais
    AC_value = 5
    BD_value = 7

    # Substituindo os valores na equação
    result = eq.subs({symbols('AC'): AC_value, symbols('BD'): BD_value})
    print("\nVerificação numérica:")
    print(f"Para AC = {AC_value} e BD = {BD_value}, temos:")
    print(f"{result.lhs} = {result.rhs}")

def plot_quadrilateral(a, b, c, d):
    """
    Plota um quadrilátero cíclico e suas diagonais.

    :param a: Lado AB
    :param b: Lado BC
    :param c: Lado CD
    :param d: Lado DA
    """
    # Coordenadas dos vértices do quadrilátero
    A = np.array([0, 0])
    B = np.array([a, 0])
    C = np.array([a + b * np.cos(np.pi/4), b * np.sin(np.pi/4)])
    D = np.array([d * np.cos(np.pi/4), d * np.sin(np.pi/4)])

    # Criando a figura
    plt.figure(figsize=(8, 8))
    plt.plot([A[0], B[0]], [A[1], B[1]], 'ro-')
    plt.plot([B[0], C[0]], [B[1], C[1]], 'ro-')
    plt.plot([C[0], D[0]], [C[1], D[1]], 'ro-')
    plt.plot([D[0], A[0]], [D[1], A[1]], 'ro-')
    
    # Diagonais
    plt.plot([A[0], C[0]], [A[1], C[1]], 'b--', label='Diagonal AC')
    plt.plot([B[0], D[0]], [B[1], D[1]], 'g--', label='Diagonal BD')

    # Adicionando rótulos
    plt.text(A[0], A[1], 'A', fontsize=12, ha='right')
    plt.text(B[0], B[1], 'B', fontsize=12, ha='left')
    plt.text(C[0], C[1], 'C', fontsize=12, ha='left')
    plt.text(D[0], D[1], 'D', fontsize=12, ha='right')

    plt.xlim(-1, a + b + 1)
    plt.ylim(-1, b + 1)
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.title('Quadrilátero Cíclico')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend()
    plt.grid()
    plt.show()

# Exemplo de uso
a = 3  # Lado AB
b = 4  # Lado BC
c = 5  # Lado CD
d = 2  # Lado DA

demonstrate_ptolomeu(a, b, c, d)
plot_quadrilateral(a, b, c, d)