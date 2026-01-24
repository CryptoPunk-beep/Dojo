# A correspondência fundamental em extensões de Galois estabelece uma relação entre subgrupos de um grupo de Galois e subcorpos de uma extensão de campo. 
# Se K é uma extensão de campo de F e G é o grupo de Galois de K sobre F, então existe uma correspondência bijetiva entre os subgrupos de G e os subcorpos de K que contêm F. 
# Essa correspondência é fundamental para entender a estrutura das extensões de Galois e suas aplicações em teoria de números e geometria algébrica.

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

# Inicializa a impressão em LaTeX
sp.init_printing()

def galois_extension_example():
    """
    Demonstra uma extensão de Galois simples e a correspondência fundamental.
    
    A função considera a extensão K = Q(√2) sobre F = Q e calcula o grupo de Galois.
    """
    # Definindo os campos
    F = sp.Q
    K = sp.Field(sp.sqrt(2), extension=F)
    
    # Calculando o grupo de Galois
    G = sp.GaloisGroup(K, F)
    
    # Exibindo o grupo de Galois
    print("Grupo de Galois G(K/F):")
    sp.pretty_print(G)

    # Subgrupos e subcorpos
    subgroups = G.subgroups()
    subfields = [K.subfield(g) for g in subgroups]
    
    print("\nSubgrupos e seus respectivos subcorpos:")
    for g, sf in zip(subgroups, subfields):
        print(f"Subgrupo: {g}, Subcorpo: {sf}")

def plot_galois_correspondence():
    """
    Plota a correspondência entre subgrupos e subcorpos.
    """
    # Definindo os subgrupos e subcorpos
    subgroups = ['G', 'H', 'L']
    subfields = ['K', 'F', 'Q']

    # Criando um gráfico
    G = nx.DiGraph()
    for sg, sf in zip(subgroups, subfields):
        G.add_node(sg)
        G.add_node(sf)
        G.add_edge(sg, sf)

    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold', arrows=True)
    plt.title("Correspondência Fundamental de Galois")
    plt.show()

# Executando o exemplo e a visualização
galois_extension_example()
plot_galois_correspondence()