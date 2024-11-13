from libGrafos import Grafo
from libGrafos import Vertice
from libGrafos import Aresta

# Criação do grafo
grafo = Grafo(9)
grafo.imprimir_vertices()
rotulos=['a','b','c','d','e','f','g','h','i']
pesos=[10,20,30,40,50,60,70,80,90]
grafo.rotular_vertices(rotulos)
grafo.ponderar_vertices(pesos)
grafo.imprimir_vertices()
# grafo.adicionar_aresta(0, 1)
# grafo.adicionar_aresta(0, 2)
# grafo.adicionar_aresta(1, 3)
# grafo.adicionar_aresta(2, 3)
# grafo.adicionar_aresta(3, 4)
# grafo.adicionar_aresta(4, 5)
# grafo.adicionar_aresta(5, 6)
# grafo.adicionar_aresta(6, 7)
# grafo.adicionar_aresta(7, 8)

# Rotulação e ponderação do grafo
# grafo.rotular_aresta(0,1,"aresta 1")
# grafo.rotular_vertice(0,'primeiro')

# Teste de impreção
# grafo.imprimir_matriz_aresta()
# grafo.imprimir_matriz_vertice()
# grafo.imprimir_lista_adjacencia()

# Teste de manipulação
# grafo.remover_aresta(0,1)

# Impreção novamente
# grafo.imprimir_matriz_aresta()
# grafo.imprimir_matriz_adjacencia()
# grafo.imprimir_matriz_incidencia()
# grafo.imprimir_lista_adjacencia()

# grafo.sao_adjacentes(0,1)
