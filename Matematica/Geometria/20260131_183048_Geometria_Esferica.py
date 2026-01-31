# Este script explora a geometria esférica, focando em triângulos esféricos e o conceito de excesso angular.
# Na geometria esférica, a soma dos ângulos internos de um triângulo é maior que 180 graus.
# O excesso angular é definido como a soma dos ângulos menos 180 graus. 
# Usaremos SymPy para manipulação simbólica, NumPy para cálculos numéricos e Matplotlib para visualizações.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializa a impressão do SymPy
sp.init_printing()

def excesso_angular(a, b, c):
    """
    Calcula o excesso angular de um triângulo esférico dado os ângulos a, b e c em radianos.
    
    Parameters:
    a (float): ângulo A em radianos
    b (float): ângulo B em radianos
    c (float): ângulo C em radianos
    
    Returns:
    float: excesso angular
    """
    return (a + b + c) - np.pi

def demonstracao_excesso_angular():
    """
    Demonstra o cálculo do excesso angular usando SymPy.
    """
    # Definindo os ângulos
    A, B, C = sp.symbols('A B C')
    
    # Soma dos ângulos
    soma_angulos = A + B + C
    
    # Excesso angular
    excesso = soma_angulos - sp.pi
    
    # Exibindo a demonstração
    sp.pprint(excesso)

def visualizar_triangulo_esferico(angulos):
    """
    Visualiza um triângulo esférico dado os ângulos em radianos.
    
    Parameters:
    angulos (list): lista de ângulos [A, B, C] em radianos
    """
    A, B, C = angulos
    
    # Cálculo do excesso angular
    excesso = excesso_angular(A, B, C)
    
    # Criando o gráfico
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Coordenadas dos vértices do triângulo esférico
    x = [np.sin(A), np.sin(B), np.sin(C), np.sin(A)]
    y = [np.cos(A), np.cos(B), np.cos(C), np.cos(A)]
    z = [0, 0, 0, 0]
    
    ax.plot(x, y, z, marker='o')
    ax.set_title(f'Triângulo Esférico com ângulos A={A:.2f}, B={B:.2f}, C={C:.2f}\nExcesso Angular={excesso:.2f} rad')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    plt.show()

# Exemplos numéricos
A = np.radians(100)  # ângulo A em graus
B = np.radians(80)   # ângulo B em graus
C = np.radians(50)   # ângulo C em graus

# Cálculo do excesso angular
excesso = excesso_angular(A, B, C)
print(f'Excesso Angular: {excesso:.4f} rad')

# Demonstração simbólica
demonstracao_excesso_angular()

# Visualização do triângulo esférico
visualizar_triangulo_esferico([A, B, C])