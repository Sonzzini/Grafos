from grafoMatrizND import GrafoND

grafo = GrafoND(5)
grafo.insereA(0, 1, 2.5)  # Aresta com peso 2.5 entre os vértices 0 e 1
grafo.insereA(1, 2, 1.8)  # Aresta com peso 1.8 entre os vértices 1 e 2
grafo.insereA(3, 4, 3.3)  # Aresta com peso 3.3 entre os vértices 3 e 4

grafo.show()
grafo.showMin()
