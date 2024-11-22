import os
from libGrafos import Grafo

def testar_grafo_gexf():
    grafo = Grafo(3)

    grafo.rotular_vertices(["A", "B", "C"])
    
    grafo.adicionar_aresta(0, 1)
    grafo.adicionar_aresta(0, 2)
    grafo.adicionar_aresta(1, 2)

    grafo.ponderar_vertices([25,24,23])

    grafo.ponderar_arestas({23,24,25})

    
    grafo.rotular_arestas(["Diogo gay","ivo","copão"])


  
    nome_arquivo = "Lastdance16.gexf"
    
    grafo.salvar_grafo_gexf(nome_arquivo)
    

    if os.path.exists(nome_arquivo):
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
        
        with open(nome_arquivo, 'r') as file:
            conteudo = file.read()
            print("Conteúdo do arquivo GEXF gerado:")
            print(conteudo)
    else:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi criado.")

if __name__ == "__main__":
    testar_grafo_gexf()
