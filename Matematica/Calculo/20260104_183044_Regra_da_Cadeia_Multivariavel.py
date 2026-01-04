# A Regra da Cadeia Multivariável é uma ferramenta fundamental em cálculo que permite calcular a derivada de funções compostas que dependem de múltiplas variáveis. 
# Quando temos uma função que é composta por outras funções, a regra da cadeia nos ajuda a entender como as mudanças em uma variável afetam a função final. 
# Neste script, utilizaremos a biblioteca SymPy para manipulação simbólica e NumPy para cálculos numéricos. 
# Também criaremos visualizações usando Matplotlib para ilustrar as relações entre as variáveis.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import init_printing

# Inicializa a impressão em LaTeX
init_printing()

def regra_da_cadeia_multivariavel(funcao, variaveis):
    """
    Calcula a derivada de uma função multivariável usando a regra da cadeia.

    :param funcao: A função a ser derivada.
    :param variaveis: Lista de variáveis independentes.
    :return: A derivada da função em relação às variáveis.
    """
    gradiente = [sp.diff(funcao, var) for var in variaveis]
    return gradiente

# Definindo as variáveis
x, y = sp.symbols('x y')

# Definindo a função multivariável
f = sp.sin(x**2 + y**2)

# Calculando a derivada usando a regra da cadeia
gradiente_f = regra_da_cadeia_multivariavel(f, [x, y])
display(gradiente_f)

# Exemplo numérico
def exemplo_numerico(funcao, ponto):
    """
    Avalia a função e seu gradiente em um ponto específico.

    :param funcao: A função a ser avaliada.
    :param ponto: Um dicionário com valores das variáveis.
    :return: O valor da função e o gradiente no ponto.
    """
    valor_funcao = funcao.subs(ponto)
    gradiente = [g.evalf(subs=ponto) for g in regra_da_cadeia_multivariavel(funcao, [x, y])]
    return valor_funcao, gradiente

# Avaliando a função e seu gradiente no ponto (1, 1)
ponto = {x: 1, y: 1}
valor_funcao, gradiente = exemplo_numerico(f, ponto)
print(f"Valor da função em {ponto}: {valor_funcao}")
print(f"Gradiente em {ponto}: {gradiente}")

# Visualização da função
def plotar_funcao(funcao, x_range, y_range):
    """
    Plota a função em um gráfico 3D.

    :param funcao: A função a ser plotada.
    :param x_range: Intervalo para a variável x.
    :param y_range: Intervalo para a variável y.
    """
    x_vals = np.linspace(x_range[0], x_range[1], 100)
    y_vals = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(x_vals, y_vals)
    Z = np.array([[funcao.subs({x: x_val, y: y_val}) for x_val in x_vals] for y_val in y_vals], dtype=float)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X, Y)')
    ax.set_title('Gráfico da Função Multivariável')
    plt.show()

# Plotando a função
plotar_funcao(f, (-2, 2), (-2, 2))