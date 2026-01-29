"""
O Jacobiano é uma matriz que contém todas as derivadas parciais de uma função vetorial. Em integrais múltiplas, ele é crucial para a mudança de variáveis, pois ajusta a medida do espaço quando se transforma de um sistema de coordenadas para outro. O determinante do Jacobiano fornece o fator de escala necessário para a integração em novas variáveis. Neste script, usaremos o SymPy para manipulação simbólica, o NumPy para computação numérica e o Matplotlib para visualizações gráficas.
"""

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import dblquad

# Inicializa a impressão do SymPy
sp.init_printing()

def jacobiano(funcs, vars):
    """
    Calcula o Jacobiano de um conjunto de funções em relação a um conjunto de variáveis.

    Parameters:
    funcs (list): Lista de funções.
    vars (list): Lista de variáveis.

    Returns:
    sympy.Matrix: Matriz Jacobiana.
    """
    J = sp.Matrix([[sp.diff(f, v) for v in vars] for f in funcs])
    return J

def exemplo_jacobiano():
    """
    Demonstra a mudança de variáveis em integrais múltiplas usando o Jacobiano.
    """
    # Definindo as variáveis
    x, y = sp.symbols('x y')
    
    # Definindo as funções de mudança de variáveis
    u = x**2 + y**2
    v = sp.atan2(y, x)
    
    # Calculando o Jacobiano
    funcs = [u, v]
    vars = [x, y]
    J = jacobiano(funcs, vars)
    
    # Exibindo o Jacobiano
    display(J)

    # Calculando o determinante do Jacobiano
    det_J = J.det()
    display(det_J)

    return det_J

def integrar_com_mudanca_de_variaveis():
    """
    Realiza uma integral dupla utilizando a mudança de variáveis e o Jacobiano.
    """
    # Definindo os limites da integral
    r_min, r_max = 0, 1
    theta_min, theta_max = 0, 2 * np.pi

    # Função a ser integrada
    integrando = lambda r, theta: r**2 * np.sin(theta)

    # Calculando a integral usando a mudança de variáveis
    resultado, erro = dblquad(integrando, theta_min, theta_max, lambda theta: r_min, lambda theta: r_max)
    
    print(f"Resultado da integral: {resultado:.4f}, Erro estimado: {erro:.4e}")

def visualizar_mudanca_de_variaveis():
    """
    Visualiza a mudança de variáveis de coordenadas cartesianas para coordenadas polares.
    """
    # Criando um grid de pontos
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    
    # Calculando U e V
    U = X**2 + Y**2
    V = np.arctan2(Y, X)

    # Plotando os resultados
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.title('Coordenadas Cartesianas')
    plt.scatter(X, Y, c='blue', alpha=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')

    plt.subplot(1, 2, 2)
    plt.title('Coordenadas Polares (U, V)')
    plt.scatter(U, V, c='red', alpha=0.5)
    plt.xlabel('U')
    plt.ylabel('V')
    plt.axis('equal')

    plt.tight_layout()
    plt.show()

# Executando as funções
det_J = exemplo_jacobiano()
integrar_com_mudanca_de_variaveis()
visualizar_mudanca_de_variaveis()