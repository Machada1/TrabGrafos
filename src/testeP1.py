from libGrafos import Grafo, Aresta, Vertice


def test_grafo():
    print("Testando...")

    # Teste: Criação de um grafo com X vértices
    vertices = 5
    grafo = Grafo(vertices)
    print(f"Grafo criado com {vertices} vértices: {grafo}")

    # Teste: Adição e remoção de arestas
    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(1, 2)
    print("Arestas adicionadas: (0, 1), (1, 2)")
    grafo.remover_aresta(1, 2)
    print("Aresta (1, 2) removida.")

    # Teste: Ponderação e rotulação de vértices
    grafo.rotular_vertice(0, "A")
    grafo.ponderar_vertice(0, 10)
    print(f"Vértice 0 rotulado como 'A' com peso 10.")

    # Teste: Ponderação e rotulação de arestas
    grafo.ponderar_aresta(0, 1, 5)
    grafo.rotular_aresta(0, 1, "aresta01")
    print(f"Aresta (0, 1) rotulada como 'aresta01' com peso 5.")

    # Teste: Checagem de adjacência entre vértices e arestas
    print(f"Vertices 0 e 1 são adjacentes? {grafo.sao_adjacentes(0, 1)}")
    print(f"Aresta (0, 1) existe? {grafo.existe_aresta(0, 1)}")

    # Teste: Checagem da quantidade de vértices e arestas
    print(f"Quantidade de vértices: {grafo.numero_vertices()}")
    print(f"Quantidade de arestas: {grafo.numero_arestas()}")

    # Teste: Checagem de grafo vazio e completo
    print(f"O grafo está vazio? {grafo.grafo_vazio()}")
    print(f"O grafo é completo? {grafo.grafo_completo()}")

    # Teste: Checagem de conectividade
    print(f"O grafo é simplesmente conexo? {grafo.e_conexo()}")
    print(f"O grafo é fortemente conexo? {grafo.kosaraju()}")

    # Teste: Checagem de ponte e articulação
    print(f"O grafo possui ponte? {grafo.e_ponte()}")
    print(f"O grafo possui articulação? {grafo.e_articulacao()}")

    print("Todos os testes executados.")

if __name__ == "__main__":
    test_grafo()
