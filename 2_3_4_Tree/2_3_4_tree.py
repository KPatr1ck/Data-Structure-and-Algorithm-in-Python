#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
from queue import Queue


class TreeNode:
    def __init__(self, v1=None, v2=None, v3=None):
        self.values = [v1, v2, v3]
        self.children = [None] * 4
        self.parent = None

    def is_empty(self):
        return self.values.count(None) == len(self.values)

    def is_full(self):
        return self.values.count(None) == 0

    def values_count(self):
        """
        实际值的个数
        :return:
        """
        return len(self.values) - self.values.count(None)

    def has_children(self):
        return self.children.count(None) < len(self.children)

    def insert_value(self, v):
        """
        插入
        :param v:
        :return:
        """
        assert(type(v) is int)
        if self.is_full():
            raise Exception('try to insert value to a full node: {}'.format(id(self)))

        if self.is_empty():
            self.values[0] = 1
        else:
            # 对存在1个值和2个值的情况分别处理
            if self.values_count() == 1:
                if v < self.values[0]:
                    self.values[0], self.values[1] = v, self.values[0]
                else:
                    self.values[1] = v
            else:
                self.values[2] = v
                self.values.sort()

    def find_child_idx(self, v):
        """
        寻找合适的插入子节点
        根据要插入的数值，找出插入的子节点索引值
        :param v:
        :return:
        """
        assert(not self.is_empty())

        if v < self.values[0]:
            return 0
        if self.values_count() == 1 or v < self.values[1]:
            return 1
        if self.values_count() == 2 or v < self.values[2]:
            return 2
        return 3
            
    def __repr__(self):
        return str(self.values)


class Tree234:
    def __init__(self):
        self.root = None

    def insert(self, v):
        """
        节点的插入
        注意：
        1. 不支持重复的值
        2. 插入动作最终必定发现在子节点
        3. 在查找插入节点的过程中，遇到满的节点，则分裂
        :param v:
        :return:
        """
        assert(type(v) is int)
        if self.search(v):
            raise KeyError('{} is already exist'.format(v))

        if self.root is None:
            self.root = TreeNode(v)
            return

        n = self.root
        # 找到要插入的节点，插入的节点必须是叶子节点
        # 插入过程中，如果遇到满的节点，需要进行分裂
        while n:
            p = n
            child_idx = n.find_child_idx(v)
            n = n.children[child_idx]

            # 分裂后p需要重定位
            if p.is_full():
                new_node = self.split(p)
                # 分裂前向右边走
                if child_idx > 1:
                    p = new_node
                    child_idx -= 2

        # 父节点p的某一个子节点还没创建
        if p.has_children():
            n = TreeNode(v)
            n.parent = p
            p.children[child_idx] = n
        else:
            p.insert_value(v)

    def split(self, node):
        """
        分裂节点
        根节点和非根节点分裂处理的方式不同
        :param node:
        :return:
        """
        # 新节点
        new_node = TreeNode(node.values[2])
        new_node.children[:2] = node.children[2:]
        for n in new_node.children[:2]:
            if n is not None:
                n.parent = new_node
        new_node.parent = node.parent

        # 父节点
        # 注意分裂根节点需要特殊处理
        if node.parent is not None:
            # 普通节点分裂
            node.parent.insert_value(node.values[1])
            # 调整父节点的children指针
            idx = node.parent.children.index(node)
            node.parent.children[idx+1:] = [new_node] + node.parent.children[idx+1:-1]
        else:
            # 根节点分裂
            new_root = TreeNode(node.values[1])
            node.parent, new_node.parent = new_root, new_root
            new_root.children[0], new_root.children[1] = node, new_node
            self.root = new_root

        # 原节点
        node.values[1:] = [None, None]
        node.children[2:] = [None, None]

        return new_node

    def delete(self, v):
        assert(type(v) is int)
        pass

    def search(self, v):
        """
        按值搜索
        :param v:
        :return:
        """
        assert(type(v) is int)

        n = self.root
        while n:
            if v in n.values:
                return n
            child_idx = n.find_child_idx(v)
            n = n.children[child_idx]

        return None

    def _bfs(self):
        q = Queue()
        q.put(self.root)

        ret = []
        while not q.empty():
            n = q.get()
            if n is not None:
                ret.append(n.values)
                for c in n.children:
                    q.put(c)

        return ret

    def __repr__(self):
        return str(self._bfs())


if __name__ == '__main__':
    #                [10,     20]
    #           /          \       \
    #       [1, 2]    [11, 12]    [40]
    #                                \
    #                                [55]
    t1 = Tree234()
    n1 = TreeNode(10, 20)
    n2 = TreeNode(1, 2)
    n3 = TreeNode(11, 12)
    n4 = TreeNode(40)
    t1.root = n1
    n1.children[0] = n2
    n1.children[1] = n3
    n1.children[2] = n4
    n2.parent = n3.parent = n4.parent = n1
    n5 = TreeNode(55)
    n4.children[1] = n5
    n5.parent = n4
    print(t1)

    print('-' * 50)

    t2 = Tree234()
    nums_set = list(range(1, 11))
    for n in nums_set:
        t2.insert(n)
    print(t2)
