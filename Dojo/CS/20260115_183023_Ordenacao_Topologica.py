# Este código implementa a ordenação topológica de um grafo de dependências. 
# A ordenação topológica é usada para organizar tarefas que dependem umas das outras, 
# garantindo que uma tarefa só seja executada após todas as suas dependências. 
# O código utiliza um algoritmo de busca em profundidade (DFS) para realizar a ordenação.

from collections import defaultdict

def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        stack.append(node)

    for vertex in graph:
        dfs(vertex)

    return stack[::-1]  # Retorna a ordem inversa do stack

# Exemplo de uso
if __name__ == "__main__":
    graph = defaultdict(list)
    graph['A'].extend(['B', 'C'])
    graph['B'].extend(['D'])
    graph['C'].extend(['D'])
    graph['D'].extend([])

    print("Grafo de dependências:", dict(graph))
    print("Ordenação topológica:", topological_sort(graph))