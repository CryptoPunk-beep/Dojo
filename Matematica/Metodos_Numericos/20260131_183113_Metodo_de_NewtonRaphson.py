# O Método de Newton-Raphson é um método iterativo utilizado para encontrar raízes de funções. 
# A convergência quadrática do método significa que a cada iteração, a precisão da raiz encontrada 
# aumenta de forma quadrática, ou seja, o erro na iteração n+1 é proporcional ao quadrado do erro na iteração n. 
# Essa propriedade é importante pois garante que, sob certas condições, o método convergirá rapidamente para a raiz.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.optimize import newton

# Inicializa a impressão de expressões em LaTeX
sp.init_printing()

def newton_raphson(f, df, x0, tol=1e-10, max_iter=100):
    """
    Implementa o método de Newton-Raphson para encontrar raízes de uma função.
    
    Parameters:
    f : callable
        A função para a qual se deseja encontrar a raiz.
    df : callable
        A derivada da função f.
    x0 : float
        O ponto inicial para a iteração.
    tol : float
        A tolerância para a convergência.
    max_iter : int
        O número máximo de iterações permitidas.
    
    Returns:
    float
        A raiz encontrada.
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivada zero. Não pode continuar.")
        x_new = x - fx / dfx
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    raise ValueError("Número máximo de iterações alcançado.")

# Definindo uma função e sua derivada
x = sp.symbols('x')
f = sp.cos(x) - x  # Exemplo: f(x) = cos(x) - x
df = sp.diff(f, x)

# Exibindo a função e sua derivada
f_latex = sp.latex(f)
df_latex = sp.latex(df)
print(f"Função: $f(x) = {f_latex}$")
print(f"Derivada: $f'(x) = {df_latex}$")

# Convertendo para funções numéricas
f_num = sp.lambdify(x, f, 'numpy')
df_num = sp.lambdify(x, df, 'numpy')

# Encontrando a raiz usando o método de Newton-Raphson
x0 = 0.5  # Chute inicial
raiz = newton_raphson(f_num, df_num, x0)
print(f"A raiz encontrada é: {raiz:.10f}")

# Visualização da função e da raiz
x_vals = np.linspace(-1, 1, 400)
y_vals = f_num(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label='$f(x) = \cos(x) - x$', color='blue')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(raiz, color='red', lw=1, label=f'Raiz: x = {raiz:.10f}')
plt.title('Método de Newton-Raphson')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()

# Demonstração da convergência quadrática
def convergence_demo(f, df, x0, n_iter=10):
    """
    Demonstra a convergência quadrática do método de Newton-Raphson.
    
    Parameters:
    f : callable
        A função para a qual se deseja encontrar a raiz.
    df : callable
        A derivada da função f.
    x0 : float
        O ponto inicial para a iteração.
    n_iter : int
        O número de iterações para demonstrar a convergência.
    
    Returns:
    list
        Lista de erros em cada iteração.
    """
    errors = []
    x = x0
    for _ in range(n_iter):
        fx = f(x)
        dfx = df(x)
        x_new = x - fx / dfx
        error = abs(x_new - x)
        errors.append(error)
        x = x_new
    return errors

# Realizando a demonstração
errors = convergence_demo(f_num, df_num, x0)

# Visualização da convergência
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(errors) + 1), errors, marker='o', label='Erro')
plt.yscale('log')
plt.title('Demonstração da Convergência Quadrática do Método de Newton-Raphson')
plt.xlabel('Iterações')
plt.ylabel('Erro (Escala Logarítmica)')
plt.grid()
plt.legend()
plt.show()