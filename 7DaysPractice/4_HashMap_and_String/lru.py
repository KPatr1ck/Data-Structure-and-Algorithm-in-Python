#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


class Node:
    def __init__(self, v: int = None) -> None:
        self.data = v
        self.prev = None
        self.next = None


class LRU:
    """
    LRU
    1. 新数据插入到链表的头部
    2. 每当缓存命中（即缓存数据被访问），则将数据移到链表的头部
    3. 当链表满的时候，将链表尾部的数据丢弃
    """
    def __init__(self, capacity: int = 10) -> None:
        # 哨兵
        self.head = Node()
        self.tail = self.head
        self.capacity = capacity
        self.length = 0

    def search(self, v: int) -> Node or None:
        p: Node = self.head.next
        while p is not None:
            if p.data == v:
                return p
            p = p.next

        return None

    def add_to_head(self, n: Node) -> None:
        p: Node = self.head.next

        # 将节点加到头部，4个指针的操作
        n.prev = self.head
        n.next = p
        self.head.next = n
        if p is None:
            # p是None，就是当前链表为空
            self.tail = n
        else:
            p.prev = n

        if self.length >= self.capacity:
            # 链表满了，删除尾部节点
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.length += 1

    def move_to_head(self, n: Node) -> None:
        # 将节点断开连接，然后加到头部
        if n == self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            n.prev = None
        else:
            n.prev.next = n.next
            n.next.prev = n.prev
            n.prev, n.next = None, None

        self.length -= 1
        self.add_to_head(n)

    def get_cache(self, v: int) -> int:
        n: Node = self.search(v)
        if n is None:
            n = Node(v)
            self.add_to_head(n)
        else:
            self.move_to_head(n)

        return n.data

    def __repr__(self) -> str:
        prt_str = ''
        p: Node = self.head.next
        while p is not None:
            prt_str += str(p.data)
            if p != self.tail:
                prt_str += ' <-> '
            p = p.next
        prt_str += ' [head: {}, tail: {}] '.format(self.head.next.data, self.tail.data)
        return prt_str


if __name__ == '__main__':
    lru = LRU()
    for i in range(10):
        lru.get_cache(i)
    print(lru)

    lru.get_cache(10)
    print(lru)

    lru.get_cache(5)
    print(lru)
