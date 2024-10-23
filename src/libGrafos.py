import random

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
        self.matriz_incidencia = []
        self.lista_adjacencia = {i: [] for i in range(num_vertices)}

    # Adiciona uma aresta entre os vértices u e v
    def adicionar_aresta(self, u, v, peso=1):
        # Matriz de Adjacência
        self.matriz_adjacencia[u][v] = peso
        self.matriz_adjacencia[v][u] = peso  # Se for um grafo não-direcionado

        # Lista de Adjacência
        self.lista_adjacencia[u].append((v, peso))
        self.lista_adjacencia[v].append((u, peso))  # Se for um grafo não-direcionado

        # Matriz de Incidência (implementação simples)
        aresta = [0] * self.num_vertices
        aresta[u] = peso
        aresta[v] = peso
        self.matriz_incidencia.append(aresta)

    # Remove uma aresta entre os vértices u e v
    def remover_aresta(self, u, v):
        # Matriz de Adjacência
        self.matriz_adjacencia[u][v] = 0
        self.matriz_adjacencia[v][u] = 0

        # Lista de Adjacência
        self.lista_adjacencia[u] = [vert for vert in self.lista_adjacencia[u] if vert[0] != v]
        self.lista_adjacencia[v] = [vert for vert in self.lista_adjacencia[v] if vert[0] != u]

        # Matriz de Incidência
        for aresta in self.matriz_incidencia:
            if aresta[u] != 0 and aresta[v] != 0:
                self.matriz_incidencia.remove(aresta)
                break

    # Método para imprimir a matriz de adjacência
    def imprimir_matriz_adjacencia(self):
        print("Matriz de Adjacência:")
        # Imprime o cabeçalho das colunas
        print("   " + " ".join(str(i) for i in range(self.num_vertices)))
        for i, linha in enumerate(self.matriz_adjacencia):
            # Imprime o índice da linha à esquerda
            print(f"{i} | " + " ".join(map(str, linha)))

    # Método para imprimir a matriz de incidência
    def imprimir_matriz_incidencia(self):
        print("Matriz de Incidência:")
        if not self.matriz_incidencia:  # Verifica se a matriz de incidência está vazia
            print("A matriz de incidência está vazia.")
            return
        # Imprime o cabeçalho das colunas
        print("   " + " ".join(str(i) for i in range(len(self.matriz_incidencia[0]))))
        for i, linha in enumerate(self.matriz_incidencia):
            # Imprime o índice da linha à esquerda
            print(f"{i} | " + " ".join(map(str, linha)))

    # Método para imprimir a lista de adjacência
    def imprimir_lista_adjacencia(self):
        print("Lista de Adjacência:")
        for vertice, adjacentes in self.lista_adjacencia.items():
            print(f"{vertice}: {adjacentes}")

    # Pondera e rotula vértices
    def rotular_vertice(self, vertice, rotulo):
        print(f"Vértice {vertice} rotulado como {rotulo}")

    # Pondera e rotula arestas
    def rotular_aresta(self, u, v, rotulo):
        print(f"Aresta entre {u} e {v} rotulada como {rotulo}")

    # Checa se dois vértices são adjacentes
    def sao_adjacentes(self, u, v):
        return self.matriz_adjacencia[u][v] != 0

    # Checa se uma aresta existe entre dois vértices
    def existe_aresta(self, u, v):
        return self.matriz_adjacencia[u][v] != 0

    # Checa o número de vértices
    def numero_vertices(self):
        return self.num_vertices

    # Checa o número de arestas
    def numero_arestas(self):
        return len(self.matriz_incidencia)

    # Checa se o grafo está vazio
    def grafo_vazio(self):
        return all(all(peso == 0 for peso in linha) for linha in self.matriz_adjacencia)

    # Checa se o grafo é completo
    def grafo_completo(self):
        for u in range(self.num_vertices):
            for v in range(self.num_vertices):
                if u != v and self.matriz_adjacencia[u][v] == 0:
                    return False
        return True

    # Checa a conectividade do grafo (simplismente conexo)
    def e_conexo(self):
        visitados = [False] * self.num_vertices

        def dfs(v):
            visitados[v] = True
            for vizinho, _ in self.lista_adjacencia[v]:
                if not visitados[vizinho]:
                    dfs(vizinho)

        dfs(0)
        return all(visitados)

    # Algoritmo de Kosaraju para componentes fortemente conexos
    def kosaraju(self):
        # Algoritmo simplificado para detectar componentes fortemente conexos
        # Passo 1: DFS normal
        visitados = [False] * self.num_vertices
        ordem = []

        def dfs(v):
            visitados[v] = True
            for vizinho, _ in self.lista_adjacencia[v]:
                if not visitados[vizinho]:
                    dfs(vizinho)
            ordem.append(v)

        for v in range(self.num_vertices):
            if not visitados[v]:
                dfs(v)

        # Passo 2: Transpor o grafo
        grafo_transposto = Grafo(self.num_vertices)
        for u in range(self.num_vertices):
            for v, peso in self.lista_adjacencia[u]:
                grafo_transposto.adicionar_aresta(v, u, peso)

        # Passo 3: DFS no grafo transposto na ordem inversa
        visitados = [False] * self.num_vertices
        componentes = []

        def dfs_transposto(v, componente):
            visitados[v] = True
            componente.append(v)
            for vizinho, _ in grafo_transposto.lista_adjacencia[v]:
                if not visitados[vizinho]:
                    dfs_transposto(vizinho, componente)

        for v in reversed(ordem):
            if not visitados[v]:
                componente = []
                dfs_transposto(v, componente)
                componentes.append(componente)

        return componentes

    # Checa se há uma ponte (aresta cuja remoção desconecta o grafo)
    def e_ponte(self, u, v):
        self.remover_aresta(u, v)
        conexo_sem_aresta = self.e_conexo()
        self.adicionar_aresta(u, v)  # Restaurar aresta
        return not conexo_sem_aresta

    # Checa se um vértice é um ponto de articulação (vértice cuja remoção desconecta o grafo)
    def e_articulacao(self, vertice):
        original_adjacentes = self.lista_adjacencia[vertice][:]
        for vizinho, peso in original_adjacentes:
            self.remover_aresta(vertice, vizinho)

        conexo_sem_vertice = self.e_conexo()

        # Restaurar as arestas removidas
        for vizinho, peso in original_adjacentes:
            self.adicionar_aresta(vertice, vizinho, peso)

        return not conexo_sem_vertice

    # Função para gerar um grafo aleatório
    def graforandom(self, num_arestas):
        for _ in range(num_arestas):
            u = random.randint(0, self.num_vertices - 1)
            v = random.randint(0, self.num_vertices - 1)
            print(f"Aresta adicionada: {u} - {v}")
            while u == v or self.existe_aresta(u, v):
                u = random.randint(0, self.num_vertices - 1)
                v = random.randint(0, self.num_vertices - 1)
            self.adicionar_aresta(u, v,)