# Este script explora a área de superfície de revolução, um conceito fundamental em cálculo.
# A área de superfície de um sólido de revolução pode ser obtida integrando a função que descreve
# a curva que está sendo girada em torno de um eixo. Usaremos SymPy para derivar a fórmula e 
# Matplotlib para visualizar os sólidos gerados. O exemplo incluirá a curva y = f(x) = x^2 
# girando em torno do eixo x.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import init_printing

# Inicializa a impressão do SymPy para LaTeX
init_printing()

def area_superficie_revolucao(funcao, limite_inferior, limite_superior):
    """
    Calcula a área da superfície de revolução de uma função em torno do eixo x.

    Parameters:
    funcao (sympy function): A função a ser girada.
    limite_inferior (float): Limite inferior da integração.
    limite_superior (float): Limite superior da integração.

    Returns:
    sympy expression: Área da superfície de revolução.
    """
    x = sp.symbols('x')
    # Derivada da função
    derivada = sp.diff(funcao, x)
    # Fórmula da área de superfície de revolução
    area = 2 * sp.pi * sp.integrate(funcao * sp.sqrt(1 + derivada**2), (x, limite_inferior, limite_superior))
    return area

# Definindo a função y = x^2
x = sp.symbols('x')
funcao = x**2

# Calculando a área da superfície de revolução de y = x^2 de 0 a 1
limite_inferior = 0
limite_superior = 1
area = area_superficie_revolucao(funcao, limite_inferior, limite_superior)

# Exibindo o resultado em LaTeX
print("Área da superfície de revolução de y = x^2 de 0 a 1:")
sp.pprint(area)

# Visualização da curva e da superfície de revolução
def plot_superficie_revolucao(funcao, limite_inferior, limite_superior):
    """
    Plota a curva e a superfície de revolução.

    Parameters:
    funcao (sympy function): A função a ser girada.
    limite_inferior (float): Limite inferior da integração.
    limite_superior (float): Limite superior da integração.
    """
    x_vals = np.linspace(limite_inferior, limite_superior, 100)
    y_vals = funcao.evalf(subs={x: x_vals})

    # Plotando a curva
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Curva: $y = x^2$', color='blue')
    plt.fill_between(x_vals, y_vals, color='blue', alpha=0.1)

    # Visualizando a superfície de revolução
    theta = np.linspace(0, 2 * np.pi, 100)
    X, Theta = np.meshgrid(x_vals, theta)
    Y = X**2
    Z = Y * np.cos(Theta)
    Y_surf = Y * np.sin(Theta)

    # Plotando a superfície
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y_surf, Z, alpha=0.5, color='cyan', edgecolor='none')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Superfície de Revolução de $y = x^2$')
    plt.legend()
    plt.show()

# Chamando a função para plotar a superfície de revolução
plot_superficie_revolucao(funcao, limite_inferior, limite_superior)