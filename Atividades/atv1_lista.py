import numpy as np
from typing import List

def isEqual(self, grafo2):
        if self.n != grafo2.n or self.m != grafo2.m:
            return False
        
        for i in range(self.n):
            if sorted(self.listaAdj[i]) != sorted(grafo2.listaAdj[i]):
                return False
        
        return True


def fromMatrizToList(cls, matrizAdjacencia):
    n = len(matrizAdjacencia)
    grafo = cls(n)
        
    for i in range(n):
        for j in range(n):
            if matrizAdjacencia[i][j] != 0:
                grafo.insereA(i, j)
        
    return grafo

def invertAdjList(self):
    for i in range(self.n):
        self.listaAdj[i] = self.listaAdj[i][::-1]

def isSource(self, vertice):
        # Verificar grau de saída
        grauSaida = len(self.listaAdj[vertice])
        
        # Verificar grau de entrada
        grauEntrada = 0
        for i in range(self.n):
            if vertice in self.listaAdj[i]:
                grauEntrada += 1
        
        # Verificar condições de fonte
        if grauSaida > 0 and grauEntrada == 0:
            return 1
        else:
            return 0
        
def isSorvedouro(self, vertice):
        # Verificar grau de saída
        grauSaida = len(self.listaAdj[vertice])
        
        # Verificar grau de entrada
        grauEntrada = 0
        for i in range(self.n):
            if vertice in self.listaAdj[i]:
                grauEntrada += 1
        
        # Verificar condições de sorvedouro
        if grauSaida == 0 and grauEntrada > 0:
            return 1
        else:
            return 0
        
def isSymetric(self):
        for v in range(self.n):
            for w in self.listaAdj[v]:
                if v not in self.listaAdj[w]:
                    return 0
        return 1


def adjListBuilder(cls, nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        
    # Primeira linha: número de vértices
    n = int(linhas[0].strip())
    # Segunda linha: número de arestas
    m = int(linhas[1].strip())
        
    # Criar o grafo com n vértices
    grafo = cls(n)
        
    # Ler as arestas
    for linha in linhas[2:]:
        v, w = map(int, linha.strip().split())
        grafo.insereA(v, w)
        
    return grafo

def removeV(self, vertice):
    # Remover todas as arestas associadas ao vértice
    while self.listaAdj[vertice]:
        adjacente = self.listaAdj[vertice].pop()
        self.listaAdj[adjacente].remove(vertice)
        self.m -= 1
        
    # Remover o vértice da lista de adjacência
    self.listaAdj.pop(vertice)
    self.n -= 1
        
    # Ajustar a numeração dos vértices restantes
    for i in range(len(self.listaAdj)):
        self.listaAdj[i] = [v - 1 if v > vertice else v for v in self.listaAdj[i]]

def removeVD(self, vertice):
    # Remover todas as arestas que partem do vértice
    while self.listaAdj[vertice]:
        adjacente = self.listaAdj[vertice].pop()
        self.m -= 1
        
    # Remover todas as arestas que chegam ao vértice
    for i in range(self.n):
        if vertice in self.listaAdj[i]:
            self.listaAdj[i].remove(vertice)
            self.m -= 1
        
    # Remover o vértice da lista de adjacência
    self.listaAdj.pop(vertice)
    self.n -= 1
        
    # Ajustar a numeração dos vértices restantes
    for i in range(len(self.listaAdj)):
        self.listaAdj[i] = [v - 1 if v > vertice else v for v in self.listaAdj[i]]

def isComplete(self):
    for i in range(self.n):
        # Verificar se o vértice i tem arestas para todos os outros vértices
        if len(self.listaAdj[i]) != self.n - 1:
            return False
            
        # Verificar se todos os outros vértices têm arestas para o vértice i (para grafos dirigidos)
        for j in range(self.n):
            if i != j and i not in self.listaAdj[j]:
                return False
        
    return True