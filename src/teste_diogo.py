from libGrafos import Grafo
from libGrafos import Vertice
from libGrafos import Aresta

grafo = Grafo(10)
grafo.grafo_vazio()
grafo.imprimir_vertices()
print("\n")

rotulosErro = ['a','b','c','d','e','f','g','h','i',]
grafo.rotular_vertices(rotulosErro)
rotulos = ['a','b','c','d','e','f','g','h','i','j']
grafo.rotular_vertices(rotulos)
grafo.imprimir_vertices()
print("\n")

pesosErro = [10,20,30,40,50,60,70,80,90,100,110]
grafo.ponderar_vertices(pesosErro)
pesos = [10,20,30,40,50,60,70,80,90,100]
grafo.ponderar_vertices(pesos)
grafo.imprimir_vertices()
print("\n")

grafo.adicionar_aresta(0,1)
grafo.adicionar_aresta('b','c')
grafo.adicionar_aresta(4,5)
grafo.adicionar_aresta(6,7)
grafo.adicionar_aresta(8,9)
grafo.adicionar_aresta(0,9)
grafo.adicionar_aresta(10,11)
grafo.adicionar_aresta(0,1)
grafo.imprimir_arestas()
print("\n")

rotulosAErro = [1,2,3,4,5,6,7]
grafo.rotular_arestas(rotulosAErro)
rotulosA = [1,2,3,4,5,6]
grafo.rotular_arestas(rotulosA)
grafo.imprimir_arestas()
print("\n")


pesosAErro= [100,200,300,400,500]
grafo.ponderar_arestas(pesosAErro)
pesosA= [100,200,300,400,500,600]
grafo.ponderar_arestas(pesosA)
grafo.imprimir_arestas()
print("\n")

grafo.remover_aresta(2)
grafo.remover_aresta((8,9))
grafo.imprimir_arestas()
print("\n")

grafo.sao_adjacentesV(0,1)
grafo.sao_adjacentesV(0,2)
grafo.sao_adjacentesV('a','b')
grafo.sao_adjacentesV(0,11)
print("\n")

grafo.sao_adjacentesA((0,1),(4,5))
grafo.sao_adjacentesA((0,1),(10,11))
grafo.sao_adjacentesA(1,3)
grafo.sao_adjacentesA(1,6)
grafo.imprimir_arestas()
print("\n")

grafo.existe_aresta(1,2)
grafo.existe_aresta(6,7)
print("\n")

grafo.numero_arestas()
grafo.numero_vertices()
print("\n")

grafo.grafo_vazio()
grafo.grafo_completo()
print("\n")

grafo.imprimir_lista_adjacencia()
print("\n")
grafo.imprimir_matriz_adjacencia()
print("\n")
grafo.imprimir_matriz_incidencia()
