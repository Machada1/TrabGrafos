import unittest
from libGrafos import Grafo

class TestGrafo(unittest.TestCase):
    def setUp(self):
        # Inicializa um grafo com 5 vértices para cada teste
        self.grafo = Grafo(5)

    def test_adicionar_aresta(self):
        self.grafo.adicionar_aresta(0, 1)
        self.assertEqual(self.grafo.matriz_adjacencia[0][1], 1)
        self.assertIn((1, 1), self.grafo.lista_adjacencia[0])

    def test_remover_aresta(self):
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.remover_aresta(0, 1)
        self.assertEqual(self.grafo.matriz_adjacencia[0][1], 0)
        self.assertNotIn((1, 1), self.grafo.lista_adjacencia[0])

    def test_sao_adjacentes(self):
        self.grafo.adicionar_aresta(0, 1)
        self.assertTrue(self.grafo.sao_adjacentes(0, 1))
        self.grafo.remover_aresta(0, 1)
        self.assertFalse(self.grafo.sao_adjacentes(0, 1))

    def test_existe_aresta(self):
        self.grafo.adicionar_aresta(0, 1)
        self.assertTrue(self.grafo.existe_aresta(0, 1))
        self.grafo.remover_aresta(0, 1)
        self.assertFalse(self.grafo.existe_aresta(0, 1))

    def test_grafo_vazio(self):
        self.assertTrue(self.grafo.grafo_vazio())
        self.grafo.adicionar_aresta(0, 1)
        self.assertFalse(self.grafo.grafo_vazio())

    def test_grafo_completo(self):
        for u in range(5):
            for v in range(u + 1, 5):
                self.grafo.adicionar_aresta(u, v)
        self.assertTrue(self.grafo.grafo_completo())
        self.grafo.remover_aresta(0, 1)
        self.assertFalse(self.grafo.grafo_completo())

    def test_numero_vertices(self):
        self.assertEqual(self.grafo.numero_vertices(), 5)

    def test_numero_arestas(self):
        self.assertEqual(self.grafo.numero_arestas(), 0)
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.adicionar_aresta(2, 3)
        self.assertEqual(self.grafo.numero_arestas(), 2)

    def test_e_conexo(self):
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.adicionar_aresta(1, 2)
        self.assertFalse(self.grafo.e_conexo())  # Grafo desconexo
        self.grafo.adicionar_aresta(2, 3)
        self.grafo.adicionar_aresta(3, 4)
        self.assertTrue(self.grafo.e_conexo())  # Agora é conexo

    def test_kosaraju(self):
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.adicionar_aresta(1, 2)
        self.grafo.adicionar_aresta(2, 0)
        self.grafo.adicionar_aresta(3, 4)
        componentes = self.grafo.kosaraju()
        self.assertEqual(len(componentes), 2)  # Dois componentes

    def test_e_ponte(self):
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.adicionar_aresta(1, 2)
        self.assertTrue(self.grafo.e_ponte(0, 1))
        self.grafo.adicionar_aresta(0, 2)
        self.assertFalse(self.grafo.e_ponte(0, 1))  # Agora não é mais ponte

    def test_e_articulacao(self):
        self.grafo.adicionar_aresta(0, 1)
        self.grafo.adicionar_aresta(1, 2)
        self.grafo.adicionar_aresta(2, 3)
        self.assertTrue(self.grafo.e_articulacao(1))
        self.grafo.adicionar_aresta(0, 2)
        self.assertFalse(self.grafo.e_articulacao(1))  # Não é mais articulação

if __name__ == '__main__':
    unittest.main()
