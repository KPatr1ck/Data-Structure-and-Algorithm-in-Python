#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class LRUCache:
    """
    单链表实现的LRU

    Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

    get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
    set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
    """
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.count = 0
        self.head = Node()

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
            self._delete(p.next.key)

        while p.next:
            p = p.next
        p.next = node
        self.count += 1

    def get(self, key):
        """
        获取对应key节点的值
        访问后需要将节点放到链表末尾
        """
        p = self.head
        while p.next:
            if p.next.key == key:
                ret = p.next.value
                self._move_to_end(key, p.next.value)
                return ret
            p = p.next
        return -1

    def set(self, key, value):
        """
        设置对应key节点的值
        key存在时改值，并移动到末尾
        key不存在时直接在尾部插入
        """
        p = self.head
        while p.next:
            if p.next.key == key:
                p.next.value = value
                # 访问后需要移动到末尾
                self._move_to_end(key, value)
                return
            p = p.next

        # key在当前链表不存在
        self._insert(key, value)

    def _delete(self, key):
        # print('delete: {}'.format(key))
        p = self.head

        while p.next:
            if p.next.key == key:
                p.next = p.next.next
                self.count -= 1
                return True
            p = p.next

        return False

    def _move_to_end(self, key, value):
        self._delete(key)
        self._insert(key, value)

    def __repr__(self):
        ret = ''
        prt_data = []
        p = self.head
        while p.next:
            prt_data.append('[{}]: {}'.format(p.next.key, p.next.value))
            p = p.next
        ret = " -> ".join(prt_data)
        return ret


if __name__ == '__main__':
    lru = LRUCache()
    for i in range(10):
        lru.set(i, random.randint(0, 100))
    print(lru)
    lru.set(10, random.randint(0, 100))
    print(lru)
    print(lru.get(5))
    print(lru)
    lru.set(4, 666)
    print(lru)



