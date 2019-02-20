#!/usr/bin/python
# -*- coding: UTF-8 -*-

from link_list import Node, SingleLinkList
from typing import Tuple


class HashMap:
    def __init__(self, capacity: int = 10) -> None:
        self.capacity = capacity
        # 链表法
        self.data = [SingleLinkList() for i in range(self.capacity)]

    def _hash(self, v: int) -> int:
        return v % self.capacity

    def search(self, v: int) -> Tuple[int, Node] or None:
        idx = self._hash(v)
        p: Node = self.data[idx].head.next

        while p is not None:
            if p.data == v:
                return idx, p
            p = p.next

        return None

    def insert(self, v: int) -> bool:
        idx = self._hash(v)
        self.data[idx].append(v)
        return True

    def delete(self, v: int) -> bool:
        try:
            idx, node = self.search(v)
        except TypeError:
            print('delete {} fail'.format(v))
            return False

        self.data[idx].delete_by_node(node)
        return True

    def __repr__(self) -> str:
        ret = ''
        for link_list in self.data:
            ret += '{}\n'.format(link_list)
        return ret


if __name__ == '__main__':
    hash_map = HashMap(5)
    for i in range(10):
        hash_map.insert(i)
    print('-'*30)
    print('HashMap insert:')
    print(hash_map)

    v = 0
    print('-'*30)
    print('delete {}:'.format(v))
    hash_map.delete(v)
    print(hash_map)

    v = 9
    print('-'*30)
    print('search {}:'.format(v))
    print(hash_map.search(v))

