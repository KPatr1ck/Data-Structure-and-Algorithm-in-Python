#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MyQueue import MyQueue
from TreeNode import TreeNode


# Simple Tree
class Tree:
    def __init__(self, val_list=[]):
        self.root = TreeNode()
        if val_list:
            self._list_to_tree(val_list)

    def _list_to_tree(self, val_list):
        """
        初始化树的时候，将数组转成树结构
        :param val_list:
        :return:
        """
        # 两个队列，一个存值，一个存节点
        vq = MyQueue()
        nq = MyQueue()
        
        for n in val_list:
            vq.enqueue(n)

        self.root.val = vq.dequeue()
        nq.enqueue(self.root)

        while not nq.is_empty():
            n = nq.dequeue()
            if not vq.is_empty():
                v = vq.dequeue()
                if v is not None:
                    n.left = TreeNode(v)
                    nq.enqueue(n.left)
            if not vq.is_empty():
                v = vq.dequeue()
                if v is not None:
                    n.right = TreeNode(v)
                    nq.enqueue(n.right)

    def _cbt_to_list(self):
        """
        树结构转成数组表示，这里只能完美处理完全二叉树
        :return:
        """
        # must be a complete binary tree
        nq = MyQueue()
        nq.enqueue(self.root)

        ret = []
        while not nq.is_empty():
            n = nq.dequeue()
            if n:
                ret.append(n.val)
                nq.enqueue(n.left)
                nq.enqueue(n.right)
            else:
                ret.append(None)

        return ret

    def pre_order(self):
        """
        先序遍历
        :return:
        """
        return self._pre_order(self.root)

    def _pre_order(self, node):
        if not node:
            return []

        ret = []
        ret.extend([node.val])
        ret.extend(self._pre_order(node.left))
        ret.extend(self._pre_order(node.right))
        return ret

    def in_order(self):
        """
        中序遍历
        :return:
        """
        return self._in_order(self.root)

    def _in_order(self, node):
        if not node:
            return []

        ret = []
        ret.extend(self._in_order(node.left))
        ret.extend([node.val])
        ret.extend(self._in_order(node.right))
        return ret

    def post_order(self):
        """
        后序遍历
        :return:
        """
        return self._post_order(self.root)

    def _post_order(self, node):
        if not node:
            return []

        ret = []
        ret.extend(self._post_order(node.left))
        ret.extend(self._post_order(node.right))
        ret.extend([node.val])
        return ret

    def __repr__(self):
        return 'coming soon...'


if __name__ == '__main__':
    t = Tree([1, 2, 3, 4, None, 5])
    print(t.pre_order())
    print(t.in_order())
    print(t.post_order())

    print('-'*30)
    t1 = Tree([1, 2, 3, 4, 5])
    print(t1.pre_order())
    print(t1.in_order())
    print(t1.post_order())
