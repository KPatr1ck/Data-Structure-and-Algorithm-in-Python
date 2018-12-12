#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pygraphviz as pgv
import random
from queue import Queue
from Stack import Stack

OUTPUT_PATH = 'C:/Users/gz1301/'


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
        graph = pgv.AGraph('graph foo {}', strict=False, directed=False, rankdir='LR')
        for v in range(self._v):
            graph.add_node(v, style='filled', fillcolor='red', fontcolor='white')
        for vertex, neighbors in enumerate(self._adj):
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
        """
        bfs 队列实现
        注意更新访问表的时机，在入队时更新能避免非最短路径的问题
        :param s:
        :param t:
        :return:
        """
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
        """
        dfs 递归实现
        :param s:
        :param t:
        :return:
        """
        assert type(s) is int and type(t) is int
        assert s < self._v and t < self._v

        if s == t:
            return str(s)

        visited = [False] * self._v
        prev = [None] * self._v
        visited[s] = True

        # 减少递归次数
        is_found = False

        def _dfs(source, target):
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
                    _dfs(nb, target)

        _dfs(s, t)
        if is_found:
            return self._path(prev, s, t)
        else:
            return '[bfs] no path found of {} -> {}'.format(s, t)

    def dfs_stack(self, s, t):
        """
        dfs 栈实现
        :param s:
        :param t:
        :return:
        """
        assert type(s) is int and type(t) is int
        assert s < self._v and t < self._v

        if s == t:
            return str(s)

        st = Stack(100)
        visited = [False] * self._v
        prev = [None] * self._v

        st.push(s)
        visited[s] = True
        is_found = False

        while not st.is_empty():
            v = st.pop()
            visited[v] = True
            if v == t:
                is_found = True
                break
            # 倒序入栈
            for i in range(len(self._adj[v]) - 1, -1, -1):
                nb = self._adj[v][i]
                if not visited[nb]:
                    prev[nb] = v
                    st.push(nb)

        if is_found:
            return self._path(prev, s, t)
        else:
            return '[bfs_stack] no path found of {} -> {}'.format(s, t)

    @staticmethod
    def _path_r(mp, s, t):
        """
        递归找搜索路径
        返回反向 t->s 的路径
        :param mp:
        :param s:
        :param t:
        :return:
        """
        ret = [t]
        if s != t:
            ret.extend(Graph._path_r(mp, s, mp[t]))
        return ret

    @staticmethod
    def _path_yield(mp, s, t):
        if s != t:
            yield from Graph._path_yield(mp, s, mp[t])
        yield t

    @staticmethod
    def _path(mp, s, t):
        """
        非递归找搜索路径
        处理后返回正向路径 s->t
        :param mp:
        :param s:
        :param t:
        :return:
        """
        ret = [t]
        while s != t:
            ret.append(mp[t])
            t = mp[t]
        ret.reverse()
        return ' -> '.join(map(str, ret))

    def __repr__(self):
        prt_data = ''
        for vertex, neighbors in enumerate(self._adj):
            prt_data += str(vertex) + ' | ' + str(neighbors) + '\n'
        return prt_data


if __name__ == '__main__':
    g = Graph(15)
    g.random_edges()
    g.draw_graph()
    print('--- graph ---')
    print(g)

    print('--- bfs ---')
    print(g.bfs(2, 5) + '\n')

    print('--- dfs ---')
    print(g.dfs(2, 5) + '\n')

    print('--- dfs_stack ---')
    print(g.dfs_stack(2, 5) + '\n')
