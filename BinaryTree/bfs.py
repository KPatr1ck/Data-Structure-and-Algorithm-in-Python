#!/usr/bin/python
# -*- coding: UTF-8 -*-

from MyQueue import MyQueue
from binary_tree import Tree


def bfs(root):
    """
    广度遍历
    用队列实现，将每层节点左右顺序入队
    :param root:
    :return:
    """
    if not root:
        return None

    nq = MyQueue()
    nq.enqueue(root)

    ret = []
    while not nq.is_empty():
        n = nq.dequeue()
        if n:
            ret.append(n.val)
            nq.enqueue(n.left)
            nq.enqueue(n.right)
    return ret


if __name__ == '__main__':
    t = Tree([1, 2, 3, 4, 5])
    print(bfs(t.root))
