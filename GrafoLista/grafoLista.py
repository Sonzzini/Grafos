# -- coding: utf-8 --
"""
Created on Tue Feb 14 16:01:03 2023

@author: icalc
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Atividades.atv1_lista import isEqual as atvIsEqual
from Atividades.atv1_lista import fromMatrizToList as atvFromMatrizToList
from Atividades.atv1_lista import invertAdjList as atvInvertAdjList
from Atividades.atv1_lista import isSource as atvIsSource
from Atividades.atv1_lista import isSorvedouro as atvIsSorvedouro
from Atividades.atv1_lista import isSymetric as atvIsSymetric
from Atividades.atv1_lista import adjListBuilder as atvAdjListBuilder
from Atividades.atv1_lista import removeVertice as atvRemoveVertice
from Atividades.atv1_lista import removeVD as atvRemoveVD
from Atividades.atv1_lista import isComplete as atvIsComplete

# Grafo como uma lista de adjacência
class Grafo:
    TAM_MAX_DEFAULT = 100 # qtde de vértices máxima default
    # construtor da classe grafo
    def __init__(self, n=TAM_MAX_DEFAULT):
        self.n = n # número de vértices
        self.m = 0 # número de arestas
        # lista de adjacência
        self.listaAdj = [[] for i in range(self.n)]
    
    
    def insereV(self):
        self.listaAdj.append([])
        self.n += 1

	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m+=1

    def insereA_com_peso(self, v, w, value):
        self.listaAdj[v].append((w, value))
        self.m+=1
     
    # Remove uma aresta v->w do Grafo
    def removeA(self, v, w):
        for edge in self.listaAdj[v]:
            if edge[0] == w:
                self.listaAdj[v].remove(edge)
                self.m -= 1
                break
        for edge in self.listaAdj[w]:
            if edge[0] == v:
                self.listaAdj[w].remove(edge)
                self.m -= 1
                break

    # Remove um vértice do Grafo
    def removeV(self, v):
        if v >= self.n:
            print("Vértice não existe no grafo.")
            return

        # Remover todas as arestas que partem do vértice v
        self.m -= len(self.listaAdj[v])
        self.listaAdj[v] = []

        # Remover todas as arestas que chegam ao vértice v
        for i in range(self.n):
            self.listaAdj[i] = [edge for edge in self.listaAdj[i] if edge[0] != v]

        # Ajustar a lista de adjacência
        self.listaAdj.pop(v)
        self.n -= 1

        # Ajustar as arestas restantes
        for i in range(self.n):
            self.listaAdj[i] = [(x - 1 if x > v else x, p) for x, p in self.listaAdj[i]]
        
	# Apresenta o Grafo contendo
	# número de vértices, arestas
	# e a LISTA de adjacência obtida	
    def show(self):
        print(f"\n n: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}")
        for i in range(self.n):
            print(f"\n{i:2d}: ", end="")
            for w in range(len(self.listaAdj[i])):
                val = self.listaAdj[i][w]
                print(f"{val}", end="")

        print("\n\nfim da impressao do grafo." )

    def show_as_matrix(self):
        print(f"\nn: {self.n:2d} ", end="")
        print(f"m: {self.m:2d}\n")
        for i in range(self.n):
            print(i, end=": ")
            for j in range(len(self.listaAdj[i])):
                print(f"{self.listaAdj[i][j]} ", end = "")
            print()

    def isEqual(self, grafo2):
      return atvIsEqual(self, grafo2)
    
    def fromMatrizToList(self, matriz):
      return atvFromMatrizToList(self, matriz)
    
    def invertAdjList(self):
        return atvInvertAdjList(self)
    
    def isSource(self,v):
        return atvIsSource(self,v)
    
    def isSorvedouro(self, v):
        return atvIsSorvedouro(self, v)
    
    def isSymetric(self):
        return atvIsSymetric(self)
    
    def adjListBuilder(self, nome_arquivo):
        return atvAdjListBuilder(self, nome_arquivo)
        
    def removeVertice(self, v):
        return atvRemoveVertice(self, v)
    
    def removeVD(self, v):
        return atvRemoveVD(self, v)
    
    def isComplete(self):
        return atvIsComplete(self)
    
    # Função auxiliar para realizar uma busca em profundidade (DFS)
    def dfs(self, v, visitados):
        visitados[v] = True
        for vizinho, _ in self.listaAdj[v]:
            if not visitados[vizinho]:
                self.dfs(vizinho, visitados)

    # Função para verificar quantos componentes conexos existem no grafo
    def contar_componentes_conexos(self):
        visitados = [False] * self.n
        componentes = 0
        for v in range(self.n):
            if not visitados[v]:
                self.dfs(v, visitados)
                componentes += 1
        return componentes

    # Função para determinar a conexidade C0, C1, C2 e C3
    def determinar_conexidade(self):
        componentes = self.contar_componentes_conexos()
        if componentes > 1:
            print("C0: Grafo Desconexo")
        elif componentes == 1 and self.m > 0:
            print("C3: Grafo Fortemente Conexo")
        else:
            print("C2: Grafo Medianamente Conexo")

    # Função para imprimir o grafo reduzido
    def grafo_reduzido(self):
        componentes = self.contar_componentes_conexos()
        if componentes == 1:
            print("Grafo reduzido é um único vértice, pois o grafo é fortemente conexo.")
        else:
            print(f"O grafo possui {componentes} componentes. Não pode ser reduzido a um único vértice.")
