from libGrafos import Grafo, Direcionado

#Não Direcionado
grafo = Grafo(10)

print("Grafo não direcionado")
grafo.adicionar_aresta(0,1)
grafo.adicionar_aresta(1,2) 
grafo.adicionar_aresta(2,3) 
grafo.adicionar_aresta(3,4) 

grafo.adicionar_aresta(5,6)
grafo.adicionar_aresta(6,7)
grafo.adicionar_aresta(7,8) 
grafo.adicionar_aresta(8,9) 

grafo.kosaraju()
grafo.fleury_naive()
grafo.fleury_tarjan()
print("\n\n")

#Direcionado
dir = Direcionado(10)

print("Grafo direcionado")
dir.adicionar_aresta(0,1)
dir.adicionar_aresta(1,2) 
dir.adicionar_aresta(2,3) 
dir.adicionar_aresta(3,4) 

dir.adicionar_aresta(5,6)
dir.adicionar_aresta(6,7)
dir.adicionar_aresta(7,8) 
dir.adicionar_aresta(8,9) 

grafo.kosaraju()
print(dir.euleriano())
dir.fleury_naive()
dir.fleury_tarjan()
dir.fleury_naive()