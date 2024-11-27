from libGrafos import Grafo,Direcionado

grafo = Grafo(5)
grafo.adicionar_aresta(0,1)
grafo.adicionar_aresta(1,2)
grafo.adicionar_aresta(2,3)
grafo.adicionar_aresta(3,4)
grafo.rotular_vertices(['a','b','c','d','e'])
grafo.ponderar_vertices([10,20,30,40,50])
grafo.rotular_arestas(['A','B','C','D'])
grafo.ponderar_arestas([100,200,300,400])
grafo.salvar_grafo_gexf('teste')