import time
from libGrafos import Grafo 

def testar_grafos(tamanhos):
    resultados = {}  
    for n in tamanhos:
        try:
            print(f"Testando grafo com {n} vértices")
            
            grafo = Grafo(n)  # Cria o grafo com n vértices
            num_arestas = min(n * (n - 1) // 2, 10 * n)  # Definindo um número razoável de arestas

            grafo.graforandom(num_arestas)  # Gerando arestas aleatórias

            # Teste o método ingênuo
            start_time = time.time()
            pontes_naive = grafo.detectar_ponte_naive()
            end_time = time.time()
            print(f"Tempo ingênuo para {n} vértices: {end_time - start_time:.5f} segundos")

            # Teste o método de Tarjan
            start_time = time.time()
            pontes_tarjan = grafo.detectar_ponte_tarjan()
            end_time = time.time()
            print(f"Tempo Tarjan para {n} vértices: {end_time - start_time:.5f} segundos")

        except Exception as e:
            print(f"Erro ao testar grafo com {n} vértices: {e}")
            pontes_naive = []  # Defina um valor padrão (pode ser uma lista vazia ou None)
            pontes_tarjan = []

        # Armazenar os resultados no dicionário, mesmo que haja erro
        resultados[n] = {
            "pontes_naive": pontes_naive,
            "pontes_tarjan": pontes_tarjan,
        }
    return resultados

tamanhos = [100, 1000, 10000, 100000]

if __name__ == "__main__":
    resultados = testar_grafos(tamanhos)
    for n, res in resultados.items():
        print(f"Resultados para grafo com {n} vértices:")
        print(f"Pontes (Naive): {res['pontes_naive']}")
        print(f"Pontes (Tarjan): {res['pontes_tarjan']}")
