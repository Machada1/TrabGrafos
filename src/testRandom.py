import time
from libGrafos import Grafo

def testar_graforandom(tamanhos):
    resultados = []  # Lista para armazenar os tempos de execução e arestas geradas

    for n in tamanhos:
        # Inicializando o grafo e medindo o tempo
        grafo = Grafo(n)
        start_time = time.perf_counter()
        grafo.graforandom() 
        end_time = time.perf_counter()

        # Calculando o tempo de execução
        tempo_execucao = end_time - start_time
        num_arestas = grafo.num_arestas

        # Armazenando os resultados
        resultados.append((n, tempo_execucao, num_arestas))

    return resultados

# Definindo os tamanhos a serem testados
tamanhos = [5, 10, 50, 100, 500, 1000, 2000, 5000, 10000, 50000,100000]

if __name__ == "__main__":
    resultados = testar_graforandom(tamanhos)

    # Exibindo os resultados finais
    print("\nResumo dos tempos de geração:")
    for n, tempo, arestas in resultados:
        print(f"{n} vértices: {tempo:.5f} segundos, {arestas} arestas geradas")
