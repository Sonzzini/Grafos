import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from create_graph_from_txt import make_graph_from_txt as create_from_txt
from create_graph_from_txt import make_txt_from_graph as create_txt_from
from GrafoLista.grafoLista import Grafo

from typing import List


def presentMenu():
    print("""----------------------------------------------
0 - Ler dados do arquivo
1 - Gravar dados no arquivo
2 - Inserir vértice
3 - Inserir aresta
4 - Remover vértice
5 - Remover aresta
6 - Mostrar conteúdo do arquivo
7 - Mostrar grafo
8 - Mostrar conexão do grafo e o reduzido
9 - Encerrar
----------------------------------------------""")

def handle_selection(selection: int, grafo_f: List[Grafo]):
    if selection == 0:
        grafo = create_from_txt('Projeto/grafo.txt')
        print("Arquivo 'grafo.txt' lido com sucesso")
        grafo_f[0] = grafo
    

    elif selection == 1:
        nome_arquivo = str(input("Digite o nome do arquivo para ser escrito: "))
        create_txt_from(nome_arquivo, grafo_f)
    

    elif selection == 2:  # Inserir vértice
        grafo_f[0].insereV()
        print("Vértice inserido no grafo com sucesso.")


    elif selection == 3:  # Inserir aresta
        while True:
            option = int(input("Gostaria de inserir uma aresta com peso ou sem peso?\n1 - Com peso\n2 - Sem peso\n"))

            if option == 1:
                print("-- Inserindo aresta com peso --")
                v1, v2, peso = int(input("Formato [v1] [v2] [peso]").split())
                grafo_f[0].insereA_com_peso(v1, v2, peso)
                print(f"Aresta de valor {peso} entre {v1} e {v2} adicionada com sucesso.")
                break

            elif option == 2:
                print("-- Inserindo aresta sem peso (peso - 1) --")
                v1, v2 = int(input("Formato [v1] [v2]").split())
                grafo_f[0].insereA_com_peso(v1, v2, 1)
                print(f"Aresta entre {v1} e {v2} adicionada com sucesso.")
                break

            else:
                print("Erro.\nPor favor escolha:\n1 - Inserir aresta com peso\n2 - Inserir aresta sem peso\n")

    elif selection == 4: # Remover vértice
        vertice = int(input("Digite o vértice a ser removido:"))
        print(vertice)
        grafo_f[0].removeV(vertice)

    elif selection == 5: # Remover aresta
        vertice1 = int(input("Digite o primeiro elemento da aresta a ser removida:"))
        vertice2 = int(input("Digite o segundo elemento da aresta a ser removida:"))
        grafo_f[0].removeA(vertice1, vertice2)

    elif selection == 6:  # Mostrar conteúdo do arquivo
        print("Mostrando conteúdo do arquivo 'Projeto/grafo.txt':", end="\n\n")
        arquivo = 'Projeto/grafo.txt'
        with open(arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            print(linhas)

    
    elif selection == 7:  # Mostrar grafo
        grafo_f[0].show_as_matrix()

    
    elif selection == 8:
        # Mostrar conexão do grafo
        # Grafo reduzido
        ...


    elif selection == 9:
        print("Encerrando o programa...")


def main():

    grafo = [Grafo(0)]

    while True:
        presentMenu()
        selection = int(input())

        handle_selection(selection, grafo)

        if selection == 9:
            break
    


main()
