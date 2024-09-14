# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
import sys
import os

# Adiciona o diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Atividades.atv1 import inDegree as atvInDegree
from Atividades.atv1 import outDegree as atvOutDegree
from Atividades.atv1 import fonte as atvFonte
from Atividades.atv1 import sorvedouro as atvSorvedouro
from Atividades.atv1 import isSymmetric as atvIsSymmetric
from Atividades.atv1 import createGraphFromFile as atvCreateGraphFromFile
from Atividades.atv1 import D_isComplete as atvIsComplete
from Atividades.atv1 import complemento as atvComplemento

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

    # Remove um vértice v e todas as arestas associadas
    def removeV(self, v):
        # Remover todas as arestas de entrada e saída relacionadas ao vértice v
        for i in range(self.n):
            if self.adj[i][v] == 1:  # Verifica se há uma aresta de entrada
                self.adj[i][v] = 0
                self.m -= 1
            if self.adj[v][i] == 1:  # Verifica se há uma aresta de saída
                self.adj[v][i] = 0
                self.m -= 1

        # Remover a linha correspondente ao vértice v
        self.adj.pop(v)

        # Remover a coluna correspondente ao vértice v em todas as outras linhas
        for i in range(self.n - 1):
            self.adj[i].pop(v)

        # Atualizar o número de vértices
        self.n -= 1

    
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
    
    def isSymmetric(self) -> int:
        return atvIsSymmetric(self.adj)
    
    def createGraphFromFile(self, filename):
        atvCreateGraphFromFile(self, filename)
        self.showMin()

    def isComplete(self) -> bool:
        is_complete = atvIsComplete(self)
        print(f"Grafo == completo: {is_complete}")
        return is_complete

    def complemento(self) -> g:
        return atvComplemento(self)
    
    