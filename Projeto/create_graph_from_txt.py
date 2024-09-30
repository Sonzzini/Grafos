import sys
import os
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from GrafoLista.grafoLista import Grafo


def make_graph_from_txt(nome_arquivo: str) -> Grafo:
     with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
        tipo_grafo = int(linhas[0].strip())
        if tipo_grafo != 2:
            raise ValueError(f"Tipo de grafo ({tipo_grafo}) não suportado. Apenas grafos do tipo 2 são suportados.")
        
        n = int(linhas[1].strip().split()[0])
        grafo = Grafo(n)
        
        # Ignorando os vértices e seus apelidos/pesos (linhas de 2 a n+1)
        indice_linha = 2 + n
        
        m = int(linhas[indice_linha].strip().split()[0])
        indice_linha += 1
        
        for i in range(m):
            aresta = linhas[indice_linha + i].strip().split()
            v = int(aresta[0]) - 1  # Convertendo para índice 0-based
            w = int(aresta[1]) - 1  # Convertendo para índice 0-based
            value = int(aresta[2])
            # Ignorando o peso da aresta, se houver
            grafo.insereA_com_peso(v, w, value)
            grafo.insereA_com_peso(w, v, value)
        
        return grafo


def make_txt_from_graph(nome_arquivo: str, grafo_f: List[Grafo]):
    grafo = grafo_f[0]

    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write("2\n")
        arquivo.write(str(grafo.n)+"\n")
        
        for i in range(grafo.n):
            arquivo.write(str(i)+"\n")
        
        arquivo.write(str(grafo.m)+"\n")

        for j in range(grafo.n):
            for k in range(len(grafo.listaAdj[j])):
                aresta = grafo.listaAdj[j][k]
                arquivo.write(f"{j} {aresta[0]} {aresta[1]}\n")