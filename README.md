Biblioteca de Manipulação de Grafos

Descrição
Este projeto consiste na implementação de uma biblioteca para manipulação de grafos em Python, com foco em diferentes representações de grafos e suas funcionalidades associadas. A biblioteca permite a criação e manipulação de grafos utilizando várias abordagens, além de fornecer algoritmos para verificação de propriedades e análise de conectividade.

Funcionalidades
Representação de Grafos
A biblioteca suporta três formas de representação de grafos:

Matriz de Adjacência: Representa as conexões entre vértices em uma matriz onde cada célula indica se há ou não uma aresta entre dois vértices.
Matriz de Incidência: Usa uma matriz para representar as arestas em relação aos vértices, mostrando quais vértices estão conectados por quais arestas.
Lista de Adjacência: Cada vértice é associado a uma lista que contém seus vértices adjacentes, permitindo um armazenamento mais eficiente de grafos esparsos.
Operações de Manipulação
A biblioteca implementa diversas operações para manipulação de grafos, incluindo:

Criação de Grafo: Permite criar grafos com um número de vértices definido pelo usuário.
Manipulação de Arestas: Adição e remoção de arestas entre vértices.
Rotulação e Ponderação: Atribuição de rótulos e pesos tanto para vértices quanto para arestas.
Verificação de Adjacências: Checagem de adjacências entre vértices e entre arestas.
Verificação de Existência de Arestas: Confirma se uma aresta específica existe entre dois vértices.
Contagem de Componentes: Determinação da quantidade de vértices e arestas no grafo.
Propriedades do Grafo: Checagem se o grafo é vazio, completo, ou se possui conectividade simples, semi-forte ou forte.
Componentes Fortemente Conexos: Identificação de componentes fortemente conexos usando o algoritmo de Kosaraju.
Detecção de Pontes e Articulações: Verifica se há arestas ou vértices cuja remoção desconecta o grafo.
Exportação e Visualização
A biblioteca oferece suporte à exportação de grafos para diferentes formatos de arquivos compatíveis com a ferramenta de visualização de grafos Gephi, permitindo a análise visual dos grafos manipulados. Os formatos suportados incluem:

GEXF
GraphML
GML
GraphViz DOT
