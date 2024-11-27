import xml.etree.ElementTree as ET
from libGrafos import Grafo

def process_gexf(file_path):

    tree = ET.parse(file_path)
    root = tree.getroot()

    namespace = {'ns': 'http://www.gexf.net/1.3draft'}

    nodes = {}
    edges = []

    for node in root.findall('.//ns:node', namespace):
        node_id = node.attrib['id']
        label = node.attrib.get('label', '')
        weight = node.attrib.get('weight', '0')
        nodes[node_id] = {'label': label, 'weight': float(weight)}

    for edge in root.findall('.//ns:edge', namespace):
        edge_id = edge.attrib['id']
        source = edge.attrib['source']
        target = edge.attrib['target']
        label = edge.attrib.get('label', '')
        edges.append({'id': edge_id, 'source': source, 'target': target, 'label': label})

    return nodes, edges

file_path = "../TrabGrafos/nãoDirecionado"

nodes, edges = process_gexf(file_path)

indices = []
rotulos = []
pesos = []

for vertice,propertys in nodes.items():
    indices.append(vertice)
    rotulos.append(propertys['label'])
    pesos.append(propertys['weight'])

grafo = Grafo(len(indices))
grafo.rotular_vertices(rotulos)
grafo.ponderar_vertices(pesos)

for aresta in edges:
    u = int(aresta['source'])
    v = int(aresta['target'])
    peso = aresta['label']
    grafo.adicionar_aresta(u,v,None,peso)


grafo.fleury_tarjan()
grafo.fleury_naive()
grafo.kosaraju()