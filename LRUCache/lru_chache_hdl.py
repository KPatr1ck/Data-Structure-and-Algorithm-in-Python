#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        # 用于解决哈希冲突
        self.hnext = None


class LRUCacheHDL:
    """
    散列表(H)和双向链表(DL)表实现的LRU

    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    """

    # 散列表容量
    _HASH_TABLE_SIZE = 10

    def __init__(self, capacity=10):
        # Cache容量
        self.capacity = capacity
        self.count = 0

        # 双向链表的哨兵节点
        self.head = Node()

        # 链表的tail指针，作用是可以O(1)去定位链表的末尾
        self.tail = self.head

        # 散列表存储的每一个链表哨兵节点
        self.table = []
        for i in range(type(self)._HASH_TABLE_SIZE):
            self.table.append(Node())
            
    def _hash(self, key):
        """
        简单哈希处理
        取模
        """
        return int(key) % type(self)._HASH_TABLE_SIZE

    def _insert(self, key, value):
        """
        插入
        容量未满时，新节点从尾部插入
        容量满时，需要删除头部节点，然后再从尾部插入
        """
        node = Node(key, value)
        p = self.head

        # 满
        if self.count == self.capacity:
            # 原双向链表和HASH的链表都需要处理
            self._delete(p.next.key)

        # 原双向链表
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

        # HASH链表
        idx = self._hash(key)
        hp = self.table[idx]
        while hp.hnext:
            hp = hp.hnext
        hp.hnext = node

        self.count += 1

    def get(self, key):
        """
        获取对应key节点的值
        访问后需要将节点放到链表末尾
        """
        idx = self._hash(key)
        hp = self.table[idx]
        while hp.hnext:
            if hp.hnext.key == key: 
                ret = hp.hnext.value
                # TODO: 可优化成指针操作，这样可以减少一个插入的操作
                self._move_to_end(key, hp.hnext.value)
                return ret
            hp = hp.hnext

        return -1

    def set(self, key, value):
        """
        设置对应key节点的值
        key存在时改值，并移动到末尾
        key不存在时直接在尾部插入
        """
        idx = self._hash(key)
        hp = self.table[idx]

        while hp.hnext:
            if hp.hnext.key == key: 
                hp.hnext.value = value
                self._move_to_end(key, value)
                return
            hp = hp.hnext

        # key在当前链表不存在
        self._insert(key, value)

    def _delete(self, key):
        """
        删除节点
        1. 删除原双向链表中的节点
        2. 删除HASH链表中的节点
        """
        # print('delete: {}'.format(key))
        idx = self._hash(key)
        hp = self.table[idx]
        while hp.hnext:
            if hp.hnext.key == key:
                # 1. 原链表
                hp.hnext.prev.next = hp.hnext.next
                # 如果删除的是原链表的末尾节点，尾指针需要处理
                if hp.hnext == self.tail:
                    self.tail = self.tail.prev
                else:
                    hp.hnext.next.prev = hp.hnext.prev
                # 2. HASH链表
                hp.hnext = hp.hnext.hnext
                self.count -= 1
                return True
            hp = hp.hnext

        return False

    def _move_to_end(self, key, value):
        self._delete(key)
        self._insert(key, value)

    def __repr__(self):
        ret = ''
        for i in range(type(self)._HASH_TABLE_SIZE):
            prt_data = []
            hp = self.table[i]
            while hp.hnext:
                prt_data.append('[{}]: {}'.format(hp.hnext.key, hp.hnext.value))
                hp = hp.hnext
            ret += '{} | '.format(i) + " -> ".join(prt_data) + '\n'
        return ret

    def print_link(self):
        ret = ''
        prt_data = []
        p = self.head
        while p.next:
            prt_data.append('[{}]: {}'.format(p.next.key, p.next.value))
            p = p.next
        ret = " -> ".join(prt_data) + '\n'
        return ret


if __name__ == '__main__':
    lru = LRUCacheHDL()
    for i in range(10):
        lru.set(i, random.randint(0, 100))
    print(lru)
    print(lru.print_link())
    lru.set(10, random.randint(0, 100))
    print(lru)
    print(lru.print_link())
    print(lru.get(5))
    print(lru.print_link())
    lru.set(4, 666)
    print(lru)
    print(lru.print_link())
