# O Triângulo de Pascal, embora associado a Blaise Pascal, tem raízes muito mais antigas na matemática indiana, especialmente com o matemático Pingala. 
# Ele utilizou uma forma primitiva do triângulo para descrever os coeficientes binomiais, que são fundamentais em combinações e probabilidades. 
# O triângulo é construído a partir de somas de números acima dele, e os coeficientes binomiais têm aplicações em várias áreas da matemática.

import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, binomial, init_printing
init_printing()

def triangulo_pascal(n):
    """
    Gera o Triângulo de Pascal até a linha n.
    
    :param n: Número de linhas do triângulo.
    :return: Lista de listas representando o Triângulo de Pascal.
    """
    triangulo = []
    for linha in range(n):
        nova_linha = [1] * (linha + 1)
        for j in range(1, linha):
            nova_linha[j] = triangulo[linha - 1][j - 1] + triangulo[linha - 1][j]
        triangulo.append(nova_linha)
    return triangulo

def visualizar_triangulo(triangulo):
    """
    Visualiza o Triângulo de Pascal usando Matplotlib.
    
    :param triangulo: Lista de listas representando o Triângulo de Pascal.
    """
    plt.figure(figsize=(10, 6))
    for i, linha in enumerate(triangulo):
        for j, valor in enumerate(linha):
            plt.text(j - i / 2, -i, str(valor), ha='center', va='center', fontsize=12)
    plt.title("Triângulo de Pascal")
    plt.axis('off')
    plt.show()

def coeficientes_binomiais(n):
    """
    Calcula e exibe os coeficientes binomiais usando a notação de Pingala.
    
    :param n: Número total de elementos.
    """
    print("Coeficientes Binomiais para n =", n)
    for k in range(n + 1):
        coef = binomial(n, k)
        print(f"C({n}, {k}) = {coef}")

n = 5  # Número de linhas do Triângulo de Pascal
triangulo = triangulo_pascal(n)
visualizar_triangulo(triangulo)
coeficientes_binomiais(n)

# Demonstração de uma propriedade do coeficiente binomial
x, y = symbols('x y')
demonstracao = (x + y)**n
demonstracao_expansao = demonstracao.expand()
demonstracao_expansao