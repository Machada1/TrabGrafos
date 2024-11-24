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

Dir.sao_adjacentesA((0,1),(1,2))
Dir.sao_adjacentesA((0,1),(2,3))

Dir.existe_aresta(0,1)
Dir.existe_aresta(1,2)
Dir.existe_aresta(2,0)
Dir.existe_aresta(0,2)
Dir.existe_aresta(2,1)
Dir.existe_aresta(1,0)

Dir.numero_arestas()
Dir.numero_vertices()

Dir.grafo_vazio()
Dir.grafo_completo()

Dir.e_ponte(2,3) #É
Dir.e_ponte(2,0) #Não é

Dir.e_articulacao(1)
Dir.e_articulacao(2)

Dir.kosaraju()

Dir.conectividade()
Dir.remover_aresta((2,0))
Dir.conectividade()
Dir.remover_aresta((1,2))
Dir.e_conexo()
Dir.conectividade()


print(Dir.euleriano())
Dir.remover_aresta((2,3))
print(Dir.euleriano())