#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import TypeVar, Generic, List, Generator
from graphviz import Digraph
from queue import Queue
import random

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T = None) -> None:
        self.data: T = data
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None
        # 二叉树的节点序号，另外提供给画图用
        self.node_id: int = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, v: int) -> bool:
        if self.root is None:
            self.root = Node[int](v)
            self.root.node_id = 1
            return True

        p: Node = self.root
        while p is not None:
            if v < p.data:
                if p.left is None:
                    break
                else:
                    p = p.left
            elif v > p.data:
                if p.right is None:
                    break
                else:
                    p = p.right
            else:
                # raise Exception('not support for same key')
                return False

        # p是插入节点的父节点
        new_node: Node = Node[int](v)
        new_node.parent = p
        if v < p.data:
            p.left = new_node
            new_node.node_id = p.node_id * 2
        else:
            p.right = new_node
            new_node.node_id = p.node_id * 2 + 1

        return True

    def delete(self, v: int) -> bool:
        n = self.search(v)
        if n is None:
            return False
        else:
            self._delete(n)

    def _delete(self, n: Node) -> None:
        if n.left is None:
            p = n.parent
            if n.data < p.data:
                p.left = n.right
            else:
                p.right = n.right

            if n.right is not None:
                n.right.parent = p
            n.parent = None
        else:
            p = self.find_max(n.left)
            n.data = p.data
            self._delete(p)

    def search(self, v: int) -> Node or None:
        if self.root is None:
            print('This binary tree has no nodes')
            return

        p: Node = self.root
        while p is not None:
            if v == p.data:
                return p
            elif v < p.data:
                p = p.left
            else:
                p = p.right

        return None

    @staticmethod
    def find_max(n: Node) -> Node:
        # 寻找以节点n为根的子树的最大节点
        p = n
        while p.right is not None:
            p = p.right
        return p

    @staticmethod
    def find_min(n: Node) -> Node:
        # 寻找以节点n为根的子树的最小节点
        p = n
        while p.left is not None:
            p = p.left
        return p

    def successor(self, n: Node) -> Node or None:
        if n.right is not None:
            return self.find_min(n.right)
        else:
            if n.parent is None:        # case 1: 没有父节点(根节点)
                return None
            elif n == n.parent.left:    # case 2: n是父节点的左节点
                return n.parent
            elif n == n.parent.right:   # case 3: n是父节点的右节点
                p = n.parent
                while p.parent is not None and p.parent.right == p:
                    p = p.parent
                return p.parent

    def predecessor(self, n: Node) -> Node or None:
        if n.left is not None:
            return self.find_max(n.left)
        else:
            if n.parent is None:        # case 1: 没有父节点(根节点)
                return None
            elif n == n.parent.left:    # case 2: n是父节点的左节点
                p = n.parent
                while p.parent is not None and p.parent.left == p:
                    p = p.parent
                return p.parent
            elif n == n.parent.right:   # case 3: n是父节点的右节点
                return n.parent

    def pre_order(self) -> List:
        ret = []
        self._pre_order(self.root, ret)
        return ret

    def _pre_order(self, n: Node, l: List) -> None:
        if n is None:
            return

        l.append(n.data)
        self._pre_order(n.left, l)
        self._pre_order(n.right, l)

    def mid_order(self) -> List:
        ret = []
        self._mid_order(self.root, ret)
        return ret

    def _mid_order(self, n: Node, l: List) -> None:
        if n is None:
            return

        self._mid_order(n.left, l)
        l.append(n.data)
        self._mid_order(n.right, l)

    # def mid_order2(self) -> Generator[int, None, None]:
    #     """
    #     用生成器实现
    #     :return:
    #     """
    #     return self._mid_order2(self.root)
    #
    # def _mid_order2(self, n: Node) -> Generator[int, None, None]:
    #     if n is None:
    #         return
    #
    #     yield from self._mid_order2(n.left)
    #     yield n.data
    #     yield from self._mid_order2(n.right)

    def post_order(self) -> List:
        ret = []
        self._post_order(self.root, ret)
        return ret

    def _post_order(self, n: Node, l: List) -> None:
        if n is None:
            return

        self._post_order(n.left, l)
        self._post_order(n.right, l)
        l.append(n.data)

    def layer_order(self) -> List:
        ret = []
        self._layer_order(self.root, ret)
        return ret

    def _layer_order(self, n: Node, l: List) -> None:
        if n is None:
            return

        q = Queue()
        q.put(n)

        while not q.empty():
            node: Node = q.get()
            l.append(node.data)
            for c in [node.left, node.right]:
                if c is not None:
                    q.put(c)

    def plot(self) -> None:
        if self.root is None:
            print('This binary tree has no nodes')
            return

        g = Digraph()
        q = Queue()
        p: Node = self.root
        g.node(str(p.node_id), str(p.data))
        q.put(p)

        while not q.empty():
            n: Node = q.get()
            if n.left is not None:
                g.node(str(n.left.node_id), str(n.left.data))
                g.edge(str(n.node_id), str(n.left.node_id))
                q.put(n.left)
            if n.right is not None:
                g.node(str(n.right.node_id), str(n.right.data), color='red')
                g.edge(str(n.node_id), str(n.right.node_id))
                q.put(n.right)

        g.view()


if __name__ == '__main__':
    bt = BinaryTree()
    l = [i for i in range(8)]
    random.seed(0)
    random.shuffle(l)

    for num in l:
        bt.insert(num)
    print(l)

    print(bt.pre_order())
    print(bt.mid_order())
    print(bt.post_order())
    print(bt.layer_order())
    # print(list(bt.mid_order2()))
    bt.plot()
