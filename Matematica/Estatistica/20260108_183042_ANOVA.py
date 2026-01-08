# ANOVA (Análise de Variância) é uma técnica estatística utilizada para comparar as médias de três ou mais grupos. 
# O objetivo é determinar se existe uma diferença estatisticamente significativa entre as médias dos grupos. 
# A ANOVA de um fator analisa a variância entre os grupos em relação à variância dentro dos grupos. 
# Neste script, utilizaremos Python para demonstrar os conceitos matemáticos da ANOVA, 
# incluindo a derivação da estatística F e a visualização dos resultados.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import sympy as sp
from statsmodels.stats.anova import AnovaRM

# Inicializando a impressão de LaTeX
sp.init_printing()

def anova_one_way(groups):
    """
    Realiza a ANOVA de um fator (one-way ANOVA) e retorna os resultados.

    Parameters:
    groups (list of np.ndarray): Lista de arrays numpy contendo os dados de cada grupo.

    Returns:
    tuple: Estatística F e valor-p da ANOVA.
    """
    # Número de grupos
    k = len(groups)
    # Número total de observações
    N = sum(len(group) for group in groups)
    
    # Média geral
    grand_mean = np.mean(np.concatenate(groups))
    
    # Soma dos quadrados entre grupos (SSB)
    ssb = sum(len(group) * (np.mean(group) - grand_mean) ** 2 for group in groups)
    
    # Soma dos quadrados dentro dos grupos (SSW)
    ssw = sum(np.sum((group - np.mean(group)) ** 2) for group in groups)
    
    # Graus de liberdade
    df_between = k - 1
    df_within = N - k
    
    # Estatística F
    msb = ssb / df_between  # Média dos quadrados entre grupos
    msw = ssw / df_within    # Média dos quadrados dentro dos grupos
    F = msb / msw
    
    # Valor-p
    p_value = 1 - stats.f.cdf(F, df_between, df_within)
    
    return F, p_value

def plot_groups(groups):
    """
    Plota os dados dos grupos.

    Parameters:
    groups (list of np.ndarray): Lista de arrays numpy contendo os dados de cada grupo.
    """
    plt.boxplot(groups, labels=[f'Grupo {i+1}' for i in range(len(groups))])
    plt.title('Boxplot dos Grupos')
    plt.ylabel('Valores')
    plt.xlabel('Grupos')
    plt.grid()
    plt.show()

# Exemplo de dados simulados
np.random.seed(42)
grupo1 = np.random.normal(loc=5, scale=1, size=30)
grupo2 = np.random.normal(loc=6, scale=1, size=30)
grupo3 = np.random.normal(loc=7, scale=1, size=30)

# Realizando a ANOVA
F, p_value = anova_one_way([grupo1, grupo2, grupo3])

# Exibindo resultados
print(f"Estatística F: {F:.4f}")
print(f"Valor-p: {p_value:.4f}")

# Plotando os grupos
plot_groups([grupo1, grupo2, grupo3])

# Demonstração simbólica da fórmula da ANOVA usando SymPy
k, N, mu_g, mu_i, n_i = sp.symbols('k N mu_g mu_i n_i')
SSB = sp.Sum(n_i * (mu_i - mu_g)**2, (i, 1, k))
SSW = sp.Sum((n_i - 1) * (mu_i - mu_g)**2, (i, 1, k))
F_stat = SSB / SSW

sp.init_printing()
display(F_stat)