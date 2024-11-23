import random
import copy

class Vertice:
    def __init__(self, indice, rotulo=None, peso=None):
        self.indice = indice
        self.rotulo = rotulo
        self.peso = peso
        self.grau = 0
    
    def rotular_vertice(self, rotulo):
        self.rotulo = rotulo 

    def ponderar_vertice(self, peso):
        self.peso = peso 

    def imprimir_vertice(self):
        print(f'Vertice: {self.indice}, Rotulo: {self.rotulo}, Peso: {self.peso}, Grau:{self.grau}')

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


    # Adiciona uma aresta entre os vertices u e v
    def adicionar_aresta(self, V1, V2, rotulo=None, peso=1):
        if self.existe_aresta(V1,V2,False):
            print(f'A aresta {V1,V2} ja existe')
            return
        if self.achar_vertice(V1) != -1 and self.achar_vertice(V2) != -1:
            
            u=self.array_vertices[self.achar_vertice(V1)]
            v=self.array_vertices[self.achar_vertice(V2)]

            aresta = Aresta(u,v,rotulo,peso)

            # Array de arestas
            self.array_arestas.append(aresta)

            # Matriz de Adjacencia
            self.matriz_adjacencia[u.indice][v.indice] = peso
            self.matriz_adjacencia[v.indice][u.indice] = peso

            # Lista de Adjacencia
            self.lista_adjacencia[self.array_vertices[self.array_vertices.index(u)]].append(v)
            self.lista_adjacencia[self.array_vertices[self.array_vertices.index(v)]].append(v)

            # Matriz de Incidencia (implementação simples)
            newAresta = []
            for i in range(self.num_vertices):
                if i == u.indice or i == v.indice:
                    newAresta.append(1)
                else:
                    newAresta.append(0)
            self.matriz_incidencia.append(newAresta)

            u.grau = u.grau + 1
            v.grau = v.grau + 1

            self.num_arestas = self.num_arestas + 1
            
        else :
            print('Um dos vertices selecionados nao existe')

    # Remove uma aresta entre os vertices u e v
    def remover_aresta(self, aresta):
        if self.achar_aresta(aresta) != -1:
            A = self.array_arestas[self.achar_aresta(aresta)]
            u = A.V1
            v = A.V2

            # Matriz de Adjacencia
            self.matriz_adjacencia[A.V1.indice][A.V2.indice] = 0
            self.matriz_adjacencia[A.V2.indice][A.V1.indice] = 0

            # Lista de Adjacencia
            self.lista_adjacencia[u].remove(v) 
            self.lista_adjacencia[v].remove(u)  
            
            # Matriz de Incidencia
            for aresta in self.matriz_incidencia:
                if aresta[u.indice] != 0 and aresta[v.indice] != 0:
                    self.matriz_incidencia.remove(aresta)
                    break

            # Array de arestas
            self.array_arestas.remove(A)

            u.grau = u.grau - 1
            v.grau = v.grau - 1

            self.num_arestas = self.num_arestas - 1

        else:
            print('A aresta selecionada nao existe')

    def remover_vertice(self,v):
        vertice = self.array_vertices[self.achar_vertice(v)]
        adjacentes = self.lista_adjacencia[vertice]
        vizinhos = []
        for vizinho in adjacentes:
            vizinhos.append(vizinho)
        for item in vizinhos:
            self.remover_aresta((vertice.indice,item.indice))
        del self.lista_adjacencia[vertice]
        self.num_vertices = self.num_vertices - 1
        self.array_vertices.pop(vertice.indice)

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

    
    # Checa se dois vertices sao adjacentes
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
            
    # Checa se uma aresta existe entre dois vertices
    def existe_aresta(self, u, v, prnt=True):
        if self.matriz_adjacencia[u][v] != 0:
            if prnt:
                print(f"A aresta ({u},{v}) existe")
            return True
        else :
            if prnt:
                print(f"A aresta ({u},{v}) nao existe")
            return False 
        
    # Checa o número de vertices
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

    # Checa se o grafo e completo
    def grafo_completo(self):
        if self.num_arestas == (self.num_vertices*(self.num_vertices - 1))/2 :
            print("O grafo esta completo")
        else :
            print("O grafo nao esta completo")
        return self.num_arestas == (self.num_vertices*(self.num_vertices - 1))/2

    # Checa a conectividade do grafo (simplesmente conexo)
    def e_conexo(self, prnt=True):
        # Usa o novo DFS iterativo para verificar a conectividade
        visitados = self.dfs_iterativo(self.array_vertices[0].indice)  # Começa do vértice 0
        conexo = len(visitados) == self.num_vertices  # Verifica se todos os vértices foram visitados
        if prnt:  
            print(f"O grafo é {'conexo' if conexo else 'não conexo'}.")
        return conexo
    
    # Algoritmo de Kosaraju para componentes fortemente conexos
    def kosaraju(self):
        # Passo 1: DFS normal (usando o novo dfs_iterativo para obter a ordem de saída)
        visitados = self.dfs_iterativo(self.array_vertices[0].indice)  # Ordem de visita do grafo original
        ordem = list(reversed(visitados))  # Ordem inversa para a segunda DFS

        # Passo 2: Transpor o grafo
        grafo_transposto = Grafo(self.num_vertices)
        for u in range(self.num_vertices):
            for vizinho in self.lista_adjacencia[self.array_vertices[u]]:
                grafo_transposto.adicionar_aresta(vizinho.indice, u)

        # Passo 3: DFS no grafo transposto na ordem inversa
        componentes = []
        visitados_transposto = [False] * self.num_vertices

        for v in ordem:
            if not visitados_transposto[v]:
                componente = grafo_transposto.dfs_iterativo(v)
                componentes.append(componente)
                for vertice in componente:
                    visitados_transposto[vertice] = True

        print(f"Componentes fortemente conexos: {componentes}")
        return componentes

    
    def conectividade(self):
        if self.e_conexo(False):
            print("O grafo e fortemente conexo")
        else:
            print("O grafo e deconexo")


    # Checa se há uma ponte (aresta cuja remoção desconecta o grafo)
    def e_ponte(self, u, v, prnt=True):
        aresta = (u, v)
        self.remover_aresta(aresta) 
        conexo_sem_aresta = self.e_conexo(False)  
        self.adicionar_aresta(u, v)  # Restaura a aresta

        if prnt:
            if not conexo_sem_aresta:
                print(f"A aresta ({u}, {v}) e uma ponte.")
            else:
                print(f"A aresta ({u}, {v}) nao e uma ponte.")

        return not conexo_sem_aresta  # Retorna o estado correto da ponte

    # Checa se um vertice e um ponto de articulacao (vertice cuja remoção desconecta o grafo)
    def e_articulacao(self, v):
        if self.e_conexo(False):
            grafo_aux = copy.deepcopy(self)
            grafo_aux.remover_vertice(v)
            articulacao = grafo_aux.e_conexo(False)
            if not articulacao:
                print(f"O vertice {v} e articulacao")
            else:
                print(f"O vertice {v} nao e articulacao")
            return not articulacao
        else:
            print('O vertice nao e uma articulacao pois o grafo ja e desconexo')

    # Função para gerar um grafo aleatório
    def graforandom(self, num_arestas=0):
        if num_arestas == 0:
            max_arestas = random.randint(1, ((self.num_vertices * (self.num_vertices - 1)) // 2))
            num_arestas = max(1, max_arestas // 10)
        if num_arestas > (self.num_vertices * (self.num_vertices - 1)) // 2:
            print("Número de arestas excede o máximo possível para um grafo simples.")
            return

        for _ in range(num_arestas):
            u = random.randint(0, self.num_vertices - 1)
            v = random.randint(0, self.num_vertices - 1)
            
            while self.existe_aresta(u,v,False) or u == v:
                u = random.randint(0, self.num_vertices - 1)
                v = random.randint(0, self.num_vertices - 1)
            
            self.adicionar_aresta(u, v)

        print(f"Grafo aleatorio gerado com {num_arestas} arestas.")
    
        
    def tarjan_ponte_util(self, u, visitados, disc, low, parent, pontes):
        visitados[u] = True
        disc[u] = low[u] = self.time
        self.time += 1

        # Acessando a lista de adjacência corretamente usando o índice de 'u'
        for v in self.lista_adjacencia[self.array_vertices[u]]:  # Acesse corretamente o índice do vertice
            if not visitados[v]:  # v nao visitado
                parent[v] = u
                self.tarjan_ponte_util(v, visitados, disc, low, parent, pontes)

                low[u] = min(low[u], low[v])

                # Se o menor vertice alcançável a partir de v for
                # abaixo de u em DFS, então u-v e uma ponte
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
        for u in self.lista_adjacencia:
            grau = len(self.lista_adjacencia[u])
            if grau % 2 != 0:
                impares += 1
        return impares == 0 or impares == 2

    def fleury_naive(self):
        if not self.euleriano() or not self.e_conexo(False):
            print("O grafo nao e euleriano.")
            return None

        grafo_aux = copy.deepcopy(self)
        caminho = []
        
        for vertice in grafo_aux.array_vertices:
            if vertice.grau % 2 != 0:
                v = vertice
                break
            else:
                v = grafo_aux.array_vertices[0]
        caminho.append(v.indice)
        while grafo_aux.num_arestas > 0:
            if v.grau > 1:
                for vizinho in grafo_aux.lista_adjacencia[v]:
                    if not grafo_aux.e_ponte(v.indice, vizinho.indice, False):
                        caminho.append(vizinho.indice)
                        grafo_aux.remover_aresta((v.indice,vizinho.indice))
                        v = vizinho
            else:
                vizinho = grafo_aux.lista_adjacencia[v][0]
                caminho.append(vizinho.indice)
                grafo_aux.remover_aresta((v.indice,vizinho.indice))
                v = vizinho
        print(f"Caminho euleriano:{caminho}")
        if caminho[0] == caminho[len(caminho)-1]:
            print("O grafo e euleriano")
        else:
            print("O grafo e semi-euleriano")


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
                peso = vertice.peso if vertice.peso else vertice.indice
                f.write(f'      <node id="{vertice.indice}" label="{rotulo}"/>  weight="{peso}"/> \n')
            f.write('    </nodes>\n')

            # Adicionando arestas
            f.write('    <edges>\n')
            edge_id = 0
            for aresta in self.array_arestas:
                u, v = aresta.V1.indice, aresta.V2.indice 
                peso = aresta.peso 
                print(peso)
                f.write(f'      <edge id="{edge_id}" source="{u}" target="{v}" label="{peso}"/>\n')
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

    # Metodo para imprimir a matriz de adjacencia
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

    # Metodo para imprimir a matriz de incidencia
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

    # Metodo para imprimir a lista de adjacencia
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
    
    def dfs_iterativo(self, u):
        vertice = self.array_vertices[self.achar_vertice(u)]
        visitados = [False] * self.num_vertices
        stack = [vertice]
        ordem_visita = []
        while stack:
            vertice_atual = stack.pop()
            if not visitados[self.array_vertices.index(vertice_atual)]:
                visitados[self.array_vertices.index(vertice_atual)] = True
                ordem_visita.append(vertice_atual.indice)
                for vizinho in self.lista_adjacencia[vertice_atual]:
                    if not visitados[self.array_vertices.index(vizinho)]:
                        stack.append(vizinho)
        return ordem_visita
    
    # def dfs(self,v=0):
    #     t=0
    #     tabela = {vertice : {'td':0,'tt':0,'pai':None} for vertice in self.array_vertices}
    #     def busca(v):
    #         nonlocal t
    #         vertice = self.array_vertices[self.achar_vertice(v)]
    #         t = t+1
    #         tabela[vertice]['td'] = t
    #         for vizinho in self.lista_adjacencia[vertice]:
    #             if tabela[vizinho]['td'] == 0:
    #                 tabela[vizinho]['pai'] = vertice
    #                 busca(vizinho.indice)
    #         t = t+1
    #         tabela[vertice]['tt'] = t
    #     for vertice in tabela:
    #         if tabela[vertice]['td'] == 0:
    #             busca(vertice.indice)

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

    # Adiciona uma aresta entre os vertices u e v
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

            u.grau = u.grau + 1

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

            u.grau = u.grau - 1

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

