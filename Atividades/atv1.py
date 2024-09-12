def inDegree(v, adj) -> int:
    degree = 0
    for row in range(len(adj)):
        degree += adj[row][v]
    return degree
