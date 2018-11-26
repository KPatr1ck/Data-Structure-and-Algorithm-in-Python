#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import random


class BinaryHeap:
    def __init__(self, data=None):
        self._data = []
        if type(data) is list:
            map(self._type_assert, data)
            self._data = data
            # self.heapify()

        self._length = len(self._data)

    def heapify(self):
        self._heapify(self._data, self._length-1)

    def _heapify(self, data, tail_idx):
        # heapify data[:tail_idx+1]
        if tail_idx <= 0:
            return

        # idx of the Last Parent node
        lp = (tail_idx - 1) // 2

        for i in range(lp, -1, -1):
            self._heap_down(data, i, tail_idx)

    @staticmethod
    def _heap_down(data, idx, tail_idx):
        assert type(data) is list

        lp = (tail_idx - 1) // 2
        # top-down
        while idx <= lp:
            # Left and Right Child index
            lc = 2 * idx + 1
            rc = lc + 1

            # right child exists
            if rc <= tail_idx:
                tmp = lc if data[lc] > data[rc] else rc
            else:
                tmp = lc

            if data[tmp] > data[idx]:
                data[tmp], data[idx] = data[idx], data[tmp]
                idx = tmp
            else:
                break

    def insert(self, num):
        if self._insert(self._data, num):
            self._length += 1

    @staticmethod
    def _insert(data, num):
        assert type(data) is list
        assert type(num) is int

        data.append(num)
        length = len(data)

        # idx of New Node
        nn = length - 1
        # bottom-up
        while nn > 0:
            p = (nn-1) // 2
            if data[nn] > data[p]:
                data[nn], data[p] = data[p], data[nn]
                nn = p
            else:
                break

        return True

    def delete_root(self):
        if self._delete_root(self._data):
            self._length -= 1

    @staticmethod
    def _delete_root(data):
        assert type(data) is list

        length = len(data)
        if length == 0:
            return False

        data[0], data[-1] = data[-1], data[0]
        data.pop()
        length -= 1

        # length == 0 or == 1, return
        if length > 1:
            BinaryHeap._heap_down(data, 0, length-1)

        return True

    @staticmethod
    def _type_assert(num):
        assert type(num) is int

    @staticmethod
    def _draw_heap(data):
        length = len(data)

        if length == 0:
            return 'empty heap'

        layer_num = int(math.log(length, 2)) + 1
        prt_nums = []

        for i in range(layer_num):
            prt_nums.append([])
            for j in range(2**i):
                idx = 2**i + j - 1
                if idx > length - 1:
                    break
                prt_nums[i].append(data[idx])

        ret = ''
        for l in prt_nums:
            ret += str(l)[1:-1] + '\n'
        return ret

    def __repr__(self):
        return self._draw_heap(self._data)


if __name__ == '__main__':
    nums = list(range(7))
    random.shuffle(nums
                   )
    bh = BinaryHeap(nums)
    print(bh)

    # heapify
    bh.heapify()
    print(bh)

    # insert
    bh.insert(100)
    print(bh)

    # delete_root
    bh.delete_root()
    print(bh)
