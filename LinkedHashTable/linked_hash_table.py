#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedHashTable:
    _HASH_TABLE_SIZE = 10

    def __init__(self, capacity=10):
        self.capacity = capacity
        # 为每个散列值指向的链表初始化一个哨兵节点
        self.table = []
        for i in range(capacity):
            p = Node()
            self.table.append(p)

    def _hash(self, data):
        """
        简单哈希处理
        取模
        """
        return int(data) % type(self)._HASH_TABLE_SIZE

    def insert(self, data):
        # 当前只支持整数的插入
        assert(type(data) in [int])
        node = Node(data)
        idx = self._hash(data)
        p = self.table[idx]

        while p.next:
            p = p.next

        p.next = node

    def delete(self, data):
        """
        删除节点
        如果存在值相同的节点，只删除第一个
        """
        idx = self._hash(data)
        p = self.table[idx]

        while p.next:
            if p.next.data == data:
                p.next = p.next.next
                return True
            p = p.next

        return False

    def search(self, data):
        """
        查找节点
        如果存在值相同的节点，返回第一个
        """
        idx = self._hash(data)
        p = self.table[idx]

        while p.next:
            if p.next.data == data:
                return p.next
            p = p.next

        return None

    def __repr__(self):
        ret = ''
        for i in range(type(self)._HASH_TABLE_SIZE):
            prt_data = []
            p = self.table[i]
            while p.next:
                prt_data.append(p.next.data)
                p = p.next
            ret += '{} | '.format(i) + " -> ".join(map(str, prt_data)) + '\n'
        return ret


if __name__ == '__main__':
    t = LinkedHashTable()
    for i in range(50):
        t.insert(random.randint(0, 30))
    print(t)

    p = t.search(11)
    print(p.data)
    t.delete(11)
    print(t)
