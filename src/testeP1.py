from libGrafos import Grafo, Aresta, Vertice

#Cria vértices do Grafo
grafo = Grafo(4)
#Rotula e pondera vértices criados.
grafo.rotular_vertices(["A", "B", "C","D"])
grafo.ponderar_vertices([1,2,3,4])
grafo.imprimir_vertices()

#Cria, rotula e pondera arestas
grafo.imprimir_arestas()
grafo.adicionar_aresta("A","B")
grafo.adicionar_aresta(1,2)
grafo.adicionar_aresta("C", 3)
grafo.ponderar_arestas([4,3,2])
grafo.imprimir_arestas()

#Imprime matrizes e lista
# grafo.imprimir_lista_adjacencia()
# grafo.imprimir_matriz_adjacencia()
# grafo.imprimir_matriz_incidencia()

#Remove aresta
# grafo.remover_aresta((2,3))

#Reimprime matrizes e lista
# grafo.imprimir_lista_adjacencia()
# grafo.imprimir_matriz_adjacencia()
# grafo.imprimir_matriz_incidencia()

#Checa adjacencia entre arestas
grafo.sao_adjacentesA((1,2),(2,3))
grafo.sao_adjacentesA((0,1),(2,3))

#Checa adjacencia entre vértices
grafo.sao_adjacentesV(0,1)
grafo.sao_adjacentesV(0,3)

#Checa existencia aresta
grafo.existe_aresta(1,2)
grafo.existe_aresta(0,2)

#Checa numero de vértices e arestas
grafo.numero_arestas()
grafo.numero_vertices()

#Checa grafo vazio e completo
grafo.grafo_vazio()
grafo.grafo_completo()

#Checa se é conexo
grafo.e_conexo()
grafo.remover_aresta((1,2))
grafo.e_conexo()








#testa função de gerar grafo aleatório
grafo = Grafo(10)
grafo.graforandom(0)
grafo.imprimir_vertices()
grafo.imprimir_arestas()

grafo.imprimir_lista_adjacencia()
grafo.imprimir_matriz_adjacencia()
grafo.imprimir_matriz_incidencia()