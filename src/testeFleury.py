from libGrafos import Grafo, Direcionado

#Não Direcionado
grafo = Grafo(4)

print("Grafo não direcionado")
grafo.adicionar_aresta(0,1) # Semi Euleriano
grafo.adicionar_aresta(1,2) # Semi Euleriano
grafo.adicionar_aresta(2,3) # Semi Euleriano
grafo.adicionar_aresta(3,0) # Euleriano
#grafo.adicionar_aresta(1,3) # Não Euleriano

grafo.fleury_naive()
grafo.fleury_tarjan()
print("\n\n")

#Direcionado
dir = Direcionado(4)

print("Grafo direcionado")
dir.adicionar_aresta(0,1) #Semi Euleriano
dir.adicionar_aresta(1,2) #Semi Euleriano
dir.adicionar_aresta(2,3) #Semi Euleriano
dir.adicionar_aresta(3,0) #Euleriano
dir.adicionar_aresta(1,3) #Não euleriano

print(dir.euleriano())
dir.fleury_naive()
dir.fleury_tarjan()
dir.fleury_naive()