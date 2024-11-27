from libGrafos import Grafo, Direcionado

def main():
    grafo = None  # Inicializa o grafo como None
    op = 0

    while op != -1:
        print("\nOpções:")
        print("1- Criar Grafo vazio")
        print("2- Criar Grafo aleatório")
        print("3- Adicionar aresta")
        print("4- Remover aresta")
        print("5- Remover vértice")
        print("6- Rotular arestas")
        print("7- Ponderar arestas")
        print("8- Rotular vértices")
        print("9- Ponderar vértices")
        print("10- Adjacência entre vértices")
        print("11- Adjacência entre arestas")
        print("12- Existência de arestas")
        print("13- Quantidade de vértices e arestas")
        print("14- Checagem de grafo vazio")
        print("15- Checagem de grafo completo")
        print("16- Conectividade do grafo")
        print("17- Quantidade de componentes fortemente conexos (Kosaraju)")
        print("18- Checagem de ponte")
        print("19- Checagem de articulação")
        print("20- Representar por matriz de adjacência")
        print("21- Representar por matriz de incidência")
        print("22- Representar por lista de adjacência")
        print("23- Fleury naive")
        print("24- Fleury Tarjan")
        print("25- Exportar Grafo")
        print("-1- Sair do menu")
        
        op = int(input("\nEscolha uma opção: "))
        
        # Verifica se o grafo já foi criado
        if grafo is None:
            if op == 1:
                n = int(input("Digite o número de vértices do grafo: "))
                grafo = Grafo(n)
                print(f"Grafo vazio criado com {n} vértices!")
            
            elif op == 2:
                n_vertices = int(input("Digite o número de vértices do grafo: "))
                n_arestas = input("Digite o número de arestas desejadas (pressione Enter para 0): ")
                n_arestas = int(n_arestas) if n_arestas else 0  # Se o input estiver vazio, assume 0
                grafo = Grafo(n_vertices)  # Cria o grafo com o número de vértices fornecido
                grafo.graforandom(n_arestas)  # Preenche o grafo com o número de arestas
                print(f"Grafo aleatório criado com {n_vertices} vértices e {n_arestas} arestas.")
        else:
            if op == 1 or op == 2:
                print("Você já criou um grafo. Não é possível criar outro.")
            
            elif op == 3:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                peso = int(input("Digite o peso da aresta (padrão 1): "))
                grafo.adicionar_aresta(v1, v2, peso=peso)

            elif op == 4:
                v1 = int(input("Digite o primeiro vértice da aresta a ser removida: "))
                v2 = int(input("Digite o segundo vértice da aresta a ser removida: "))
                grafo.remover_aresta((v1, v2))

            elif op == 5:
                v = int(input("Digite o vértice a ser removido: "))
                grafo.remover_vertice(v)

            elif op == 6:
                rotulos = input("Digite os rótulos das arestas separados por vírgula: ").split(',')
                grafo.rotular_arestas(rotulos)

            elif op == 7:
                pesos = list(map(int, input("Digite os pesos das arestas separados por espaço: ").split()))
                grafo.ponderar_arestas(pesos)

            elif op == 8:
                rotulos = input("Digite os rótulos dos vértices separados por vírgula: ").split(',')
                grafo.rotular_vertices(rotulos)

            elif op == 9:
                pesos = list(map(int, input("Digite os pesos dos vértices separados por espaço: ").split()))
                grafo.ponderar_vertices(pesos)

            elif op == 10:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                grafo.sao_adjacentesV(v1, v2)

            elif op == 11:
                a1 = tuple(map(int, input("Digite a primeira aresta (v1, v2): ").split(',')))
                a2 = tuple(map(int, input("Digite a segunda aresta (v1, v2): ").split(',')))
                grafo.sao_adjacentesA(a1, a2)

            elif op == 12:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                grafo.existe_aresta(v1, v2)

            elif op == 13:
                grafo.numero_vertices()
                grafo.numero_arestas()

            elif op == 14:
                grafo.grafo_vazio()

            elif op == 15:
                grafo.grafo_completo()

            elif op == 16:
                grafo.conectividade()

            elif op == 17:
                grafo.kosaraju()

            elif op == 18:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
                grafo.e_ponte(v1, v2)

            elif op == 19:
                v = int(input("Digite o vértice: "))
                grafo.e_articulacao(v)

            elif op == 20:
                grafo.imprimir_matriz_adjacencia()

            elif op == 21:
                grafo.imprimir_matriz_incidencia()

            elif op == 22:
                grafo.imprimir_lista_adjacencia()

            elif op == 23:
                grafo.fleury_naive()

            elif op == 24:
                grafo.fleury_tarjan()

            elif op == 25:
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