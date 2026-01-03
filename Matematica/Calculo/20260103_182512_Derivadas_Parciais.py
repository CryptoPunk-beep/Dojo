# Este script educacional aborda o conceito de derivadas parciais, que são fundamentais no cálculo multivariável. 
# As derivadas parciais permitem analisar como uma função de várias variáveis muda em relação a uma variável específica, 
# mantendo as outras constantes. Usaremos a biblioteca SymPy para manipulação simbólica e demonstrações, 
# NumPy para computação numérica, e Matplotlib para visualizações gráficas.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import init_printing

# Inicializa a impressão do SymPy para formato LaTeX
init_printing()

def derivadas_parciais(funcao, variavel):
    """
    Calcula a derivada parcial de uma função em relação a uma variável específica.
    
    :param funcao: A função simbólica da qual calcular a derivada parcial.
    :param variavel: A variável em relação à qual calcular a derivada parcial.
    :return: A derivada parcial da função em relação à variável.
    """
    return sp.diff(funcao, variavel)

# Definindo a função f(x, y) = x^2 * y + y^3
x, y = sp.symbols('x y')
funcao = x**2 * y + y**3

# Calculando as derivadas parciais
df_dx = derivadas_parciais(funcao, x)
df_dy = derivadas_parciais(funcao, y)

# Exibindo os resultados
print("Função: ", funcao)
print("Derivada parcial em relação a x: ", df_dx)
print("Derivada parcial em relação a y: ", df_dy)

# Gerando um gráfico da função
def plot_funcao(funcao, x_range, y_range):
    """
    Plota a função em um espaço 3D.
    
    :param funcao: A função a ser plotada.
    :param x_range: Intervalo para a variável x.
    :param y_range: Intervalo para a variável y.
    """
    X = np.linspace(x_range[0], x_range[1], 100)
    Y = np.linspace(y_range[0], y_range[1], 100)
    X, Y = np.meshgrid(X, Y)
    Z = sp.lambdify((x, y), funcao, 'numpy')(X, Y)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gráfico da Função f(x, y) = x^2 * y + y^3')
    plt.show()

# Plotando a função
plot_funcao(funcao, (-3, 3), (-3, 3))

# Exemplo numérico: cálculo das derivadas parciais em um ponto específico (x=1, y=2)
ponto = (1, 2)
df_dx_num = df_dx.subs({x: ponto[0], y: ponto[1]})
df_dy_num = df_dy.subs({x: ponto[0], y: ponto[1]})

print(f"Valor da derivada parcial em relação a x em (1, 2): {df_dx_num}")
print(f"Valor da derivada parcial em relação a y em (1, 2): {df_dy_num}")

# Exemplo de dados simulados para análise estatística
np.random.seed(0)
dados_x = np.random.normal(0, 1, 100)
dados_y = 2 * dados_x + np.random.normal(0, 0.5, 100)

# Cálculo da média e desvio padrão
media_x = np.mean(dados_x)
media_y = np.mean(dados_y)
desvio_x = np.std(dados_x)
desvio_y = np.std(dados_y)

print(f"Média de X: {media_x}, Desvio padrão de X: {desvio_x}")
print(f"Média de Y: {media_y}, Desvio padrão de Y: {desvio_y}")

# Visualização dos dados simulados
plt.scatter(dados_x, dados_y, alpha=0.5)
plt.title('Dados Simulados: Y em função de X')
plt.xlabel('X')
plt.ylabel('Y')
plt.axhline(0, color='gray', lw=1, ls='--')
plt.axvline(0, color='gray', lw=1, ls='--')
plt.grid()
plt.show()