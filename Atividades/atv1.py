import numpy as np
from typing import List


def inDegree(v, adj) -> int:
    degree = 0
    for row in range(len(adj)):
        degree += adj[row][v]
    return degree


def outDegree(v, adj) -> int:
    return sum(adj[v])


def fonte(v, adj) -> int:
    incidentes = inDegree(v, adj)
    outcidentes = outDegree(v, adj)
    if outcidentes > 0 and incidentes == 0:
        return 1
    return 0


def sorvedouro(v, adj) -> int:
    incidentes = inDegree(v, adj)
    outcidentes = outDegree(v, adj)
    if incidentes > 0 and outcidentes == 0:
        return 1
    return 0


def isSymmetric(adj) -> int:
    adj_np = np.array(adj)
    return int(np.array_equal(adj_np, adj_np.T))


def createGraphFromFile(g, filename) -> List[List[int]]:
    import GrafoMatriz.grafoMatriz

    with open(filename, 'r') as file:
        conteudo = file.readlines()

        conteudo = [linha.strip() for linha in conteudo]
        
        nVertices = int(conteudo[0]); conteudo.pop(0)
        nArestas = int(conteudo[0]); conteudo.pop(0)

        g.n = nVertices
        g.m = 0

        g.adj = [[0 for _ in range(nVertices)] for _ in range(nVertices)]

        for linha in conteudo:
            x, y = map(int, linha.split())
            g.insereA(x, y)


def ND_isComplete(g) -> bool:
    for i in range(g.n):
        if None in g.adj[i][:i] + g.adj[i][i+1:]:
            return False
    return True


def D_isComplete(g) -> bool:
    for i in range(g.n):
        if 0 in g.adj[i][:i] + g.adj[i][i+1:]:
            return False
    return True


def complemento(g):
    d = g.adj
    for i in range(g.n):
        for j in range(g.n):
            if d.adj[i][j] == 0:
                d.adj[i][j] = 1
    return d


# Método para verificar se o grafo é conexo
def ND_isConexo(g) -> bool:
    # Inicializar uma lista de visitados com False para cada vértice
    visitados = [False] * g.n

    # Realiza a DFS começando no vértice 0
    ND_dfs(g, 0, visitados)

    # Se todos os vértices foram visitados, o grafo é conexo (retorna 0)
    # Caso contrário, o grafo é desconexo (retorna 1)
    if all(visitados):
        return 0  # Grafo é conexo
    else:
        return 1  # Grafo é desconexo


# Método auxiliar de busca em profundidade (DFS)
def ND_dfs(g, v, visitados):
    # Marca o vértice atual como visitado
    visitados[v] = True

    # Percorre todos os vértices adjacentes ao vértice v
    for w in range(g.n):
        if g.adj[v][w] is not None and not visitados[w]:
            # Se o vértice adjacente não foi visitado, faz a DFS nele
            ND_dfs(g, w, visitados)


