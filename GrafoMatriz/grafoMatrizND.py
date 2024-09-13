
class GrafoND:
    TAM_MAX_DEFAULT = 100

    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n
        self.m = 0
        self.adj = [[0 for i in range(n)] for j in range(n)]

    # Insere uma aresta no Grafo tal que
    # v e w são adjacentes um do outro
    def insereA(self, v, w):
        if self.adj[v][w] == 0 and self.adj[w][v] == 0:
            self.adj[v][w] = 1
            self.adj[w][v] = 1
            self.m += 1
    
    def removeA(self, v, w):
        if self.adj[v][w] == 1 and self.adj[w][v] == 1:
            self.adj[v][w] = 0
            self.adj[w][v] = 0
            self.m -= 1

    def show(self):
        print('-' * 50)

        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
                else:
                    print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

        print('-' * 50)

    def showMin(self):
        print('-' * 50)
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1  ", end="") 
                else:
                    print(" 0  ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )
        print('-' * 50)