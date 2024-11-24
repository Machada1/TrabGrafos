from libGrafos import Grafo, Direcionado

Dir = Direcionado(7)

Dir.adicionar_aresta(0,1)
Dir.adicionar_aresta(1,4)
Dir.adicionar_aresta(4,2)
Dir.adicionar_aresta(2,1)
Dir.adicionar_aresta(0,3)
Dir.adicionar_aresta(4,6)
Dir.adicionar_aresta(6,5)
Dir.adicionar_aresta(5,6)
Dir.adicionar_aresta(2,5)
Dir.adicionar_aresta(3,5)

Dir.imprimir_lista_adjacencia()
Dir.imprimir_matriz_adjacencia()
Dir.imprimir_matriz_incidencia()

Dir.kosaraju()