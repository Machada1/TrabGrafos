import random

class Vertice:
    def __init__(self, indice, rotulo=None, peso=None):
        self.indice = indice
        self.rotulo = rotulo
        self.peso = peso
    
    def rotular_vertice(self, rotulo):
        self.rotulo = rotulo 

    def ponderar_vertice(self, peso):
        self.peso = peso 

    def imprimir_vertice(self):
        print(f'Vertice: {self.indice}, Rotulo: {self.rotulo}, Peso: {self.peso}')

class Aresta:
    def __init__(self, saida, chegada, rotulo=None, peso=1):
        self.Vsaida = saida
        self.Vchegada = chegada
        self.rotulo = rotulo
        self.peso = peso

    def rotular_aresta(self, rotulo):
        self.rotulo = rotulo

    def ponderar_aresta(self, peso):
        self.peso = peso

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_arestas = 0
        self.array_vertices = []
        self.array_arestas = []
        for i in range(num_vertices):
            self.array_vertices.append(Vertice(i))
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
        self.matriz_incidencia = []
        self.lista_adjacencia = {i: [] for i in range(num_vertices)}

    # Rotula os vertices do grafo
    def rotular_vertices(self,rotulos):
        if len(rotulos) == len(self.array_vertices):
            for i,rotulo in enumerate(rotulos):
                self.array_vertices[i].rotular_vertice(rotulo)
        else:
            print(f'A quantidade de rotulos fornecida não condiz com a quantidade de vertices do grafo. Faltam {len(self.array_vertices)-len(rotulos)} rotulos')

    # Pondera os vertices do grafo
    def ponderar_vertices(self,pesos):
        if len(pesos) == len(self.array_vertices):
            for i,peso in enumerate(pesos):
                self.array_vertices[i].ponderar_vertice(peso)
        else:
            print(f'A quantidade de pesos fornecida não condiz com a quantidade de vertices do grafo. Faltam {len(self.array_vertices)-len(pesos)} pesos')

    # Imprime os vertices do grafo com seus rotulos e pesos
    def imprimir_vertices(self):
        for i in range(len(self.array_vertices)):
            self.array_vertices[i].imprimir_vertice()

    # Adiciona uma aresta entre os vértices u e v
    def adicionar_aresta(self, u, v):
        if u<self.num_vertices and v<self.num_vertices:
            #Matriz de aresta
            self.matriz_aresta.append([(u,v)])

            # Matriz de Adjacência
            self.matriz_adjacencia[u][v] = 1
            self.matriz_adjacencia[v][u] = 1  # Se for um grafo não-direcionado

            # Lista de Adjacência
            self.lista_adjacencia[u].append(v)
            self.lista_adjacencia[v].append(u)  # Se for um grafo não-direcionado

            # Matriz de Incidência (implementação simples)
            aresta = [0] * self.num_vertices
            aresta[u] = 1
            aresta[v] = 1
            self.matriz_incidencia.append(aresta)

            self.num_arestas = self.num_arestas + 1
        else :
            print('Um dos vertices selecionados não existe')

    # Remove uma aresta entre os vértices u e v
    def remover_aresta(self, u, v):
        # Matriz de Adjacência
        self.matriz_adjacencia[u][v] = 0
        self.matriz_adjacencia[v][u] = 0

        # Lista de Adjacência
        self.lista_adjacencia[u] = [vert for vert in self.lista_adjacencia[u] if vert != v]
        self.lista_adjacencia[v] = [vert for vert in self.lista_adjacencia[v] if vert != u]

        # Matriz de Incidência
        for aresta in self.matriz_incidencia:
            if aresta[u] != 0 and aresta[v] != 0:
                self.matriz_incidencia.remove(aresta)
                break

        #Matriz de aresta
        for indice,aresta in enumerate(self.matriz_aresta):
            if aresta[0]==(u,v):
                self.matriz_aresta.remove(aresta)

        self.num_arestas = self.num_arestas - 1

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

    # Checa se dois vértices são adjacentes
    def sao_adjacentes(self, u, v):
        if self.matriz_adjacencia[u][v] != 0:
            print(f"Os vertices {u} e {v} são adjacentes")
            return True
        else:
            print(f"Os vertices {u} e {v} não são adjacentes")
            return False

            
    # Checa se uma aresta existe entre dois vértices
    def existe_aresta(self, u, v):
        if self.matriz_adjacencia[u][v] != 0:
            print(f"A aresta ({u},{v}) existe")
            return True
        else :
            print(f"A aresta ({u},{v}) existe")
            return False 
        
    # Checa o número de vértices
    def numero_vertices(self):
        print(self.num_vertices)
        return self.num_vertices

    # Checa o número de arestas
    def numero_arestas(self):
        print(self.num_arestas)
        return self.num_arestas

    # Checa se o grafo está vazio
    def grafo_vazio(self):
        if self.num_arestas > 0:
            print('O grafo não está vazio')
        else :
            print('O grafo está vazio')
        return self.num_arestas > 0

    # Checa se o grafo é completo
    def grafo_completo(self):
        if self.num_arestas == (self.num_vertices(self.num_vertices - 1))/2 :
            print("O grafo está completo")
        else :
            print("O grafo não esta completo")
        return self.num_arestas == (self.num_vertices(self.num_vertices - 1))/2

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
            # print(f"Aresta adicionada: {u} - {v}")
            while u == v or self.existe_aresta(u, v):
                u = random.randint(0, self.num_vertices - 1)
                v = random.randint(0, self.num_vertices - 1)
            self.adicionar_aresta(u, v,)


            # Método ingênuo para detectar pontes
    def detectar_ponte_naive(self):
        pontes = []
        for u in range(self.num_vertices):
            for v in range(u + 1, self.num_vertices):
                if self.existe_aresta(u, v):
                    self.remover_aresta(u, v)
                    if not self.e_conexo():
                        pontes.append((u, v))
                    self.adicionar_aresta(u, v)  # Restaurar aresta
        return pontes
    
        
    def tarjan_ponte_util(self, u, visitados, disc, low, parent, pontes):
        visitados[u] = True
        disc[u] = low[u] = self.time
        self.time += 1

        for v, peso in self.lista_adjacencia[u]:
            if not visitados[v]:  # v não visitado
                parent[v] = u
                self.tarjan_ponte_util(v, visitados, disc, low, parent, pontes)

                low[u] = min(low[u], low[v])

                # Se o menor vértice alcançável a partir de v for
                # abaixo de u em DFS, então u-v é uma ponte
                if low[v] > disc[u]:
                    pontes.append((u, v))

            elif v != parent[u]:  # Atualiza low[u] para o caso de um ciclo
                low[u] = min(low[u], disc[v])

    def detectar_ponte_tarjan(self):
        visitados = [False] * self.num_vertices
        disc = [float("inf")] * self.num_vertices
        low = [float("inf")] * self.num_vertices
        parent = [-1] * self.num_vertices
        pontes = []
        self.time = 0

        for i in range(self.num_vertices):
            if not visitados[i]:
                self.tarjan_ponte_util(i, visitados, disc, low, parent, pontes)

        return pontes

    def euleriano(self):
        impares = 0
        for u in range(self.num_vertices):
            grau = len(self.lista_adjacencia[u])
            if grau % 2 != 0:
                impares += 1
        return impares == 0 or impares == 2

    def fleury(self):
        if not self.euleriano():
            print("O grafo não é euleriano.")
            return None

        caminho = []
        arestas_removidas = []

        def dfs(u):
            for v, peso in self.lista_adjacencia[u]:
                if (u, v) not in arestas_removidas and (v, u) not in arestas_removidas:
                    arestas_removidas.append((u, v))
                    dfs(v)
                    caminho.append((u, v))

        dfs(0)  # Começa do vértice 0
        return caminho

    def salvar_grafo_gexf(self, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<gexf xmlns="http://www.gexf.net/1.3draft"\n')
            f.write('     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
            f.write('     xsi:schemaLocation="http://www.gexf.net/1.3draft http://www.gexf.net/1.3draft/gexf.xsd">\n')
            f.write('  <graph mode="static" defaultedgetype="undirected">\n')
            f.write('    <nodes>\n')
            for i in range(self.num_vertices):
                f.write(f'      <node id="{i}" label="{i}"/>\n')
            f.write('    </nodes>\n')
            f.write('    <edges>\n')
            edge_id = 0
            for u in range(self.num_vertices):
                for v, peso in self.lista_adjacencia[u]:
                    if u < v:  # Para não duplicar arestas
                        f.write(f'      <edge id="{edge_id}" source="{u}" target="{v}" weight="{peso}"/>\n')
                        edge_id += 1
            f.write('    </edges>\n')
            f.write('  </graph>\n')
            f.write('</gexf>\n')