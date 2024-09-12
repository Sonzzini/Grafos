import networkx as nx
import matplotlib.pyplot as plt

# Criar o grafo
metro_sp = nx.Graph()

# Adicionar as estações da Linha 1 - Azul
linha1_azul = [
    "Linha1_Azul_Jabaquara", "Linha1_Azul_Conceição", "Linha1_Azul_Saúde",
    "Linha1_Azul_Praça_da_Árvore", "Linha1_Azul_Santa_Cruz", 
    "Linha1_Azul_Vila_Mariana", "Linha1_Azul_Ana_Rosa", "Linha1_Azul_Paraíso",
    "Linha1_Azul_Vergueiro", "Linha1_Azul_São_Joaquim", "Linha1_Azul_Liberdade", 
    "Linha1_Azul_Se", "Linha1_Azul_Sao_Bento", "Linha1_Azul_Luz", 
    "Linha1_Azul_Tiradentes", "Linha1_Azul_Armênia", "Linha1_Azul_Portuguesa_Tietê",
    "Linha1_Azul_Caruara", "Linha1_Azul_Tucuruvi"
]

# Adicionar as estações da Linha 2 - Verde
linha2_verde = [
    "Linha2_Verde_Vila_Madalena", "Linha2_Verde_Sumaré", "Linha2_Verde_Clinicas", 
    "Linha2_Verde_Consolação", "Linha2_Verde_Trianon_MASP", 
    "Linha2_Verde_Brigadeiro", "Linha2_Verde_Paraíso", 
    "Linha2_Verde_Ana_Rosa", "Linha2_Verde_Chácara_Klabin", 
    "Linha2_Verde_Santos_Imigrantes", "Linha2_Verde_Alto_do_Ipiranga", 
    "Linha2_Verde_Sacoma", "Linha2_Verde_Tamanduateí", "Linha2_Verde_Vila_Prudente"
]

# Adicionar as estações da Linha 3 - Vermelha
linha3_vermelha = [
    "Linha3_Vermelha_Palmeiras_Barra_Funda", "Linha3_Vermelha_Marechal_Deodoro", 
    "Linha3_Vermelha_Santa_Cecilia", "Linha3_Vermelha_República", 
    "Linha3_Vermelha_Anhangabaú", "Linha3_Vermelha_Se", 
    "Linha3_Vermelha_Brás", "Linha3_Vermelha_Belém", 
    "Linha3_Vermelha_Tatuapé", "Linha3_Vermelha_Carrão", 
    "Linha3_Vermelha_Penha", "Linha3_Vermelha_Guilhermina_Esperança", 
    "Linha3_Vermelha_Patriarca", "Linha3_Vermelha_Artur_Alvim", 
    "Linha3_Vermelha_Corinthians_Itaquera"
]

# Adicionar nós (estações)
metro_sp.add_nodes_from(linha1_azul)
metro_sp.add_nodes_from(linha2_verde)
metro_sp.add_nodes_from(linha3_vermelha)

# Adicionar arestas da Linha 1 - Azul
for i in range(len(linha1_azul) - 1):
    metro_sp.add_edge(linha1_azul[i], linha1_azul[i+1])

# Adicionar arestas da Linha 2 - Verde
for i in range(len(linha2_verde) - 1):
    metro_sp.add_edge(linha2_verde[i], linha2_verde[i+1])

# Adicionar arestas da Linha 3 - Vermelha
for i in range(len(linha3_vermelha) - 1):
    metro_sp.add_edge(linha3_vermelha[i], linha3_vermelha[i+1])

# Adicionar conexões entre as linhas (transferências)
metro_sp.add_edge("Linha1_Azul_Paraíso", "Linha2_Verde_Paraíso")
metro_sp.add_edge("Linha1_Azul_Ana_Rosa", "Linha2_Verde_Ana_Rosa")
metro_sp.add_edge("Linha1_Azul_Se", "Linha3_Vermelha_Se")

# Cores para cada linha
color_map = []
for node in metro_sp:
    if node.startswith("Linha1_Azul"):
        color_map.append('blue')
    elif node.startswith("Linha2_Verde"):
        color_map.append('green')
    elif node.startswith("Linha3_Vermelha"):
        color_map.append('red')

# Desenhar o grafo com cores
pos = nx.spring_layout(metro_sp)  # Layout para distribuir os nós de forma organizada
pos2 = nx.planar_layout(metro_sp)
pos3 = nx.kamada_kawai_layout(metro_sp)
nx.draw(metro_sp, pos, with_labels=False, node_color=color_map, node_size=500, font_size=10, font_weight='bold', edge_color='gray')

# Mostrar o grafo
plt.show()
