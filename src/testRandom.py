import time
from libGrafos import Grafo

def testar_graforandom(tamanhos):
    resultados = {}  # Para armazenar os tempos de execução

    for n in tamanhos:
        print(f"\nTestando grafo aleatório com {n} vértices:")
        grafo = Grafo(n)

        start_time = time.time()
        grafo.graforandom() 
        end_time = time.time()

        tempo_execucao = end_time - start_time
        print(f"Tempo de geração para {n} vértices: {tempo_execucao:.5f} segundos")

        resultados[n] = tempo_execucao

        print(f"Vértices: {grafo.num_vertices}, Arestas: {grafo.num_arestas}")

    return resultados

# Definindo os tamanhos a serem testados
tamanhos = [10, 100, 1000, 10000, 100000]

if __name__ == "__main__":
    resultados = testar_graforandom(tamanhos)

    # Exibindo os resultados finais
    print("\nResumo dos tempos de geração:")
    for n, tempo in resultados.items():
        print(f"{n} vértices: {tempo:.5f} segundos")
