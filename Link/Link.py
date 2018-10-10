#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, data=0, node=None):
        self.data = data
        self.p_next = node

    def __repr__(self):
        return str(self.data)


class Link:
    def __init__(self):
        # 哨兵节点
        self.head = Node()
        self.length = 0

    def append(self, data):
        if self.is_empty():
            p = self.head
        else:
            p = self.index(self.length - 1)
        node = Node(data)
        p.p_next = node
        self.length += 1

    def insert(self, idx, data):
        p = self.index(idx)
        node = Node(data)
        node.p_next = p.p_next
        p.p_next = node
        self.length += 1

    def del_by_index(self, idx):
        # 找到所要删除的元素的前一个节点
        if idx == 0:
            p = self.head
        else:
            p = self.index(idx - 1)
        p.p_next = p.p_next.p_next
        self.length -= 1

    def del_by_val(self, val):
        prev_p = self.head
        p = self.get_first_node()
        while p:
            if p.data == val:
                # 找到首个匹配的节点，删除
                prev_p.p_next = p.p_next
                self.length -= 1
                break
            prev_p = prev_p.p_next
            p = p.p_next

    def search_by_val(self, val):
        p = self.get_first_node()
        while p:
            if p.data == val:
                return p
            p = p.p_next
        return None

    def is_empty(self):
        return self.length == 0

    def index(self, idx):
        if idx > self.length - 1 or idx < 0:
            raise IndexError('{} is an illegal index'.format(idx))

        p = self.get_first_node()
        while idx:
            p = p.p_next
            idx -= 1
        return p

    def get_first_node(self):
        if self.is_empty():
            raise IndexError('Link has no nodes')
        return self.head.p_next

    def __repr__(self):
        pr_data = []
        p = self.get_first_node()
        while p:
            pr_data.append(p.data)
            p = p.p_next

        return ','.join(map(str, pr_data))
