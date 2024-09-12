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