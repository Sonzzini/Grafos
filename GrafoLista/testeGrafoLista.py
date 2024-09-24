import sys
import os
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from grafoLista import Grafo

# # Ex 17
# grafo1 = Grafo(3)
# grafo1.insereA(0, 1)
# grafo1.insereA(1, 2)

# grafo2 = Grafo(3)
# grafo2.insereA(0, 1)
# grafo2.insereA(1, 2)

# grafo3 = Grafo(3)
# grafo3.insereA(0, 1)
# grafo3.insereA(1, 0)

# print(grafo1.isEqual(grafo2))  # Deve retornar True
# print(grafo1.isEqual(grafo3))  # Deve retornar False

# # Ex 18
# matriz_adjacencia = np.array([
#     [0, 1, 0],
#     [0, 0, 1],
#     [1, 0, 0]
# ])

# grafo = Grafo.fromMatrizToList(matriz_adjacencia)
# grafo.show()

# # Ex 19
# grafo = Grafo(3)
# grafo.insereA(0, 1)
# grafo.insereA(0, 2)
# grafo.insereA(1, 2)

# print("Antes de inverter:")
# grafo.show()

# grafo.invertAdjList()

# print("Depois de inverter:")
# grafo.show()

# # Ex 20
# grafo = Grafo(3)
# grafo.insereA(0, 1)
# grafo.insereA(0, 2)
# grafo.insereA(1, 2)

# print("Grafo:")
# grafo.show()

# print(f"O vértice 0 é uma fonte? {grafo.isSource(0)}")  # Deve retornar 1
# print(f"O vértice 1 é uma fonte? {grafo.isSource(1)}")  # Deve retornar 0
# print(f"O vértice 2 é uma fonte? {grafo.isSource(2)}")  # Deve retornar 0

# # Ex 21
# grafo = Grafo(3)
# grafo.insereA(0, 1)
# grafo.insereA(0, 2)
# grafo.insereA(1, 2)

# print("Grafo:")
# grafo.show()

# print(f"O vértice 0 é um sorvedouro? {grafo.isSorvedouro(0)}")  # Deve retornar 0
# print(f"O vértice 1 é um sorvedouro? {grafo.isSorvedouro(1)}")  # Deve retornar 0
# print(f"O vértice 2 é um sorvedouro? {grafo.isSorvedouro(2)}")  # Deve retornar 1

# # Ex 22
# grafo1 = Grafo(3)
# grafo1.insereA(0, 1)
# grafo1.insereA(1, 0)
# grafo1.insereA(1, 2)
# grafo1.insereA(2, 1)

# grafo2 = Grafo(3)
# grafo2.insereA(0, 1)
# grafo2.insereA(1, 2)

# print("Grafo 1:")
# grafo1.show()
# print(f"O grafo 1 é simétrico? {grafo1.isSymetric()}")  # Deve retornar 1

# print("Grafo 2:")
# grafo2.show()
# print(f"O grafo 2 é simétrico? {grafo2.isSymetric()}")  # Deve retornar 0

# # Ex 23
# nome_arquivo = 'grafo.txt'
# grafo = Grafo.adjListBuilder(nome_arquivo)

# print("Grafo carregado do arquivo:")
# grafo.show()

# # Ex 24
# grafo = Grafo(6)
# grafo.insereA(0, 1)
# grafo.insereA(0, 5)
# grafo.insereA(1, 5)
# grafo.insereA(2, 4)
# grafo.insereA(3, 1)
# grafo.insereA(4, 3)
# grafo.insereA(3, 5)

# print("Grafo original:")
# grafo.show()

# # Remover o vértice 3
# grafo.removeV(3)

# print("Grafo após remover o vértice 3:")
# grafo.show()

# # Ex 25
# grafo = Grafo(6)
# grafo.insereA(0, 1)
# grafo.insereA(0, 5)
# grafo.insereA(1, 5)
# grafo.insereA(2, 4)
# grafo.insereA(3, 1)
# grafo.insereA(4, 3)
# grafo.insereA(3, 5)

# print("Grafo original:")
# grafo.show()

# # Remover o vértice 3
# grafo.removeVD(3)

# print("Grafo após remover o vértice 3:")
# grafo.show()

# # Ex 26
# grafo1 = Grafo(4)
# grafo1.insereA(0, 1)
# grafo1.insereA(0, 2)
# grafo1.insereA(0, 3)
# grafo1.insereA(1, 0)
# grafo1.insereA(1, 2)
# grafo1.insereA(1, 3)
# grafo1.insereA(2, 0)
# grafo1.insereA(2, 1)
# grafo1.insereA(2, 3)
# grafo1.insereA(3, 0)
# grafo1.insereA(3, 1)
# grafo1.insereA(3, 2)

# print("Grafo 1 é completo?", grafo1.eh_completo())  # Deve retornar True

# grafo2 = Grafo(4)
# grafo2.insereA(0, 1)
# grafo2.insereA(0, 2)
# grafo2.insereA(1, 2)
# grafo2.insereA(2, 3)

# print("Grafo 2 é completo?", grafo2.eh_completo())  # Deve retornar False

# Exemplo de uso
nome_arquivo = 'grafo.txt'
grafo = Grafo()
grafo = grafo.cria_grafo_de_arquivo(nome_arquivo)
grafo.show()