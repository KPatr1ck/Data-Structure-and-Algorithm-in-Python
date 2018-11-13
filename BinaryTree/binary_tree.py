#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MyQueue import MyQueue


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


# Simple Tree
class Tree:
    def __init__(self, val_list=[]):
        self.root = TreeNode()
        self.val_list = val_list
        self._list_to_tree()

    def _list_to_tree(self):
        if not self.val_list:
            return None

        # 两个队列，一个存值，一个存节点
        vq = MyQueue()
        nq = MyQueue()
        
        for n in self.val_list:
            vq.enqueue(n)

        self.root.val = vq.dequeue()
        nq.enqueue(self.root)

        while not nq.is_empty():
            n = nq.dequeue()
            if not vq.is_empty():
                n.left = TreeNode(vq.dequeue())
                nq.enqueue(n.left)
            if not vq.is_empty():
                n.right = TreeNode(vq.dequeue())
                nq.enqueue(n.right)

    def pre_order(self, node):
        if not node:
            return []

        ret = []
        ret.extend([node.val])
        ret.extend(self.pre_order(node.left))
        ret.extend(self.pre_order(node.right))
        return ret

    def in_order(self, node):
        if not node:
            return []

        ret = []
        ret.extend(self.in_order(node.left))
        ret.extend([node.val])
        ret.extend(self.in_order(node.right))
        return ret

    def post_order(self, node):
        if not node:
            return []

        ret = []
        ret.extend(self.post_order(node.left))
        ret.extend(self.post_order(node.right))
        ret.extend([node.val])
        return ret

    def __repr__(self):
        return str(self.val_list)


if __name__ == '__main__':
    t = Tree([1, 2, 3, 4, 5])
    print(t)
    print(t.pre_order(t.root))
    print(t.in_order(t.root))
    print(t.post_order(t.root))
