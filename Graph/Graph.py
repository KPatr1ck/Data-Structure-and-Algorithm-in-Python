#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygraphviz as pgv
import random
from queue import Queue
from Stack import Stack

OUTPUT_PATH = 'E:/'


class Graph:
    """
    简单无向图
    """
    def __init__(self, v):
        """
        v是图的顶点数
        v个顶点的值是 0 ~ v-1
        :param v:
        """
        assert type(v) is int
        self._v = v       # 顶点数
        self._adj = []    # 邻接表
        for i in range(self._v):
            self._adj.append([])

    def add_edge(self, s, t):
        assert type(s) is int and type(t) is int
        assert s < self._v and t < self._v

        if t not in self._adj[s]:
            self._adj[s].append(t)

        if s not in self._adj[t]:
            self._adj[t].append(s)

    def draw_graph(self, img_name='Graph.png'):
        graph = pgv.AGraph('graph foo {}', strict=False, directed=False,rankdir='LR')
        for vertex, neighbors in enumerate(self._adj):
            if not graph.has_node(vertex):
                graph.add_node(vertex)
            for n in neighbors:
                if graph.has_edge(vertex, n) or graph.has_edge(n, vertex):
                    continue
                graph.add_edge(vertex, n)

        graph.graph_attr['epsilon'] = '0.01'
        graph.layout('dot')
        graph.draw(OUTPUT_PATH + img_name)
        return True

    def random_edges(self):
        # C(n,2) / 3
        n = self._v * (self._v-1) // (2*3)
        for i in range(n):
            v1, v2 = random.sample(range(self._v), 2)
            self.add_edge(v1, v2)

    def bfs(self, s, t):
        assert type(s) is int and type(t) is int
        assert s < self._v and t < self._v

        if s == t:
            return str(s)

        q = Queue()
        visited = [False] * self._v
        prev = [None] * self._v

        q.put(s)
        visited[s] = True

        while not q.empty():
            v = q.get()
            for nb in self._adj[v]:
                if not visited[nb]:
                    prev[nb] = v
                    if nb == t:
                        return self._path(prev, s, t)
                    # 1. 入队的同时做访问标记，可以防止多余的入队
                    # 2. 保证最短路径
                    visited[nb] = True
                    q.put(nb)

        return '[bfs] no path found of {} -> {}'.format(s, t)

    def dfs(self, s, t):
        assert type(s) is int and type(t) is int
        assert s < self._v and t < self._v

        if s == t:
            return str(s)

        st = Stack(100)
        visited = [False] * self._v
        prev = [None] * self._v

        visited[s] = True
        st.push(s)
        while not st.is_empty():
            v = st.pop()
            for nb in self._adj[v]:
                if not visited[nb]:
                    prev[nb] = v
                    if nb == t:
                        return self._path(prev, s, t)
                    visited[nb] = True
                    st.push(nb)

        return '[dfs] no path found of {} -> {}'.format(s, t)

    def dfs_r(self, s, t):
        assert type(s) is int and type(t) is int
        assert s < self._v and t < self._v

        if s == t:
            return str(s)

        visited = [False] * self._v
        prev = [None] * self._v
        visited[s] = True

        # 减少递归次数
        is_found = False

        def _dfs_r(source, target):
            nonlocal is_found
            for nb in self._adj[source]:
                if is_found:
                    return
                if not visited[nb]:
                    prev[nb] = source
                    if nb == target:
                        is_found = True
                        return
                    visited[nb] = True
                    _dfs_r(nb, target)

        _dfs_r(s, t)
        return self._path(prev, s, t)

    @staticmethod
    def _path_r(mp, s, t):
        ret = [t]
        if s != t:
            ret.extend(Graph._path_r(mp, s, mp[t]))
        return ret

    @staticmethod
    def _path(mp, s, t):
        ret = [t]
        while s != t:
            ret.append(mp[t])
            t = mp[t]
            if t is None:
                return 'no path found'
        ret.reverse()
        return ' -> '.join(map(str, ret))

    def __repr__(self):
        prt_data = ''
        for vertex, neighbors in enumerate(self._adj):
            prt_data += str(vertex) + ' | ' + str(neighbors) + '\n'
        return prt_data


if __name__ == '__main__':
    g = Graph(20)
    g.random_edges()
    g.draw_graph()
    print('--- graph ---')
    print(g)

    print('--- bfs ---')
    print(g.bfs(2, 5) + '\n')

    print('--- dfs ---')
    print(g.dfs(2, 5) + '\n')

    print('--- dfs_r ---')
    print(g.dfs_r(2, 5) + '\n')
