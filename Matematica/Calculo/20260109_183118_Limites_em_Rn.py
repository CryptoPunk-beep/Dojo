# Este script explora o conceito de limites em R^n, focando na análise de limites que dependem do caminho
# e na demonstração da não existência de limites. Usaremos SymPy para manipulação simbólica e
# visualizações com Matplotlib para ilustrar os conceitos.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Inicializa a impressão do SymPy para LaTeX
sp.init_printing()

def limite_exemplo(x, y):
    """
    Função que calcula o limite da expressão (x^2 * y) / (x^2 + y^2) quando (x, y) se aproxima de (0, 0).
    
    Args:
        x (float): Valor da coordenada x.
        y (float): Valor da coordenada y.
    
    Returns:
        float: O valor do limite.
    """
    return (x**2 * y) / (x**2 + y**2)

def calcular_limite(caminho):
    """
    Calcula o limite da função em diferentes caminhos.
    
    Args:
        caminho (str): O caminho a ser seguido (ex: 'x=0', 'y=0', 'y=x', 'y=x^2').
    
    Returns:
        float: O valor do limite para o caminho especificado.
    """
    x, y = sp.symbols('x y')
    if caminho == 'y=0':
        limite = limite_exemplo(x, 0)
    elif caminho == 'x=0':
        limite = limite_exemplo(0, y)
    elif caminho == 'y=x':
        limite = limite_exemplo(x, x)
    elif caminho == 'y=x^2':
        limite = limite_exemplo(x, x**2)
    else:
        raise ValueError("Caminho inválido.")
    
    return limite.simplify()

# Cálculo do limite em diferentes caminhos
caminhos = ['y=0', 'x=0', 'y=x', 'y=x^2']
resultados = {caminho: calcular_limite(caminho) for caminho in caminhos}

# Exibindo os resultados
for caminho, resultado in resultados.items():
    display(sp.Eq(sp.limit(limite_exemplo(sp.symbols('x'), sp.symbols('y')), (0, 0)), resultado))

def plot_limite():
    """
    Plota a função (x^2 * y) / (x^2 + y^2) em um gráfico 3D para visualizar o comportamento
    da função em torno do ponto (0, 0).
    """
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = limite_exemplo(X, Y)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title('Superfície da função (x^2 * y) / (x^2 + y^2)')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

plot_limite()