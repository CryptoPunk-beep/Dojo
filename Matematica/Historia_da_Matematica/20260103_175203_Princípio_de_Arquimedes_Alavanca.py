# O Princípio de Arquimedes, também conhecido como o princípio da alavanca, é um dos conceitos fundamentais da física e da matemática. 
# Arquimedes de Siracusa (287 a.C. - 212 a.C.) foi um matemático e inventor grego que formulou este princípio, que afirma que um corpo imerso em um fluido 
# experimenta uma força de empuxo igual ao peso do fluido deslocado. Neste script, vamos demonstrar matematicamente o equilíbrio em uma alavanca, 
# utilizando métodos originais e comparando com métodos modernos.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, init_printing

# Inicializa a impressão do SymPy para LaTeX
init_printing()

def equilibrio_alavanca(peso1, distancia1, peso2, distancia2):
    """
    Calcula o equilíbrio de uma alavanca usando o princípio de Arquimedes.
    
    Parâmetros:
    peso1 (float): Peso do primeiro objeto.
    distancia1 (float): Distância do primeiro objeto ao ponto de apoio.
    peso2 (float): Peso do segundo objeto.
    distancia2 (float): Distância do segundo objeto ao ponto de apoio.
    
    Retorna:
    bool: Verdadeiro se a alavanca está em equilíbrio, Falso caso contrário.
    """
    # Condição de equilíbrio: peso1 * distância1 = peso2 * distância2
    return peso1 * distancia1 == peso2 * distancia2

def demonstracao_equilibrio(peso1, distancia1, peso2, distancia2):
    """
    Demonstra a condição de equilíbrio de uma alavanca usando SymPy.
    
    Parâmetros:
    peso1 (float): Peso do primeiro objeto.
    distancia1 (float): Distância do primeiro objeto ao ponto de apoio.
    peso2 (float): Peso do segundo objeto.
    distancia2 (float): Distância do segundo objeto ao ponto de apoio.
    """
    x1, d1, x2, d2 = symbols('x1 d1 x2 d2')
    eq = Eq(x1 * d1, x2 * d2)
    sol = solve(eq.subs({x1: peso1, d1: distancia1, x2: peso2, d2: distancia2}), x2)
    
    print(f"A condição de equilíbrio é: {peso1} * {distancia1} = {peso2} * {distancia2}")
    print(f"Para que a alavanca esteja em equilíbrio, o peso2 deve ser: {sol[0]}")

def visualizacao_alavanca(peso1, distancia1, peso2, distancia2):
    """
    Visualiza a alavanca em equilíbrio com Matplotlib.
    
    Parâmetros:
    peso1 (float): Peso do primeiro objeto.
    distancia1 (float): Distância do primeiro objeto ao ponto de apoio.
    peso2 (float): Peso do segundo objeto.
    distancia2 (float): Distância do segundo objeto ao ponto de apoio.
    """
    plt.figure(figsize=(10, 5))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    # Ponto de apoio
    plt.plot(0, 0, 'ro', label='Ponto de Apoio')

    # Representação dos pesos
    plt.plot(-distancia1, peso1, 'bo', label=f'Peso 1: {peso1}N')
    plt.plot(distancia2, peso2, 'go', label=f'Peso 2: {peso2}N')

    # Linhas de conexão
    plt.plot([-distancia1, 0], [0, peso1], 'b--')
    plt.plot([0, distancia2], [0, peso2], 'g--')

    plt.xlim(-max(distancia1, distancia2) - 1, max(distancia1, distancia2) + 1)
    plt.ylim(0, max(peso1, peso2) + 1)
    plt.title('Visualização da Alavanca em Equilíbrio')
    plt.xlabel('Distância do Ponto de Apoio (m)')
    plt.ylabel('Peso (N)')
    plt.legend()
    plt.grid()
    plt.show()

# Exemplo de uso
peso1 = 10  # Peso do primeiro objeto em Newtons
distancia1 = 2  # Distância do primeiro objeto ao ponto de apoio em metros
peso2 = 5  # Peso do segundo objeto em Newtons
distancia2 = 4  # Distância do segundo objeto ao ponto de apoio em metros

# Verifica o equilíbrio
if equilibrio_alavanca(peso1, distancia1, peso2, distancia2):
    print("A alavanca está em equilíbrio.")
else:
    print("A alavanca não está em equilíbrio.")

# Demonstração simbólica
demonstracao_equilibrio(peso1, distancia1, peso2, distancia2)

# Visualização gráfica
visualizacao_alavanca(peso1, distancia1, peso2, distancia2)