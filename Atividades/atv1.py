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

