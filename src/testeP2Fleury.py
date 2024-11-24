import time
from libGrafos import Grafo

def testar_fleury(tamanhos):
    resultados = {}
    for n in tamanhos:
        print(f"\nTestando Fleury com {n} vértices")
        
        grafo = Grafo(n)
        grafo.graforandom()
        
        # Teste com Fleury Naive
        print("Executando Fleury (Naive)...")
        start_time = time.time()
        try:
            grafo.fleury_naive()
        except Exception as e:
            print(f"Erro em Fleury (Naive): {e}")
        end_time = time.time()
        tempo_naive = end_time - start_time
        print(f"Tempo Fleury (Naive): {tempo_naive:.5f} segundos")
        
        # Teste com Fleury Tarjan
        print("Executando Fleury (Tarjan)...")
        start_time = time.time()
        try:
            grafo.fleury_tarjan()
        except Exception as e:
            print(f"Erro em Fleury (Tarjan): {e}")
        end_time = time.time()
        tempo_tarjan = end_time - start_time
        print(f"Tempo Fleury (Tarjan): {tempo_tarjan:.5f} segundos")
        
        # Salvando resultados
        resultados[n] = {
            "tempo_naive": tempo_naive,
            "tempo_tarjan": tempo_tarjan
        }

    return resultados

# Tamanhos de grafos a serem testados
tamanhos = [5, 10, 50, 100, 500, 1000, 2000, 10000, 100000]

if __name__ == "__main__":
    resultados = testar_fleury(tamanhos)
    print("\nResumo dos resultados:")
    for n, res in resultados.items():
        print(f"\nGrafo com {n} vértices:")
        print(f"  Tempo Fleury (Naive): {res['tempo_naive']:.5f} segundos")
        print(f"  Tempo Fleury (Tarjan): {res['tempo_tarjan']:.5f} segundos")
