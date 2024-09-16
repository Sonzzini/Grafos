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
from Atividades.atv1_lista import removeV as atvRemoveV
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
        
	# Insere uma aresta no Grafo tal que
	# v é adjacente a w
    def insereA(self, v, w):
        self.listaAdj[v].append(w)
        self.m+=1
     
    # remove uma aresta v->w do Grafo	
    def removeA(self, v, w):
        self.listaAdj[v].remove(w)
        self.m-=1
        
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
                print(f"{val:2d}", end="") 

        print("\n\nfim da impressao do grafo." )

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
        
    def removeV(self, v):
        return atvRemoveV(self, v)
    
    def removeVD(self, v):
        return atvRemoveVD(self, v)
    
    def isComplete(self):
        return atvIsComplete(self)