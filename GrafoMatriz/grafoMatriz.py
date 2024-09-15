# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:59:10 2023

@author: icalc
"""
import sys
import os
import numpy as np

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
    def conexidade_categoria(self):
        # Verificar se o grafo é fortemente conexo (C3) primeiro
        if self.is_strongly_connected() == 0:
            return 3  # C3: Fortemente conexo

        # Se não for fortemente conexo, verificar se é unilateralmente conexo (C2)
        if self.is_unilaterally_connected() == 0:
            return 2  # C2: Unilateralmente conexo

        # Se não for C2, verificar se é fracamente conexo (C1)
        if self.is_weakly_connected() == 0:
            return 1  # C1: Fracamente conexo

        # Se nenhuma das condições acima for satisfeita, é desconexo (C0)
        return 0  # C0: Desconexo


    # Método auxiliar para verificar a conexidade forte (C3)
    def is_strongly_connected(self):
        n = len(self.adj)

        visited = [False] * n

        self.dfs(0, visited)

        if not all(visited):
            return False
        
        transposed_graph = np.transpose(self.adj)

        visited = [False] * n

        self.dfs(transposed_graph, 0, visited)

        return all(visited)

    # Método auxiliar para verificar a conexidade unilateral (C2)
    def is_unilaterally_connected(self):
        n = len(self.adj)

        for i in range(n):
            reachable_from_v = [False] * n
            self.dfs(self.adj, i, reachable_from_v)

            reachable_to_v = [False] * n
            self.dfs(np.transpose(self.adj), i, reachable_to_v)

            for j in range(n):
                if not (reachable_from_v[j] or reachable_to_v[j]):
                    return False
        return True


    # Método auxiliar para verificar a conexidade fraca (C1)
    def is_weakly_connected(self):
        n = len(self.adj)

        undirected_graph = np.copy(self.adj)

        for i in range(n):
            for j in range(n):
                if self.adj[i][j] == 1 or self.adj[j][i] == 1:
                    undirected_graph[i][j] = undirected_graph[j][i] = 1

        visited = [False] * n
        self.dfs(undirected_graph, 0, visited)

        return all(visited)

    # DFS que ignora a direção das arestas (para conexidade fraca)
    def _dfs_fraco(self, v, visitados):
        visitados[v] = True
        for w in range(self.n):
            if (self.adj[v][w] == 1 or self.adj[w][v] == 1) and not visitados[w]:
                self._dfs_fraco(w, visitados)

    # DFS simples (para conexidade forte e unilateral)
    def dfs(self, v, visitados):
        visitados[v] = True
        for i in range(self.n):
            if self.adj[v][i] == 1 and not visitados[i]:
                self.dfs(i, visitados)

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

    # Método que retorna o grafo reduzido no formato de uma matriz de adjacência
    def grafoReduzido(self):
        # Passo 1: Encontrar as componentes fortemente conexas usando Kosaraju
        componentes_fortemente_conexas = self._kosaraju()

        # Número de componentes fortemente conexas
        num_componentes = len(componentes_fortemente_conexas)

        # Passo 2: Criar a matriz de adjacência do grafo reduzido
        grafo_reduzido_adj = [[0 for _ in range(num_componentes)] for _ in range(num_componentes)]

        # Mapear cada vértice original para a sua componente fortemente conexa
        componente_de_vertice = [-1] * self.n
        for i, componente in enumerate(componentes_fortemente_conexas):
            for v in componente:
                componente_de_vertice[v] = i

        # Passo 3: Criar as arestas entre as componentes no grafo reduzido
        for v in range(self.n):
            for w in range(self.n):
                if self.adj[v][w] == 1:
                    componente_v = componente_de_vertice[v]
                    componente_w = componente_de_vertice[w]
                    if componente_v != componente_w:
                        grafo_reduzido_adj[componente_v][componente_w] = 1

        return grafo_reduzido_adj


    # Implementação do algoritmo de Kosaraju para encontrar as componentes fortemente conexas
    def _kosaraju(self):
        # Passo 1: Fazer a DFS normal e empilhar os vértices na ordem de finalização
        visitados = [False] * self.n
        ordem_finalizacao = []

        for v in range(self.n):
            if not visitados[v]:
                self._dfs_kosaraju(v, visitados, ordem_finalizacao)

        # Passo 2: Transpor o grafo
        grafo_transposto = self._transpor()

        # Passo 3: Fazer a DFS no grafo transposto na ordem inversa de finalização
        visitados_transposto = [False] * self.n
        componentes_fortemente_conexas = []

        while ordem_finalizacao:
            v = ordem_finalizacao.pop()
            if not visitados_transposto[v]:
                componente_atual = []
                grafo_transposto._dfs_componente(v, visitados_transposto, componente_atual)
                componentes_fortemente_conexas.append(componente_atual)

        # Depuração: Exibir as componentes fortemente conexas
        print("Componentes Fortemente Conexas:", componentes_fortemente_conexas)
        
        return componentes_fortemente_conexas


    # DFS para Kosaraju - Primeiro passo, empilhar na ordem de finalização
    def _dfs_kosaraju(self, v, visitados, ordem_finalizacao):
        visitados[v] = True
        for w in range(self.n):
            if self.adj[v][w] == 1 and not visitados[w]:
                self._dfs_kosaraju(w, visitados, ordem_finalizacao)
        ordem_finalizacao.append(v)

    # DFS para encontrar componentes fortemente conexas no grafo transposto
    def _dfs_componente(self, v, visitados_transposto, componente_atual):
        visitados_transposto[v] = True
        componente_atual.append(v)
        for w in range(self.n):
            if self.adj[w][v] == 1 and not visitados_transposto[w]:
                self._dfs_componente(w, visitados_transposto, componente_atual)
