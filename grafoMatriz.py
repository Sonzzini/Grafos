# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
from Atividades.atv1 import inDegree as atvInDegree
from Atividades.atv1 import outDegree as atvOutDegree
from Atividades.atv1 import fonte as atvFonte
from Atividades.atv1 import sorvedouro as atvSorvedouro

class Grafo:
    TAM_MAX_DEFAULT = 100

    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n  # número de vértices
        self.m = 0  # número de arestas
        self.adj = [[0 for i in range(n)] for j in range(n)]  # matriz

    # Insere uma aresta no Grafo tal que v é adjacente a w
    def insereA(self, v, w):
        if self.adj[v][w] == 0:
            self.adj[v][w] = 1
            self.m += 1  # qtde de arestas

    def removeA(self, v, w):
        if self.adj[v][w] == 1:
            self.adj[v][w] = 0
            self.m -= 1
    
    def show(self):
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

    def showMin(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            for w in range(self.n):
                if self.adj[i][w] == 1:
                    print(" 1 ", end="") 
                else:
                    print(" 0 ", end="")
            print("\n")
        print("\nfim da impressao do grafo." )

    def inDegree(self, v) -> int:
        degree = atvInDegree(v, self.adj)
        print(f"Grau de entrada {v}: {degree}")
        return degree
    
    def outDegree(self, v) -> int:
        degree = atvOutDegree(v, self.adj)
        print(f"Grau de saída de {v}: {degree}")
        return degree
    
    def fonte(self, v) -> int:
        fonte = atvFonte(v, self.adj)
        print(f"Vértice {v} == fonte: {fonte}")
        return fonte
    
    def sorvedouro(self, v) -> int:
        s = atvSorvedouro(v, self.adj)
        print(f"Vértice {v} == sorvedouro: {s}")
        return s
# class Grafo:
#     TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
#     # construtor da classe grafo
#     def __init__(self, n=TAM_MAX_DEFAULT):
#         self.n = n # número de vértices
#         self.m = 0 # número de arestas
#         # matriz de adjacência
#         self.adj = [[0 for i in range(n)] for j in range(n)]

# 	# Insere uma aresta no Grafo tal que
# 	# v é adjacente a w
#     def insereA(self, v, w):
#         if self.adj[v][w] == 0:
#             self.adj[v][w] = 1
#             self.m+=1 # atualiza qtd arestas
    
#     # remove uma aresta v->w do Grafo	
#     def removeA(self, v, w):
#         # testa se temos a aresta
# 	    if self.adj[v][w] == 1:
# 	        self.adj[v][w] = 0
#             self.m-=1; # atualiza qtd arestas

# 	# Apresenta o Grafo contendo
# 	# número de vértices, arestas
# 	# e a matriz de adjacência obtida	
#     def show(self):
#         print(f"\n n: {self.n:2d} ", end="")
#         print(f"m: {self.m:2d}\n")
#         for i in range(self.n):
#             for w in range(self.n):
#                 if self.adj[i][w] == 1:
#                     print(f"Adj[{i:2d},{w:2d}] = 1 ", end="") 
#                 else:
#                     print(f"Adj[{i:2d},{w:2d}] = 0 ", end="")
#             print("\n")
#         print("\nfim da impressao do grafo." )


# 	# Apresenta o Grafo contendo
# 	# número de vértices, arestas
# 	# e a matriz de adjacência obtida 
#     # Apresentando apenas os valores 0 ou 1	
#     def showMin(self):
#         print(f"\n n: {self.n:2d} ", end="")
#         print(f"m: {self.m:2d}\n")
#         for i in range(self.n):
#             for w in range(self.n):
#                 if self.adj[i][w] == 1:
#                     print(" 1 ", end="") 
#                 else:
#                     print(" 0 ", end="")
#             print("\n")
#         print("\nfim da impressao do grafo." )
    