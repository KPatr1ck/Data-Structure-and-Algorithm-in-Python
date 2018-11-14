#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
from TreeNode import TreeNode
from binary_tree import Tree


class BinarySearchTree(Tree):
    # 1. 初始化时要用完全二叉树的list
    # 2. 初始化空树，通过插入形成bst
    def __init__(self):
        super(BinarySearchTree, self).__init__()

    def insert(self, data):
        """
        插入
        :param data:
        :return:
        """
        assert(type(data) is int)

        if self.root.val is None:
            self.root.val = data
            return True

        n = self.root
        
        while n:
            # 找到插入的父节点
            p_node = n
            if data < n.val:
                n = n.left
            # 值相等的节点在右子树
            else:
                n = n.right
        
        new_node = TreeNode(data)

        # 插入
        if data < p_node.val:
            p_node.left = new_node
        else:
            p_node.right = new_node

        return True

    def search(self, data):
        """
        查找
        返回所有与查找值相同值的节点
        :param data:
        :return:
        """
        assert (type(data) is int)

        # 同一个值可能会找到多个节点，返回一个节点list
        ret = []
        n = self.root
        while n:
            if data < n.val:
                n = n.left
            else:
                # 值相等的节点在右子树
                if data == n.val:
                    ret.append(n)
                n = n.right
        return ret

    def delete(self, data):
        """
        删除
        所删除的节点N存在以下情况：
        1. 没有子节点：直接删除N的父节点指针
        2. 有一个子节点：将N父节点指针指向N的子节点
        3. 有两个子节点：找到右子树的最小节点M，将值赋给N，然后删除M
        :param data:
        :return:
        """
        assert (type(data) is int)

        n = self.root
        while n:
            p_node = n
            if data < n.val:
                n = n.left
            else:
                # TODO: 查找到时的操作，三种情况
                if data == n.val:
                    pass
                n = n.right
        pass


if __name__ == '__main__':
    #         7
    #      5      8
    #    4   6  N   8
    #  3
    #  
    bst = BinarySearchTree()
    nums = [7, 5, 8, 4, 6, 9, 3]
    # 插入
    for i in nums:
        bst.insert(i)
    print(bst.in_order())

    # for i in range(5):
    #     bst.insert(random.randint(1, 20))
    # print(bst.in_order())

    print('-'*20)
    # 搜索
    for n in bst.search(6):
        print(n.val)

    print('-'*20)
    # 删除


