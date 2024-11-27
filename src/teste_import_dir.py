import xml.etree.ElementTree as ET
from libGrafos import Direcionado
from libGrafos import process_gexf

file_path = "../TrabGrafos/TESTEEXPORT.gexf"

nodes, edges , tipo = process_gexf(file_path)
indices = []
rotulos = []
print(tipo)
for vertice,propertys in nodes.items():
    indices.append(vertice)
    rotulos.append(propertys['label'])

grafo = Direcionado(len(indices))
grafo.rotular_vertices(rotulos)

for aresta in edges:
    u = int(aresta['source'])
    v = int(aresta['target'])
    peso = int(aresta['label'])
    grafo.adicionar_aresta(u,v,None,peso)

grafo.fleury_naive()
grafo.fleury_tarjan()
grafo.kosaraju()