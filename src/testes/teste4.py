import time
from libGrafos import Grafo 

# Teste de desempenho
def testar_grafos(tamanhos):
    for n in tamanhos:
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

# Defina os tamanhos de grafo a serem testados
tamanhos = [100, 1000, 10000, 100000]

# Execute os testes
if __name__ == "__main__":
    testar_grafos(tamanhos)
