from libGrafos import Grafo

grafo = Grafo(5)

grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)
grafo.adicionar_aresta(3, 0)



# É ponte
grafo.e_ponte(3, 4)

# Não é ponte
grafo.e_ponte(0, 1)
grafo.e_ponte(1, 2)
grafo.e_ponte(2, 3)
grafo.e_ponte(3, 0)

# É articulação
grafo.e_articulacao(3)

# Não é articulação
grafo.e_articulacao(1)
grafo.e_articulacao(2)
grafo.e_articulacao(4)
grafo.e_articulacao(0)





