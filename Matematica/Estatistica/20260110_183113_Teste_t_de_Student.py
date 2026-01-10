# O teste t de Student é uma ferramenta estatística utilizada para determinar se há uma diferença significativa entre as médias de uma ou duas amostras. 
# Ele é especialmente útil quando as amostras são pequenas e a variância populacional é desconhecida. 
# O teste t pode ser aplicado em duas situações: (1) um teste t de uma amostra, onde comparamos a média de uma amostra com uma média conhecida, 
# e (2) um teste t de duas amostras, onde comparamos as médias de duas amostras independentes.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import sympy as sp

# Inicialização do SymPy para impressão LaTeX
sp.init_printing()

def t_test_one_sample(sample, population_mean):
    """
    Realiza um teste t de uma amostra.
    
    :param sample: Lista ou array de dados da amostra
    :param population_mean: Média populacional conhecida
    :return: Estatística t e valor p
    """
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)
    n = len(sample)
    
    t_statistic = (sample_mean - population_mean) / (sample_std / np.sqrt(n))
    p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df=n-1))
    
    return t_statistic, p_value

def t_test_two_samples(sample1, sample2):
    """
    Realiza um teste t de duas amostras independentes.
    
    :param sample1: Lista ou array de dados da primeira amostra
    :param sample2: Lista ou array de dados da segunda amostra
    :return: Estatística t e valor p
    """
    mean1 = np.mean(sample1)
    mean2 = np.mean(sample2)
    std1 = np.std(sample1, ddof=1)
    std2 = np.std(sample2, ddof=1)
    n1 = len(sample1)
    n2 = len(sample2)
    
    pooled_std = np.sqrt(((n1 - 1) * std1**2 + (n2 - 1) * std2**2) / (n1 + n2 - 2))
    t_statistic = (mean1 - mean2) / (pooled_std * np.sqrt(1/n1 + 1/n2))
    p_value = 2 * (1 - stats.t.cdf(np.abs(t_statistic), df=n1 + n2 - 2))
    
    return t_statistic, p_value

# Exemplo de uso do teste t de uma amostra
np.random.seed(0)
sample_data = np.random.normal(loc=5, scale=2, size=30)  # amostra com média 5 e desvio padrão 2
population_mean = 4.5

t_stat, p_val = t_test_one_sample(sample_data, population_mean)
print(f'Teste t de uma amostra:\nEstatística t: {t_stat:.4f}, Valor p: {p_val:.4f}')

# Exemplo de uso do teste t de duas amostras
sample_data1 = np.random.normal(loc=5, scale=2, size=30)
sample_data2 = np.random.normal(loc=6, scale=2, size=30)

t_stat_two, p_val_two = t_test_two_samples(sample_data1, sample_data2)
print(f'Teste t de duas amostras:\nEstatística t: {t_stat_two:.4f}, Valor p: {p_val_two:.4f}')

# Visualização das amostras
plt.figure(figsize=(12, 6))
plt.hist(sample_data1, alpha=0.5, label='Amostra 1', color='blue', bins=15)
plt.hist(sample_data2, alpha=0.5, label='Amostra 2', color='orange', bins=15)
plt.axvline(np.mean(sample_data1), color='blue', linestyle='dashed', linewidth=2)
plt.axvline(np.mean(sample_data2), color='orange', linestyle='dashed', linewidth=2)
plt.title('Distribuição das Amostras')
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.legend()
plt.show()

# Demonstração matemática usando SymPy para o teste t de uma amostra
x, mu, s, n = sp.symbols('x mu s n')
t_statistic_sympy = (x - mu) / (s / sp.sqrt(n))
t_statistic_sympy_simplified = sp.simplify(t_statistic_sympy)
sp.display(t_statistic_sympy_simplified)

# Demonstração matemática usando SymPy para o teste t de duas amostras
mean1, mean2, pooled_std_sympy = sp.symbols('mean1 mean2 pooled_std')
t_statistic_two_samples_sympy = (mean1 - mean2) / (pooled_std_sympy * sp.sqrt(1/n1 + 1/n2))
t_statistic_two_samples_sympy_simplified = sp.simplify(t_statistic_two_samples_sympy)
sp.display(t_statistic_two_samples_sympy_simplified)