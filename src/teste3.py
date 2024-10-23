from libGrafos import Grafo # Para um grafo com 100 vértices e aproximadamente 500 arestas

grafo_100 = Grafo(100)
grafo_100.graforandom(200)

grafo_100.imprimir_lista_adjacencia()
grafo_100.imprimir_matriz_adjacencia()
grafo_100.imprimir_matriz_incidencia()