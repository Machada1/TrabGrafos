from libGrafos import Grafo

grafo = Grafo(5)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)

grafo.imprimir_matriz_adjacencia()
grafo.imprimir_matriz_incidencia()
grafo.imprimir_lista_adjacencia()