"""
Os Métodos de Adams são métodos numéricos utilizados para resolver equações diferenciais ordinárias. 
Os métodos de Adams-Bashforth e Adams-Moulton são métodos multipasso que utilizam informações de 
passos anteriores para calcular a solução em um novo ponto. O método de Adams-Bashforth é explícito, 
enquanto o método de Adams-Moulton é implícito. Ambos são baseados na interpolação polinomial e na regra 
do trapézio. Neste script, vamos demonstrar esses métodos utilizando Python.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from sympy import symbols, Function, Eq, dsolve, Derivative, init_printing

# Inicializa a impressão do SymPy
init_printing()

def adams_bashforth(f, y0, t0, tn, h, n):
    """
    Implementa o método de Adams-Bashforth de ordem n.
    
    Parameters:
    f : função
        A função que define a equação diferencial.
    y0 : float
        Valor inicial da solução.
    t0 : float
        Tempo inicial.
    tn : float
        Tempo final.
    h : float
        Tamanho do passo.
    n : int
        Ordem do método (1, 2, 3, 4).
    
    Returns:
    t_values : list
        Lista de valores de tempo.
    y_values : list
        Lista de valores da solução.
    """
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    # Calcula os primeiros n-1 passos usando o método de Euler
    for i in range(1, n):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])

    # Aplica o método de Adams-Bashforth
    for i in range(n-1, len(t_values)-1):
        if n == 1:
            y_values[i+1] = y_values[i] + h * f(t_values[i], y_values[i])
        elif n == 2:
            y_values[i+1] = y_values[i] + (h/2) * (f(t_values[i], y_values[i]) + f(t_values[i-1], y_values[i-1]))
        elif n == 3:
            y_values[i+1] = y_values[i] + (h/3) * (f(t_values[i], y_values[i]) + 2*f(t_values[i-1], y_values[i-1]) + 2*f(t_values[i-2], y_values[i-2]))
        elif n == 4:
            y_values[i+1] = y_values[i] + (h/24) * (9*f(t_values[i], y_values[i]) - 37*f(t_values[i-1], y_values[i-1]) + 59*f(t_values[i-2], y_values[i-2]) - 3*f(t_values[i-3], y_values[i-3]))

    return t_values, y_values

def adams_moulton(f, y0, t0, tn, h, n):
    """
    Implementa o método de Adams-Moulton de ordem n.
    
    Parameters:
    f : função
        A função que define a equação diferencial.
    y0 : float
        Valor inicial da solução.
    t0 : float
        Tempo inicial.
    tn : float
        Tempo final.
    h : float
        Tamanho do passo.
    n : int
        Ordem do método (1, 2, 3, 4).
    
    Returns:
    t_values : list
        Lista de valores de tempo.
    y_values : list
        Lista de valores da solução.
    """
    t_values = np.arange(t0, tn + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    
    # Calcula os primeiros n-1 passos usando o método de Euler
    for i in range(1, n):
        y_values[i] = y_values[i-1] + h * f(t_values[i-1], y_values[i-1])

    # Aplica o método de Adams-Moulton
    for i in range(n-1, len(t_values)-1):
        if n == 1:
            y_values[i+1] = y_values[i] + (h/2) * (f(t_values[i+1], y_values[i+1]) + f(t_values[i], y_values[i]))
        elif n == 2:
            y_values[i+1] = y_values[i] + (h/6) * (f(t_values[i+1], y_values[i+1]) + 5*f(t_values[i], y_values[i]) + f(t_values[i-1], y_values[i-1]))
        elif n == 3:
            y_values[i+1] = y_values[i] + (h/24) * (9*f(t_values[i+1], y_values[i+1]) + 19*f(t_values[i], y_values[i]) - 5*f(t_values[i-1], y_values[i-1]) + f(t_values[i-2], y_values[i-2]))
        elif n == 4:
            y_values[i+1] = y_values[i] + (h/720) * (251*f(t_values[i+1], y_values[i+1]) + 646*f(t_values[i], y_values[i]) - 264*f(t_values[i-1], y_values[i-1]) + 12*f(t_values[i-2], y_values[i-2]) - f(t_values[i-3], y_values[i-3]))

    return t_values, y_values

# Definindo a função que descreve a EDO
t, y = symbols('t y')
f = Function('f')(t, y)
ode = Eq(Derivative(f, t), -2 * f)  # Exemplo: dy/dt = -2y
solucao = dsolve(ode, f)

# Exibindo a solução simbólica
print("Solução simbólica da EDO:")
display(solucao)

# Definindo a função para os métodos
def f_numeric(t, y):
    return -2 * y

# Parâmetros para os métodos
y0 = 1  # Condição inicial
t0 = 0  # Tempo inicial
tn = 5  # Tempo final
h = 0.1  # Tamanho do passo
n = 4    # Ordem do método

# Aplicando os métodos
t_bashforth, y_bashforth = adams_bashforth(f_numeric, y0, t0, tn, h, n)
t_moulton, y_moulton = adams_moulton(f_numeric, y0, t0, tn, h, n)

# Plotando os resultados
plt.figure(figsize=(10, 6))
plt.plot(t_bashforth, y_bashforth, label='Adams-Bashforth', marker='o')
plt.plot(t_moulton, y_moulton, label='Adams-Moulton', marker='x')
plt.title('Métodos de Adams: Bashforth e Moulton')
plt.xlabel('Tempo')
plt.ylabel('Solução y(t)')
plt.legend()
plt.grid()
plt.show()