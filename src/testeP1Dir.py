from libGrafos import Grafo, Direcionado

Dir = Direcionado(3)
Dir.rotular_vertices(["A", "B", "C"])
Dir.ponderar_vertices([1,2,3])

Dir.adicionar_aresta(0,1,"AB",5)
Dir.adicionar_aresta(1,2,"BC",10)
Dir.adicionar_aresta(2,0,"CA",1)

Dir.e_conexo()

Dir.imprimir_lista_adjacencia()
Dir.imprimir_matriz_adjacencia()
Dir.imprimir_matriz_incidencia()

Dir.sao_adjacentesA((0,1),(1,2))
Dir.sao_adjacentesA((1,2),(2,0))

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

Dir.kosaraju()

Dir.conectividade()
Dir.remover_aresta((2,0))
Dir.conectividade()
Dir.remover_aresta((1,2))
Dir.e_conexo()
Dir.conectividade()