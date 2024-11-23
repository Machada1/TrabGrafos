import time
from libGrafos import Grafo

def testar_grafos(tamanhos):
    resultados = {}
    for n in tamanhos:
        print(f"Testando grafo com {n} vértices")
        

        grafo = Grafo(n)
        grafo.graforandom()  
        
        # Teste do método ingênuo
        # start_time = time.time()
        # ponte_naive = []
        # for aresta in grafo.array_arestas:
        #     if grafo.e_ponte(aresta.V1.indice, aresta.V2.indice, prnt=False):
        #         ponte_naive.append((aresta.V1.indice, aresta.V2.indice))  # Adiciona a aresta identificada como ponte
        # end_time = time.time()
        # print(f"Tempo ingênuo para {n} vértices: {end_time - start_time:.5f} segundos")

        # Teste do método de Tarjan
        start_time = time.time()
        pontes_tarjan = grafo.detectar_ponte_tarjan()
        end_time = time.time()
        print(f"Tempo Tarjan para {n} vértices: {end_time - start_time:.5f} segundos")

        # Armazenar os resultados no dicionário
        resultados[n] = {
            #"pontes_naive": ponte_naive,
            "pontes_tarjan": pontes_tarjan,
        }
    return resultados

# Defina os tamanhos de grafo a serem testados
tamanhos = [10,100,1000,10000,100000]

if __name__ == "__main__":
    resultados = testar_grafos(tamanhos)
    for n, res in resultados.items():
        print(f"Resultados para grafo com {n} vértices:")
       # print(f"Pontes (Naive): {res['pontes_naive']}")
        print(f"Pontes (Tarjan): {res['pontes_tarjan']}")
