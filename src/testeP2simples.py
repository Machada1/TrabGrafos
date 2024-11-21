from libGrafos import Grafo

grafo = Grafo(5)

grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(2, 4)
grafo.adicionar_aresta(3, 0)


# Como a remoção da aresta (2, 3) desconecta o grafo, deve ser uma ponte
grafo.e_ponte(2, 4)

# A remoção de (0, 1) não deve desconectar o grafo
grafo.e_ponte(0, 1)
grafo.e_ponte(1, 2)
grafo.e_ponte(2, 3)
grafo.e_ponte(3, 0)

#  Como a remoção do vértice 2 desconecta o grafo, deve ser  articulação
grafo.e_articulacao(2)

# Como a remoção do vértice 0 não desconecta o grafo, não deve ser articulação
grafo.e_articulacao(0)
