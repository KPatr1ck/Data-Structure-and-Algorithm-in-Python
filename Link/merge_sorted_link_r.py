#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, data=0, node=None):
        self.data = data
        self.p_next = node

    def __repr__(self):
        return str(self.data)


class SingleLink:
    """
    单向链表，没有哨兵节点
    """
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, data):
        # 首节点
        if self._is_empty():
            self.head = Node(data)
        else:
            p = self.head
            while p:
                if p.p_next:
                    p = p.p_next
                else:
                    break
            node = Node(data)
            p.p_next = node
        self.length += 1

    def cat(self, node):
        # Node -> Link
        if self._is_empty():
            self.head = node
        else:
            p = self.head
            while p:
                if p.p_next:
                    p = p.p_next
                else:
                    break
            p.p_next = node

        pn = node
        length = 0
        while pn:
            length += 1
            pn = pn.p_next
        self.length += length

    def _is_empty(self):
        return self.length == 0

    def __repr__(self):
        if self._is_empty():
            return str(None)
        pr_data = []
        p = self.head
        while p:
            pr_data.append(p.data)
            p = p.p_next

        return ','.join(map(str, pr_data))        


def merge_sorted_link_r(h1, h2):
    """
    递归实现
    """
    # 返回的是一个头结点Node
    node = None

    if not h1 and not h2:
        return None

    if not h1:
        return h2

    if not h2:
        return h1

    if h1.data <= h2.data:
        node = Node(h1.data)
        node.p_next = merge_sorted_link_r(h1.p_next, h2)
    else:
        node = Node(h2.data)
        node.p_next = merge_sorted_link_r(h1, h2.p_next)

    return node


if __name__ == '__main__':
    l1 = SingleLink()
    l2 = SingleLink()
    for i in range(5):
        l1.append(2*i+1)
        l2.append(2*(i+1))
    print(l1)
    print(l2)

    lm = SingleLink()
    p = merge_sorted_link_r(l1.head, l2.head)
    lm.cat(p)
    print(lm)