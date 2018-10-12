#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, data=0, p_node=None, n_node=None):
        self.data = data
        # p_prev可用于双向的链表
        self.p_prev = p_node
        self.p_next = n_node

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

    def cat(self, link):
        if self.is_empty():
            p = self.head
        else:
            p = self.get_last_node()
        p.p_next = link.get_first_node()
        self.length += link.length

    # 兼容头部没有哨兵的链表
    def cat_with_node(self, node):
        p = node
        while p:
            self.append(p.data)
            p = p.p_next

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

    def get_next_node(self, node):
        if self.is_empty():
            raise IndexError('Link has no nodes')
        
        p = self.get_first_node()
        while p:
            if p == node:
                return p.p_next
            p = p.p_next

        raise Exception("can't find this node({}) in link({})".format(id(node), id(self.head)))

    def get_last_node(self):
        if self.is_empty():
            raise IndexError('Link has no nodes')
        return self.index(self.length - 1)


    def __repr__(self):
        if self.is_empty():
            return str(None)
        pr_data = []
        p = self.get_first_node()
        while p:
            pr_data.append(p.data)
            p = p.p_next

        return ','.join(map(str, pr_data))
