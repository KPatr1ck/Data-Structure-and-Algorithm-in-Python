#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random


class Node:
    def __init__(self, data=None, forward=[]):
        self.data = data
        self.forward = forward


class SkipList:
    """
    跳表
    _MAX_LEVEL表示该跳表最大的层数
    """
    _MAX_LEVEL = 5

    def __init__(self):
        # 哨兵节点
        self.head = Node()
        self.level_count = 1
        # 分配好可能会用到的空指针
        self.head.forward = [None] * type(self)._MAX_LEVEL

    def insert(self, data):
        """
        插入节点
        需要维持链表的有序性
        """
        level = self.random_level()

        # 决定这个节点需要在第level层和下面的层都要存在
        # 如果超过了本身的层数，则整个跳表的层数需要更新
        if level > self.level_count:
            self.level_count = level

        # 创建节点
        node = Node(data)
        node.forward = [None] * level

        # 在每一层找到合适的位置插入
        for i in range(level-1, -1, -1):
            p = self.head
            while p.forward[i] and p.forward[i].data < data:
                p = p.forward[i]
            node.forward[i], p.forward[i] = p.forward[i], node

    def delete(self, data):
        """
        删除节点
        如果需要删除的节点存在多层，需要逐个删除
        """
        p = self.head

        for i in range(self.level_count - 1, -1, -1):
            while p.forward[i] and p.forward[i].data < data:
                p = p.forward[i]
            # 下探前判断是否存在需要删除的节点
            if p.forward[i] and p.forward[i].data == data:
                p.forward[i] = p.forward[i].forward[i]

    def find_by_data(self, data):
        """
        根据值查找
        如果链表中有值相同的元素，只返回首个节点
        """
        p = self.head

        # 从顶层往下搜
        for i in range(self.level_count-1, -1, -1):
            # 每一次while找到的p都需要下探，直到最底层退出主循环
            while p.forward[i] and p.forward[i].data < data:
                p = p.forward[i]

        # 此时p为第0层中小于data的最大值节点
        # 若存在值为data的节点，则一定是在下一个
        return p.forward[0] if p.forward[0] and p.forward[0].data == data else -1

    def random_level(self, p=0.5):
        """
        计算节点需要存在的层数
        """
        level = 1
        while random.random() < p and level < type(self)._MAX_LEVEL:
            level += 1
        return level

    def node_idx(self, node):
        """
        返回具体节点的索引值
        """
        # key: id(node)
        # value: index of the linklist
        idx_dict = {}
        idx = 1
        p = self.head
        while p.forward[0]:
            idx_dict[id(p.forward[0])] = idx
            idx += 1
            p = p.forward[0]

        return idx_dict[id(node)]

    def __repr__(self):
        """
        逐层结构化打印
        """
        # 从上往下逐层打印
        ret = ''
        for i in range(self.level_count-1, -1, -1):
            # 打印用
            pre_idx = 0
            p = self.head
            prt_data = []
            while p.forward[i]:
                now_idx = self.node_idx(p.forward[i])
                prt_data.append(' '*(now_idx-pre_idx-1)*5 + str(p.forward[i].data))
                pre_idx = now_idx
                p = p.forward[i]
            if len(prt_data) > 0:
                ret += " -> ".join(prt_data) + '\n'
        return str(ret)


if __name__ == '__main__':
    a = SkipList()
    for i in range(1, 11):
        a.insert(i)
        # a.insert(random.randint(1, 9))
    print(a)
    a.delete(5)
    print(a)
