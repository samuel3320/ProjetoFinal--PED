from collections import defaultdict
from classes import *

class Grafo:
    def __init__(self, arestas, direcionado=False):
        self.adj = defaultdict(set) 
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        return list(self.adj.keys())

    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]

    def adiciona_arestas(self, arestas):
        for u, v in arestas:
            assert u.__class__.__name__ == 'Switch' and v.__class__.__name__ == 'Computador' or u.__class__.__name__ == 'Switch' and v.__class__.__name__ == 'Switch', 'Só é permitido conexões entre PCs e Switchs (Seguindo a Ordem Switch-PC)'
            u.adicionar_tabela_roteamento(v.mac)
            self.adiciona_arco(u, v)

    def adiciona_arco(self, u, v):
        self.adj[u].add(v)
        if not self.direcionado:
            self.adj[v].add(u)

    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def __len__(self):
        return len(self.adj)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))

    def __getitem__(self, v):
        return self.adj[v]