from libGrafos import Grafo


grafo = Grafo(5)
grafo.graforandom(0)
grafo.adicionar_aresta(1,3)

grafo.imprimir_arestas()
grafo.imprimir_lista_adjacencia()
grafo.imprimir_matriz_adjacencia()
grafo.imprimir_matriz_incidencia()
grafo.imprimir_vertices()