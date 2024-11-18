from libGrafos import Grafo
from libGrafos import Vertice
from libGrafos import Aresta

grafo = Grafo(10)
grafo.imprimir_vertices()

rotulos = ['a','b','c','d','e','f','g','h','i','j']
grafo.rotular_vertices(rotulos)
grafo.imprimir_vertices()

pesos = [10,20,30,40,50,60,70,80,90,100]
grafo.ponderar_vertices(pesos)
grafo.imprimir_vertices()

grafo.adicionar_aresta(0,1)
grafo.adicionar_aresta(2,3)
grafo.adicionar_aresta(4,5)
grafo.adicionar_aresta(6,7)
grafo.adicionar_aresta(8,9)
grafo.imprimir_arestas()