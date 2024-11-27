from libGrafos import Grafo, Direcionado, process_gexf

def main():
    grafo = None  # Inicializa o grafo como None
    op = 0

    while op != -1:
        print("\nOpções:")
        print("1- Importar Grafo (.gexf)")
        print("2- Criar Grafo vazio")
        print("3- Criar Grafo aleatório")
        print("4- Criar Grafo Linear")
        print("5- Adicionar aresta")
        print("6- Remover aresta")
        print("7- Remover vértice")
        print("8- Rotular arestas")
        print("9- Ponderar arestas")
        print("10- Rotular vértices")
        print("11- Ponderar vértices")
        print("12- Adjacência entre vértices")
        print("13- Adjacência entre arestas")
        print("14- Existência de arestas")
        print("15- Quantidade de vértices e arestas")
        print("16- Checagem de grafo vazio")
        print("17- Checagem de grafo completo")
        print("18- Conectividade do grafo")
        print("19- Quantidade de componentes fortemente conexos (Kosaraju)")
        print("20- Checagem de ponte")
        print("21- Checagem de articulação")
        print("22- Representar por matriz de adjacência")
        print("23- Representar por matriz de incidência")
        print("24- Representar por lista de adjacência")
        print("25- Fleury naive")
        print("26- Fleury Tarjan")
        print("27- Exportar Grafo")
        print("-1- Sair do menu")
        
        op = int(input("\nEscolha uma opção: "))
        
        if grafo is None:

            if op == 1:
                file = input("Insira o nome do arquivo:")
                file_path = f"../../TrabGrafos/src/gexfs/{file}"

                nodes, edges , tipo = process_gexf(file_path)
                indices = []
                rotulos = []

                for vertice,propertys in nodes.items():
                    indices.append(vertice)
                    rotulos.append(propertys['label'])

                if tipo == 'directed':
                    grafo = Direcionado(len(indices))
                else:
                    grafo = Grafo(len(indices))

                grafo.rotular_vertices(rotulos)

                for aresta in edges:
                    u = int(aresta['source'])
                    v = int(aresta['target'])
                    peso = int(aresta['label'])
                    grafo.adicionar_aresta(u,v,None,peso)

                print("Grafo importado com sucesso")

            elif op == 2:
                tipo = int(input("Qual o tipo do Grafo? 1 para não direcionado, 2 para direcionado"))
                n = int(input("Digite o número de vértices do grafo: "))
                if tipo == 2:
                    grafo = Direcionado(n)
                else:
                    grafo = Grafo(n)
                print(f"Grafo vazio criado com {n} vértices!")

            
            elif op == 3:
                tipo = int(input("Qual o tipo do Grafo? 1 para não direcionado, 2 para direcionado"))
                n_vertices = int(input("Digite o número de vértices do grafo: "))
                n_arestas = input("Digite o número de arestas desejadas (pressione Enter para 0): ")
                n_arestas = int(n_arestas) if n_arestas else 0
                if tipo == 2:
                    grafo = Direcionado(n_vertices)
                else:
                    grafo = Grafo(n_vertices)
                grafo.graforandom(n_arestas)
                print(f"Grafo aleatório criado com {n_vertices} vértices e {n_arestas} arestas.")

            elif op == 4:
                tipo = int(input("Qual o tipo do Grafo? 1 para não direcionado, 2 para direcionado"))
                n = int(input("Digite o número de vértices do grafo: "))
                if tipo == 2:
                    grafo = Direcionado(n)
                else:
                    grafo = Grafo(n)
                grafo.grafo_linear()
                print(f"Grafo linear criado com {n} vértices e {n - 1} arestas.")

        else:
            if op == 1 or op == 2 or op == 3 or op == 4:
                print("Você já criou um grafo. Não é possível criar outro.")
            
            elif op == 5:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                peso = int(input("Digite o peso da aresta (padrão 1): "))
                grafo.adicionar_aresta(v1, v2, peso=peso)

            elif op == 6:
                v1 = int(input("Digite o primeiro vértice da aresta a ser removida: "))
                v2 = int(input("Digite o segundo vértice da aresta a ser removida: "))
                grafo.remover_aresta((v1, v2))

            elif op == 7:
                v = int(input("Digite o vértice a ser removido: "))
                grafo.remover_vertice(v)

            elif op == 8:
                rotulos = input("Digite os rótulos das arestas separados por vírgula: ").split(',')
                grafo.rotular_arestas(rotulos)

            elif op == 9:
                pesos = list(map(int, input("Digite os pesos das arestas separados por espaço: ").split()))
                grafo.ponderar_arestas(pesos)

            elif op == 10:
                rotulos = input("Digite os rótulos dos vértices separados por vírgula: ").split(',')
                grafo.rotular_vertices(rotulos)

            elif op == 11:
                pesos = list(map(int, input("Digite os pesos dos vértices separados por espaço: ").split()))
                grafo.ponderar_vertices(pesos)

            elif op == 12:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                grafo.sao_adjacentesV(v1, v2)

            elif op == 13:
                a1 = tuple(map(int, input("Digite a primeira aresta (v1, v2): ").split(',')))
                a2 = tuple(map(int, input("Digite a segunda aresta (v1, v2): ").split(',')))
                grafo.sao_adjacentesA(a1, a2)

            elif op == 14:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                grafo.existe_aresta(v1, v2)

            elif op == 15:
                grafo.numero_vertices()
                grafo.numero_arestas()

            elif op == 16:
                grafo.grafo_vazio()

            elif op == 17:
                grafo.grafo_completo()

            elif op == 18:
                grafo.conectividade()

            elif op == 19:
                grafo.kosaraju()

            elif op == 20:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                grafo.e_ponte(v1, v2)

            elif op == 21:
                v = int(input("Digite o vértice: "))
                grafo.e_articulacao(v)

            elif op == 22:
                grafo.imprimir_matriz_adjacencia()

            elif op == 23:
                grafo.imprimir_matriz_incidencia()

            elif op == 24:
                grafo.imprimir_lista_adjacencia()

            elif op == 25:
                grafo.fleury_naive()

            elif op == 26:
                grafo.fleury_tarjan()

            elif op == 27:
                nome_arquivo = input("Digite o nome do arquivo para exportar (com extensão .gexf): ")
                grafo.salvar_grafo_gexf(nome_arquivo)
                print(f"Grafo exportado para {nome_arquivo}.")

            elif op == -1:
                print("Saindo do programa...")
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
-1