class GrafoND:
    TAM_MAX_DEFAULT = 100

    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n
        self.m = 0
        # Inicializa a matriz de adjacência com None (sem aresta)
        self.adj = [[None for _ in range(n)] for _ in range(n)]

    # Insere uma aresta no Grafo com um peso (float) opcional
    def insereA(self, v, w, peso=1.0):
        if self.adj[v][w] is None and self.adj[w][v] is None:
            self.adj[v][w] = peso
            self.adj[w][v] = peso
            self.m += 1
    
    def removeA(self, v, w):
        if self.adj[v][w] is not None and self.adj[w][v] is not None:
            self.adj[v][w] = None
            self.adj[w][v] = None
            self.m -= 1

    def show(self):
        print('-' * 50)

        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] is not None:
                    print(f"Adj[{i:2d},{w:2d}] = {self.adj[i][w]:4.1f} ", end="")
                else:
                    print(f"Adj[{i:2d},{w:2d}] = None ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

        print('-' * 50)

    def showMin(self):
        print('-' * 50)
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] is not None:
                    print(f" {self.adj[i][w]:4.1f} ", end="")
                else:
                    print(" None ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
        print('-' * 50)