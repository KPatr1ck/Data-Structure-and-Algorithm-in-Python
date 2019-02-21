#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List
from queue import Queue
from graphviz import Digraph
import random


class Heap:
    def __init__(self, l: List):
        self.data = l

    def heapify(self) -> None:
        i = len(self.data)//2 - 1
        while i >= 0:
            self.heap_downward(i)
            i -= 1

    def heap_upward(self, idx: int) -> None:
        # 由继承者实现
        pass

    def heap_downward(self, idx: int) -> None:
        # 由继承者实现
        pass

    def search(self, v: int) -> int:
        try:
            return self.data.index(v)
        except ValueError:
            return -1

    def insert(self, v: int) -> None:
        self.data.append(v)
        self.heap_upward(len(self.data) - 1)

    def delete(self, v: int) -> bool:
        if len(self.data) == 0:
            return False

        idx = self.search(v)

        if idx == -1:
            return False

        self.data[idx], self.data[-1] = self.data[-1], self.data[idx]
        self.data.pop()
        self.heap_downward(idx)
        return True

    def pop_top_element(self) -> int or None:
        if len(self.data) == 0:
            return None

        ret = self.data[0]
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.data.pop()
        self.heap_downward(0)
        return ret

    def get_p_idx(self, idx: int) -> int:
        ret = (idx - 1)//2
        if ret >= 0:
            return ret
        else:
            return -1

    def get_lc_idx(self, idx: int) -> int:
        ret = (idx + 1) * 2 - 1
        if ret < len(self.data):
            return ret
        else:
            return -1

    def get_rc_idx(self, idx: int) -> int:
        ret = (idx + 1) * 2
        if ret < len(self.data):
            return ret
        else:
            return -1

    def plot(self) -> None:
        g = Digraph()

        q = Queue()
        q.put(0)
        g.node(str(0), str(self.data[0]))
        while not q.empty():
            p: int = q.get()
            lc = self.get_lc_idx(p)
            rc = self.get_rc_idx(p)
            for c in [lc, rc]:
                if c == -1:
                    break
                edge_color = 'red' if c == rc else 'blue'
                g.node(str(c), str(self.data[c]))
                g.edge(str(p), str(c), color=edge_color)
                q.put(c)

        g.view()

    def __repr__(self):
        return str(self.data)[1:-1]


class MaxHeap(Heap):
    def __init__(self, l: List) -> None:
        super(MaxHeap, self).__init__(l)

    def heap_upward(self, idx: int) -> None:
        while 1:
            p = self.get_p_idx(idx)
            if p == -1:
                return

            if self.data[p] >= self.data[idx]:
                return
            else:
                self.data[p], self.data[idx] = self.data[idx], self.data[p]
                idx = p

    def heap_downward(self, idx: int) -> None:
        p = idx
        while 1:     # 堆是完全二叉树，如果一个节点有孩子节点，则左节点必然存在
            lc_idx = self.get_lc_idx(p)
            rc_idx = self.get_rc_idx(p)

            if lc_idx == -1:
                return

            tmp = p
            if lc_idx != -1:
                if self.data[tmp] < self.data[lc_idx]:
                    tmp = lc_idx

            if rc_idx != -1:
                if self.data[tmp] < self.data[rc_idx]:
                    tmp = rc_idx

            if tmp == p:
                return
            else:
                self.data[p], self.data[tmp] = self.data[tmp], self.data[p]
                p = tmp


class MinHeap(Heap):
    def __init__(self, l: List) -> None:
        super(MinHeap, self).__init__(l)

    def heap_upward(self, idx: int) -> None:
        while 1:
            p = self.get_p_idx(idx)
            if p == -1:
                return

            if self.data[p] <= self.data[idx]:
                return
            else:
                self.data[p], self.data[idx] = self.data[idx], self.data[p]
                idx = p

    def heap_downward(self, idx: int) -> None:
        p = idx
        while 1:     # 堆是完全二叉树，如果一个节点有孩子节点，则左节点必然存在
            lc_idx = self.get_lc_idx(p)
            rc_idx = self.get_rc_idx(p)

            if lc_idx == -1:
                return

            tmp = p
            if lc_idx != -1:
                if self.data[tmp] > self.data[lc_idx]:
                    tmp = lc_idx

            if rc_idx != -1:
                if self.data[tmp] > self.data[rc_idx]:
                    tmp = rc_idx

            if tmp == p:
                return
            else:
                self.data[p], self.data[tmp] = self.data[tmp], self.data[p]
                p = tmp


if __name__ == '__main__':
    l = list(range(20))
    # random.seed(0)
    random.shuffle(l)

    # max heap
    max_heap = MaxHeap(l)
    max_heap.heapify()

    # min heap
    min_heap = MinHeap(l)
    min_heap.heapify()

    min_heap.plot()
