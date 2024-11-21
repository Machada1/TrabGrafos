import random

class Vertice:
    def __init__(self, indice, rotulo=None, peso=None):
        self.indice = indice
        self.rotulo = rotulo
        self.peso = peso
        self.fecho = []
    
    def rotular_vertice(self, rotulo):
        self.rotulo = rotulo 

    def ponderar_vertice(self, peso):
        self.peso = peso 

    def imprimir_vertice(self):
        print(f'Vertice: {self.indice}, Rotulo: {self.rotulo}, Peso: {self.peso}')

class Aresta:
    def __init__(self, u, v, rotulo, peso):
        self.indices = [(u,v), (v,u)]
        self.V1 = u
        self.V2 = v
        self.rotulo = rotulo
        self.peso = peso

    def rotular_aresta(self, rotulo):
        self.rotulo = rotulo

    def ponderar_aresta(self, peso):
        self.peso = peso
    
    def imprimir_aresta(self):
        print(f'Aresta: {self.V1.indice,self.V2.indice}, Rotulo: {self.rotulo}, Peso: {self.peso}')

class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.num_arestas = 0
        self.array_vertices = []
        for i in range(num_vertices):
            self.array_vertices.append(Vertice(i))
        self.array_arestas = []
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]
        self.matriz_incidencia = []
        self.lista_adjacencia = {vertice: [] for vertice in self.array_vertices}

    # Rotula os vertices do grafo
    def rotular_vertices(self,rotulos):
        if self.elementos_unicos(rotulos):
            if len(rotulos) == len(self.array_vertices):
                for i,rotulo in enumerate(rotulos):
                    self.array_vertices[i].rotular_vertice(rotulo)
            else:
                print(f'A quantidade de rotulos fornecida nao condiz com a quantidade de vertices do grafo.')
        else :
            print(f'O vetor de rotulos possui dois ou mais rotulos iguais')

    # Pondera os vertices do grafo
    def ponderar_vertices(self,pesos):
        if len(pesos) == len(self.array_vertices):
            for i,peso in enumerate(pesos):
                self.array_vertices[i].ponderar_vertice(peso)
        else:
            print(f'A quantidade de pesos fornecida nao condiz com a quantidade de vertices do grafo.')


    # Adiciona uma aresta entre os vértices u e v
    def adicionar_aresta(self, V1, V2, rotulo=None, peso=1):
        for aresta in self.array_arestas:
            U = self.array_vertices[self.achar_vertice(V1)]
            V = self.array_vertices[self.achar_vertice(V2)]
            u = aresta.V1
            v = aresta.V2
            indices = [(u.indice,v.indice),(v.indice,u.indice)]
            if (U.indice,V.indice) in indices:
                print(f'A aresta {V1,V2} ja existe')
                return
        if self.achar_vertice(V1) != -1 and self.achar_vertice(V2) != -1:
            
            u=self.array_vertices[self.achar_vertice(V1)]
            v=self.array_vertices[self.achar_vertice(V2)]

            if v not in u.fecho:
                u.fecho.append(v)
            if u not in v.fecho:
                v.fecho.append(u)
            for vertice in v.fecho:
                if vertice not in u.fecho:
                    u.fecho.append(vertice)
                if u not in vertice.fecho:
                    vertice.fecho.append(u)
            for vertice in u.fecho:
                if vertice not in v.fecho:
                    v.fecho.append(vertice)
                if v not in vertice.fecho:
                    vertice.fecho.append(v)

            aresta = Aresta(u,v,rotulo,peso)

            # Array de arestas
            self.array_arestas.append(aresta)

            # Matriz de Adjacencia
            self.matriz_adjacencia[u.indice][v.indice] = peso
            self.matriz_adjacencia[v.indice][u.indice] = peso

            # Lista de Adjacencia
            for vertice in self.array_vertices:
                if vertice == u:
                    self.lista_adjacencia[vertice].append(v)
                elif vertice == v:
                    self.lista_adjacencia[vertice].append(u)

            # Matriz de Incidencia (implementação simples)
            newAresta = []
            for i in range(self.num_vertices):
                if i == u.indice or i == v.indice:
                    newAresta.append(1)
                else:
                    newAresta.append(0)
            self.matriz_incidencia.append(newAresta)

            self.num_arestas = self.num_arestas + 1
            
        else :
            print('Um dos vertices selecionados nao existe')

    # Remove uma aresta entre os vértices u e v
    def remover_aresta(self, aresta):

        if self.achar_aresta(aresta) != -1:
            A = self.array_arestas[self.achar_aresta(aresta)]
            u = A.V1
            v = A.V2

            self.atualizar_fechos()

            # Matriz de Adjacencia
            self.matriz_adjacencia[A.V1.indice][A.V2.indice] = 0
            self.matriz_adjacencia[A.V2.indice][A.V1.indice] = 0

            # Lista de Adjacencia
            self.lista_adjacencia[u] = self.lista_adjacencia[u].remove(v)
            self.lista_adjacencia[v] = self.lista_adjacencia[v].remove(u)
            
            # Matriz de Incidencia
            for aresta in self.matriz_incidencia:
                if aresta[u.indice] != 0 and aresta[v.indice] != 0:
                    self.matriz_incidencia.remove(aresta)
                    break

            # Array de arestas
            self.array_arestas.remove(A)

            self.num_arestas = self.num_arestas - 1

        else:
            print('A aresta selecionada nao existe')

    # Rotula as arestas do grafo
    def rotular_arestas(self,rotulos):
        if self.elementos_unicos:
            if len(rotulos) == len(self.array_arestas):
                for i,rotulo in enumerate(rotulos):
                    self.array_arestas[i].rotular_aresta(rotulo)
            else:
                print(f'A quantidade de rotulos fornecida nao condiz com a quantidade de arestas do grafo.')
        else :
            print(f'O vetor de rotulos possui dois ou mais rotulos iguais')

    # Pondera as arestas do grafo
    def ponderar_arestas(self,pesos):
        if len(pesos) == len(self.array_arestas):
            for i,peso in enumerate(pesos):
                self.array_arestas[i].ponderar_aresta(peso)
                u = self.array_arestas[i].V1
                v = self.array_arestas[i].V2
                self.matriz_adjacencia[u.indice][v.indice] = peso
                self.matriz_adjacencia[v.indice][u.indice] = peso
        else:
            print(f'A quantidade de pesos fornecida nao condiz com a quantidade de arestas do grafo.')

    
    # Checa se dois vértices sao adjacentes
    def sao_adjacentesV(self, u, v):
        if self.achar_vertice(u) != -1 and self.achar_vertice(v) != -1:
            V1 = self.array_vertices[self.achar_vertice(u)]
            V2 = self.array_vertices[self.achar_vertice(v)]
            if self.matriz_adjacencia[V1.indice][V2.indice] != 0:
                print(f"Os vertices {u} e {v} sao adjacentes")
                return True
            else:
                print(f"Os vertices {u} e {v} nao sao adjacentes")
                return False
        else:
            print(f'Um dos vertices selecionados nao existe, logo eles nao sao adjacentes')
            return False

    # Checa se duas arestas sao adjacentes
    def sao_adjacentesA(self, aresta1, aresta2):
        if self.achar_aresta(aresta1) != -1 and self.achar_aresta(aresta2) != -1:
            u=self.array_arestas[self.achar_aresta(aresta1)]
            v=self.array_arestas[self.achar_aresta(aresta2)]
            if u.V1 == v.V1 or u.V1 == v.V2 or u.V2 == v.V1 or u.V2 == v.V2:
                print(f"As arestas {aresta1} e {aresta2} sao adjacentes")
                return True
            else:
                print(f"As arestas {aresta1} e {aresta2} nao sao adjacentes")
                return False
        else:
            print("Alguma das arestas fornecidas nao existe, logo elas nao sao adjacentes")
            
    # Checa se uma aresta existe entre dois vértices
    def existe_aresta(self, u, v, prnt=True):
        if self.matriz_adjacencia[u][v] != 0:
            if prnt:
                print(f"A aresta ({u},{v}) existe")
            return True
        else :
            if prnt:
                print(f"A aresta ({u},{v}) nao existe")
            return False 
        
    # Checa o número de vértices
    def numero_vertices(self):
        print(f'quantidade de vertices: {self.num_vertices}')
        return self.num_vertices

    # Checa o número de arestas
    def numero_arestas(self):
        print(f'quantidade de arestas: {self.num_arestas}')
        return self.num_arestas

    # Checa se o grafo esta vazio
    def grafo_vazio(self):
        if self.num_arestas > 0:
            print('O grafo nao esta vazio')
        else :
            print('O grafo esta vazio')
        return self.num_arestas

    # Checa se o grafo é completo
    def grafo_completo(self):
        if self.num_arestas == (self.num_vertices*(self.num_vertices - 1))/2 :
            print("O grafo esta completo")
        else :
            print("O grafo nao esta completo")
        return self.num_arestas == (self.num_vertices*(self.num_vertices - 1))/2

    # Checa a conectividade do grafo (simplesmente conexo)
    def e_conexo(self):
        visitados = [0] * self.numero_vertices()
        for vertice in self.array_vertices:
            for V in vertice.fecho:
                visitados[V.indice] = 1
        if len(set(visitados)) == 1:
            print("O grafo e conexo")
            return True

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

        print(f"Componentes fortemente conexos: {componentes}")
        return componentes

    # Checa se há uma ponte (aresta cuja remoção desconecta o grafo)
    def e_ponte(self, u, v):
        self.remover_aresta(u, v)
        conexo_sem_aresta = self.e_conexo()
        self.adicionar_aresta(u, v)  # Restaurar a aresta
        print(f"A aresta ({u}, {v}) é {'uma ponte' if not conexo_sem_aresta else 'não uma ponte'}.")
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

        print(f"O vértice {vertice} é {'um ponto de articulação' if not conexo_sem_vertice else 'não um ponto de articulação'}.")
        return not conexo_sem_vertice

    # Função para gerar um grafo aleatório
    def graforandom(self, num_arestas=0):
        if num_arestas == 0:
            num_arestas = random.randint(1, ((self.num_vertices * (self.num_vertices - 1)) // 2))
        if num_arestas > (self.num_vertices * (self.num_vertices - 1)) // 2:
            print("Número de arestas excede o máximo possível para um grafo simples.")
            return

        for _ in range(num_arestas):
            u = random.randint(0, self.num_vertices - 1)
            v = random.randint(0, self.num_vertices - 1)
            
            while self.existe_aresta(u,v,False):
                u = random.randint(0, self.num_vertices - 1)
                v = random.randint(0, self.num_vertices - 1)
            
            self.adicionar_aresta(u, v)

        print(f"Grafo aleatorio gerado com {num_arestas} arestas.")


    # Método ingenuo para detectar pontes
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
            if not visitados[v]:  # v nao visitado
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
            print("O grafo nao é euleriano.")
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

    # def salvar_grafo_gexf(self, nome_arquivo):
    #     with open(nome_arquivo, 'w') as f:
    #         f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    #         f.write('<gexf xmlns="http://www.gexf.net/1.3draft"\n')
    #         f.write('     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
    #         f.write('     xsi:schemaLocation="http://www.gexf.net/1.3draft http://www.gexf.net/1.3draft/gexf.xsd">\n')
    #         f.write('  <graph mode="static" defaultedgetype="undirected">\n')
    #         f.write('    <nodes>\n')
    #         for i in range(self.num_vertices):
    #             f.write(f'      <node id="{i}" label="{i}"/>\n')
    #         f.write('    </nodes>\n')
    #         f.write('    <edges>\n')
    #         edge_id = 0
    #         for u in range(self.num_vertices):
    #             for v, peso in self.lista_adjacencia[u]:
    #                 if u < v:  # Para não duplicar arestas
    #                     f.write(f'      <edge id="{edge_id}" source="{u}" target="{v}" weight="{peso}"/>\n')
    #                     edge_id += 1
    #         f.write('    </edges>\n')
    #         f.write('  </graph>\n')
    #         f.write('</gexf>\n')

    # def elementos_unicos(self,vetor):
    #     return len(vetor) == len(set(vetor))

    # Função para verificar elementos únicos
    def elementos_unicos(vetor):
        return len(vetor) == len(set(vetor))


    # Salvar o grafo no formato GEXF
    def salvar_grafo_gexf(self, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<gexf xmlns="http://www.gexf.net/1.3draft"\n')
            f.write('     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
            f.write('     xsi:schemaLocation="http://www.gexf.net/1.3draft http://www.gexf.net/1.3draft/gexf.xsd">\n')
            f.write('  <graph mode="static" defaultedgetype="undirected">\n')
            
            # Adicionando nós
            f.write('    <nodes>\n')
            for vertice in self.array_vertices:
                rotulo = vertice.rotulo if vertice.rotulo else vertice.indice
                f.write(f'      <node id="{vertice.indice}" label="{rotulo}"/>\n')
            f.write('    </nodes>\n')

            # Adicionando arestas
            f.write('    <edges>\n')
            edge_id = 0
            for aresta in self.array_arestas:
                u, v = aresta.Vsaida, aresta.Vchegada
                peso = aresta.peso if aresta.peso is not None else 1
                if u < v: 
                    f.write(f'      <edge id="{edge_id}" source="{u}" target="{v}" weight="{peso}"/>\n')
                    edge_id += 1
            f.write('    </edges>\n')
            f.write('  </graph>\n')
            f.write('</gexf>\n')

    # Imprime os arestas do grafo com seus rotulos e pesos
    def imprimir_arestas(self):
        for i in range(len(self.array_arestas)):
            self.array_arestas[i].imprimir_aresta()

    # Imprime os vertices do grafo com seus rotulos e pesos
    def imprimir_vertices(self):
        for i in range(len(self.array_vertices)):
            self.array_vertices[i].imprimir_vertice()

    # Método para imprimir a matriz de adjacencia
    def imprimir_matriz_adjacencia(self):

        print("Matriz de Adjacencia:")

        if self.vertices_rotulados():
            print("   " + " ".join(str(vertice.rotulo) for vertice in self.array_vertices))
            for i, linha in enumerate(self.matriz_adjacencia):
                print(f"{self.array_vertices[i].rotulo} | " + " ".join(map(str, linha)))

        else:
            print("   " + " ".join(str(vertice.indice) for vertice in self.array_vertices))
            for i, linha in enumerate(self.matriz_adjacencia):
                print(f"{i} | " + " ".join(map(str, linha)))

    # Método para imprimir a matriz de incidencia
    def imprimir_matriz_incidencia(self):

        print("Matriz de Incidencia:")

        if not self.matriz_incidencia:
            print("A matriz de incidencia esta vazia.")
            return
        
        if self.arestas_rotuladas():
            print("   " + " ".join(str(vertice.rotulo) for vertice in self.array_vertices))
            for i, linha in enumerate(self.matriz_incidencia):
                print(f"{self.array_arestas[i].rotulo} | " + " ".join(map(str, linha)))

        else:
            print("   " + " ".join(str(vertice.indice) for vertice in self.array_vertices))
            for i, linha in enumerate(self.matriz_incidencia):
                print(f"{i} | " + " ".join(map(str, linha)))

    # Método para imprimir a lista de adjacencia
    def imprimir_lista_adjacencia(self):
        print("Lista de Adjacencia:")
        if self.vertices_rotulados():
            for chave,valor in self.lista_adjacencia.items():
                if valor:
                    vertices =[vertice.rotulo for vertice in valor]
                else:
                    vertices = []
                print(f'{chave.rotulo}: {vertices}')
        else:
            for chave,valor in self.lista_adjacencia.items():
                if valor:
                    vertices = [vertice.indice for vertice in valor]
                else:
                    vertices = []
                print(f'{chave.indice}: {vertices}')

    def imprimir_fechos(self):
        for vertice in self.array_vertices:
            print(f"Fecho do vertice {vertice.indice}")
            for V in vertice.fecho:
                V.imprimir_vertice()

    def elementos_unicos(self,vetor):
        return len(vetor) == len(set(vetor))
    
    def achar_vertice(self, valor):
        for i, vertice in enumerate(self.array_vertices):
            if vertice.indice == valor or vertice.rotulo == valor:
                return i
        return -1
            
    def achar_aresta(self, valor):
        for i, aresta in enumerate(self.array_arestas):
            u = aresta.V1.indice
            v = aresta.V2.indice
            indices = [(u,v),(v,u)]
            if valor in indices or valor == aresta.rotulo:
                return i
        return -1
    
    def vertices_rotulados(self):
        for vertice in self.array_vertices:
            if not vertice.rotulo:
                return False
        return True
            
    def arestas_rotuladas(self):
        for aresta in self.array_arestas:
            if not aresta.rotulo:
                return False
        return True

class Aresta_Direcionada:
    def __init__(self, u, v, rotulo, peso):
        self.indice = (u,v)
        self.V1 = u
        self.V2 = v
        self.rotulo = rotulo
        self.peso = peso

    def rotular_aresta(self, rotulo):
        self.rotulo = rotulo

    def ponderar_aresta(self, peso):
        self.peso = peso
    
    def imprimir_aresta(self):
        print(f'Aresta: {self.V1.indice,self.V2.indice}, Rotulo: {self.rotulo}, Peso: {self.peso}')

class Direcionado(Grafo):

    # Adiciona uma aresta entre os vértices u e v
    def adicionar_aresta(self, V1, V2, rotulo=None, peso=1):
        for aresta in self.array_arestas:
            U = self.array_vertices[self.achar_vertice(V1)]
            V = self.array_vertices[self.achar_vertice(V2)]
            u = aresta.V1
            v = aresta.V2
            if (U.indice, V.indice) == (u.indice, v.indice):
                print(f'A aresta {V1,V2} ja existe')
                return
        if self.achar_vertice(V1) != -1 and self.achar_vertice(V2) != -1:
            
            u=self.array_vertices[self.achar_vertice(V1)]
            v=self.array_vertices[self.achar_vertice(V2)]

            if v not in u.fecho:
                u.fecho.append(v)
            if u not in v.fecho:
                v.fecho.append(u)
            for vertice in v.fecho:
                if vertice not in u.fecho:
                    u.fecho.append(vertice)
                if u not in vertice.fecho:
                    vertice.fecho.append(u)
            for vertice in u.fecho:
                if vertice not in v.fecho:
                    v.fecho.append(vertice)
                if v not in vertice.fecho:
                    vertice.fecho.append(v)

            aresta = Aresta_Direcionada(u,v,rotulo,peso)

            # Array de arestas
            self.array_arestas.append(aresta)

            # Matriz de Adjacencia
            self.matriz_adjacencia[u.indice][v.indice] = peso

            # Lista de Adjacencia
            for vertice in self.array_vertices:
                if vertice == u:
                    self.lista_adjacencia[vertice].append(v)

            # Matriz de Incidencia (implementação simples)
            newAresta = []
            for i in range(self.num_vertices):
                if i == u.indice:
                    newAresta.append(1)
                elif i == v.indice:
                    newAresta.append(-1)
                else:
                    newAresta.append(0)
            self.matriz_incidencia.append(newAresta)

            self.num_arestas = self.num_arestas + 1
            
        else :
            print('Um dos vertices selecionados nao existe')

        
    def remover_aresta(self, aresta):

        if self.achar_aresta(aresta) != -1:
            A = self.array_arestas[self.achar_aresta(aresta)]
            u = A.V1
            v = A.V2

            # Matriz de Adjacencia
            self.matriz_adjacencia[u.indice][v.indice] = 0

            # Lista de Adjacencia
            self.lista_adjacencia[u] = self.lista_adjacencia[u].remove(v)
            
            # Matriz de Incidencia
            for aresta in self.matriz_incidencia:
                if aresta[u.indice] != 0 and aresta[v.indice] != 0:
                    self.matriz_incidencia.remove(aresta)
                    break

            # Array de arestas
            self.array_arestas.remove(A)

            self.num_arestas = self.num_arestas - 1

        else:
            print('A aresta selecionada nao existe')

    # Salvar o grafo no formato GEXF
    def salvar_grafo_gexf(self, nome_arquivo):
        with open(nome_arquivo, 'w') as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<gexf xmlns="http://www.gexf.net/1.3draft"\n')
            f.write('     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n')
            f.write('     xsi:schemaLocation="http://www.gexf.net/1.3draft http://www.gexf.net/1.3draft/gexf.xsd">\n')
            f.write('  <graph mode="static" defaultedgetype="directed">\n')
            
            # Adicionando nós
            f.write('    <nodes>\n')
            for vertice in self.array_vertices:
                rotulo = vertice.rotulo if vertice.rotulo else vertice.indice
                f.write(f'      <node id="{vertice.indice}" label="{rotulo}"/>\n')
            f.write('    </nodes>\n')

            # Adicionando arestas
            f.write('    <edges>\n')
            edge_id = 0
            for aresta in self.array_arestas:
                u, v = aresta.Vsaida, aresta.Vchegada
                peso = aresta.peso if aresta.peso is not None else 1
                if u < v: 
                    f.write(f'      <edge id="{edge_id}" source="{u}" target="{v}" weight="{peso}"/>\n')
                    edge_id += 1
            f.write('    </edges>\n')
            f.write('  </graph>\n')
            f.write('</gexf>\n')

    def achar_aresta(self, valor):
        for i, aresta in enumerate(self.array_arestas):
            u = aresta.V1.indice
            v = aresta.V2.indice
            indices = [(u,v)]
            if valor in indices or valor == aresta.rotulo:
                return i
        return -1