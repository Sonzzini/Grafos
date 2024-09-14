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
# from Atividades.atv1 import D_isConexo as atvIsConexo

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

    def complemento(self):
        return atvComplemento(self)
    
    # def isConexo(self) -> bool:
    #     return atvIsConexo(self)

    # Método principal para verificar a categoria de conexidade
    def categoriaConexidade(self):
        # Verificar se o grafo é fortemente conexo (C3)
        if self.isConexoForte() == 0:
            return 3  # C3: Fortemente conexo

        # Verificar se o grafo é unilateralmente conexo (C2)
        if self.isConexoUnilateral() == 0:
            return 2  # C2: Unilateralmente conexo

        # Verificar se o grafo é fracamente conexo (C1)
        if self.isConexoFraco() == 0:
            return 1  # C1: Fracamente conexo

        # Se não atender a nenhuma dessas condições, é desconexo (C0)
        return 0  # C0: Desconexo

    # Método auxiliar para verificar a conexidade forte (C3)
    def isConexoForte(self):
        visitados = [False] * self.n

        # Realiza a DFS a partir de um vértice
        self._dfs(0, visitados)

        # Se algum vértice não foi visitado, o grafo não é fortemente conexo
        if not all(visitados):
            return 1

        # Transpor o grafo e realizar DFS no grafo transposto
        grafo_transposto = self._transpor()
        visitados_transposto = [False] * self.n
        grafo_transposto._dfs(0, visitados_transposto)

        # Se todos os vértices foram visitados no grafo transposto, é fortemente conexo
        if all(visitados_transposto):
            return 0
        else:
            return 1

    # Método auxiliar para verificar a conexidade unilateral (C2)
    def isConexoUnilateral(self):
        for v in range(self.n):
            for w in range(v + 1, self.n):
                # Verifica se existe um caminho de v para w ou de w para v
                if not (self._existeCaminho(v, w) or self._existeCaminho(w, v)):
                    return 1  # Não é unilateralmente conexo
        return 0  # É unilateralmente conexo

    # Método auxiliar para verificar a conexidade fraca (C1)
    def isConexoFraco(self):
        visitados = [False] * self.n
        self._dfs_fraco(0, visitados)
        if all(visitados):
            return 0  # Fracamente conexo
        else:
            return 1  # Desconexo

    # DFS que ignora a direção das arestas (para conexidade fraca)
    def _dfs_fraco(self, v, visitados):
        visitados[v] = True
        for w in range(self.n):
            if (self.adj[v][w] == 1 or self.adj[w][v] == 1) and not visitados[w]:
                self._dfs_fraco(w, visitados)

    # DFS simples (para conexidade forte e unilateral)
    def _dfs(self, v, visitados):
        visitados[v] = True
        for w in range(self.n):
            if self.adj[v][w] == 1 and not visitados[w]:
                self._dfs(w, visitados)

    # Método auxiliar para transpor o grafo (inverter as arestas)
    def _transpor(self):
        grafo_transposto = Grafo(self.n)
        for v in range(self.n):
            for w in range(self.n):
                if self.adj[v][w] == 1:
                    grafo_transposto.insereA(w, v)
        return grafo_transposto

    # Método para verificar se existe um caminho entre dois vértices (DFS)
    def _existeCaminho(self, v, w):
        visitados = [False] * self.n
        self._dfs(v, visitados)
        return visitados[w]

    