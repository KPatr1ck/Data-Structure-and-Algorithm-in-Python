#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List, TypeVar, Generic
from queue import Queue
from graphviz import Digraph
import numpy as np

T = TypeVar('T')


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


class HeapSort(MaxHeap):
    def __init__(self, l: list) -> None:
        super(HeapSort, self).__init__(l)

    def sort(self) -> None:
        self.heapify()
        for i in range(len(self.data)-1):
            target_pos = len(self.data)-1-i
            self.data[0], self.data[target_pos] = self.data[target_pos], self.data[0]
            self.heap_downward_to_idx(target_pos-1)

    def heap_downward_to_idx(self, end_idx: int) -> None:
        if end_idx <= 0:
            return

        p = 0
        while 1:
            lc_idx = self.get_lc_idx(p)
            rc_idx = self.get_rc_idx(p)

            tmp = p
            if lc_idx != -1 and lc_idx <= end_idx:
                if self.data[tmp] < self.data[lc_idx]:
                    tmp = lc_idx

            if rc_idx != -1 and rc_idx <= end_idx:
                if self.data[tmp] < self.data[rc_idx]:
                    tmp = rc_idx

            if tmp == p:
                return
            else:
                self.data[p], self.data[tmp] = self.data[tmp], self.data[p]
                p = tmp


class TopKFilter(MinHeap):
    def __init__(self, l: List, k: int) -> None:
        assert k <= len(l)
        self.full_data = l
        super(TopKFilter, self).__init__(l[:k])

    def gen_top_k(self) -> None:
        self.heapify()

        k = len(self.data)
        # 首先建立了大小为k的小顶堆
        # 遍历剩余元素，如果比小顶堆堆顶大，将堆顶换成当前元素，并堆化堆顶元素
        for i in range(k, len(self.full_data)):
            self.update_top_element(self.full_data[i])

    def update_top_element(self, v: int) -> None:
        if v > self.data[0]:
            self.data[0] = v
            self.heap_downward(0)

    def insert(self, v: int):
        self.full_data.append(v)
        self.update_top_element(v)


class PriorityQueue(MinHeap, Generic[T]):
    def __init__(self, size: int) -> None:
        super(PriorityQueue, self).__init__([])
        self.size = size

    def put(self, element: T) -> bool:
        if len(self.data) >= self.size:
            return False

        self.data.append(element)
        self.heap_upward(len(self.data)-1)

    def get(self) -> int or bool:
        if self.is_empty():
            return False

        return self.pop_top_element()

    def is_empty(self) -> bool:
        return len(self.data) == 0


class Node:
    def __init__(self, v: int, idx: int) -> None:
        self.value = v
        self.from_list_idx = idx

    def __eq__(self, other: 'Node') -> bool:
        return self.value == other.value

    def __ge__(self, other: 'Node') -> bool:
        return self.value >= other.value

    def __gt__(self, other: 'Node') -> bool:
        return self.value > other.value


def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    ret = []
    k = len(lists)
    pq: PriorityQueue = PriorityQueue[Node](k)

    pointers = [0 for i in range(k)]
    for i in range(k):
        pq.put(Node(lists[i][0], i))

    while not pq.is_empty():
        n: Node = pq.get()
        v, from_list = n.value, n.from_list_idx
        ret.append(v)
        pointers[from_list] += 1

        cur_list = lists[from_list]
        cur_pointer = pointers[from_list]
        # 找出当前出队的元素的来源，继续从该数组取元素入队，直到取出了所有元素
        if cur_pointer < len(cur_list):
            pq.put(Node(cur_list[cur_pointer], from_list))

    return ret


if __name__ == '__main__':
    # np.random.seed(0)
    l = list(np.random.randint(0, 10, 8))
    print('original list:')
    print(l)

    # max heap
    max_heap = MaxHeap(l)
    max_heap.heapify()

    # min heap
    min_heap = MinHeap(l)
    min_heap.heapify()

    # min_heap.plot()

    k = 5
    print('-'*30)
    print('top {}:'.format(k))
    tk = TopKFilter(l, k)
    tk.gen_top_k()
    print(tk.data)
    tk.insert(10)
    tk.insert(6)
    print(tk.data)

    l_for_sort = l.copy()
    hs = HeapSort(l_for_sort)
    hs.sort()
    print('-'*30)
    print('sorted list:')
    print(l_for_sort)

    print('-'*30)
    print('priority queue:')
    pq = PriorityQueue[int](len(l))
    for _ in l:
        pq.insert(_)
    print(pq)
    # while not pq.is_empty():
    #     print(pq.get())

    k = 3
    print('-'*30)
    print('merge {} sorted lists:\n'.format(k))
    lists = []
    print('original lists:')
    for i in range(k):
        l_i = list(np.random.randint(0, 10, 8))
        l_i.sort()
        print('l_{}: '.format(i), l_i)
        lists.append(l_i)

    print('\nmerge result:')
    print(merge_k_sorted_lists(lists))
