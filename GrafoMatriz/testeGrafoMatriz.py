# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 14:23:05 2023

@author: icalc
"""
from grafoMatriz import Grafo

g = Grafo(4)
#insere as arestas do grafo
#A={(0,1),(0,2),(2,1),(2,3),(1,3)}
g.insereA(0,1)
g.insereA(0,2)
g.insereA(2,1)
g.insereA(2,3)
g.insereA(1,3)
# g.insereA(3,0)
# mostra o grafo preenchido
# g.inDegree(1)
# g.outDegree(1)

# g.fonte(1)
g.showMin()

g.removeV(0)

# g.show()
g.showMin()

# g.createGraphFromFile('instructions.txt')
g.isComplete()

ctg = g.conexidade_categoria()
print(f"G é C{ctg}")

print(g.grafoReduzido())
