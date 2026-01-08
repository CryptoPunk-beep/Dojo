# O Teorema Central do Limite (TCL) é um dos pilares da estatística. Ele afirma que, dado um número suficientemente grande de amostras independentes de uma população com uma média e uma variância finitas, a distribuição da média amostral se aproxima de uma distribuição normal, independentemente da forma da distribuição original. Neste script, vamos demonstrar o TCL simbolicamente e através de simulações numéricas.

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from scipy.stats import norm

# Inicializa a impressão em LaTeX
sp.init_printing()

def teorema_central_limite(n, num_amostras=1000, mu=0, sigma=1):
    """
    Simula o Teorema Central do Limite.
    
    Parâmetros:
    n (int): Tamanho da amostra.
    num_amostras (int): Número de amostras a serem geradas.
    mu (float): Média da população.
    sigma (float): Desvio padrão da população.
    
    Retorna:
    None: Gera gráficos da distribuição das amostras e da distribuição normal.
    """
    amostras = np.random.normal(mu, sigma, (num_amostras, n))
    medias_amostrais = np.mean(amostras, axis=1)

    # Gráfico da distribuição das médias amostrais
    plt.figure(figsize=(12, 6))
    plt.hist(medias_amostrais, bins=30, density=True, alpha=0.6, color='g', label='Distribuição das Médias Amostrais')

    # Parâmetros da distribuição normal
    x = np.linspace(mu - 4*sigma/np.sqrt(n), mu + 4*sigma/np.sqrt(n), 100)
    y = norm.pdf(x, mu, sigma/np.sqrt(n))
    
    plt.plot(x, y, 'r', label='Distribuição Normal Teórica')
    plt.title(f'Distribuição das Médias Amostrais (n={n})')
    plt.xlabel('Média Amostral')
    plt.ylabel('Densidade')
    plt.legend()
    plt.grid()
    plt.show()

def demonstracao_simbolica():
    """
    Demonstra simbolicamente o Teorema Central do Limite usando SymPy.
    
    Retorna:
    None: Exibe a demonstração matemática.
    """
    n, mu, sigma = sp.symbols('n mu sigma')
    # Distribuição da média amostral
    media_amostral = mu
    variancia_amostral = sigma**2 / n
    
    # Distribuição normal
    distribucao_normal = sp.Function('N')(media_amostral, sp.sqrt(variancia_amostral))
    
    display(distribucao_normal)

# Executa a demonstração simbólica
demonstracao_simbolica()

# Simula o Teorema Central do Limite para diferentes tamanhos de amostra
for n in [1, 5, 30, 100]:
    teorema_central_limite(n)