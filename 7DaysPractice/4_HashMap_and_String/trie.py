#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import TypeVar, Generic, List, IO
from queue import Queue
from graphviz import Digraph

T = TypeVar('T')


class TreeNode(Generic[T]):
    def __init__(self, node_id: int, c: T = None) -> None:
        self.node_id = node_id
        self.data = c
        self.children: List['TreeNode'] = []
        self.is_leaf = False

    def add_child(self, c: 'TreeNode') -> None:
        self.children.append(c)

    def get_child(self, c: T = None) -> 'TreeNode' or None:
        for n in self.children:
            if n.data == c:
                return n

        return None

    def children_num(self) -> int:
        return len(self.children)


class Trie:
    def __init__(self) -> None:
        self.root = TreeNode(0)
        self.node_count = 0

    def search_word(self, word: str) -> bool:
        p = self.root

        for i, char in enumerate(word):
            n = p.get_child(char)
            if n is not None:
                p = n
            else:
                return False

        return True if p.is_leaf is True else False

    def add_word(self, word: str) -> None:
        p = self.root
        # idx 用于记录第一个需要添加的节点的索引
        idx = len(word)

        for i, char in enumerate(word):
            n = p.get_child(char)
            if n is not None:
                # n不是None说明目前这个前缀是存在的
                p = n
            else:
                # n不存在，word[i:]需要逐个字符添加节点
                idx = i
                break

        for j in range(idx, len(word)):
            node_id = self.node_count + 1
            n = TreeNode(node_id, word[j])
            p.add_child(n)
            self.node_count += 1
            p = n

        p.is_leaf = True

    def plot(self) -> None:
        g = Digraph()

        q = Queue()
        q.put(self.root)
        g.node(str(self.root.node_id), self.root.data)
        while not q.empty():
            n: TreeNode = q.get()
            for c in n.children:
                node_color = 'red' if c.is_leaf is True else 'black'
                g.node(str(c.node_id), c.data, color=node_color)
                g.edge(str(n.node_id), str(c.node_id))
                q.put(c)

        g.view()


if __name__ == '__main__':
    words = ['patrick', 'pattern', 'jenny', 'jennifer', 'sunday', 'sun']
    trie = Trie()
    for w in words:
        trie.add_word(w)
    # trie.plot()

    word = 'sunday'
    print(trie.search_word(word))
