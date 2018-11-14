#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Stack import Stack
from binary_tree import Tree


def dfs(root):
    """
    深度遍历
    用栈实现，先访问左子树，所有先压右再压左
    :param root:
    :return:
    """
    if not root:
        return None

    ns = Stack()
    ns.push(root)

    ret = []
    while not ns.is_empty():
        n = ns.pop()
        if n:
            ret.append(n.val)
            ns.push(n.right)
            ns.push(n.left)
    return ret


def dfs_recursive(root):
    """
    深度遍历，递归实现
    :param root:
    :return:
    """
    if not root:
        return []

    ret = [root.val]
    ret.extend(dfs_recursive(root.left))
    ret.extend(dfs_recursive(root.right))

    return ret


if __name__ == '__main__':
    t = Tree([1, 2, 3, 4, 5])
    print(dfs(t.root))
    print(dfs_recursive(t.root))
