#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Node:
    def __init__(self, data: int=None, p_pre=None, p_next=None) -> None:
        self.data = data
        self.pre, self.next = p_pre, p_next


class LinkList:
    concat_symbol = ' -> '

    def __init__(self) -> None:
        # 哨兵
        self.head = Node()
        self.tail = self.head
        self.length = 0

    def append(self, data: int) -> None:
        pass

    def delete_by_value(self, v: int) -> None:
        pass

    def __len__(self) -> int:
        return self.length

    def __repr__(self) -> str:
        ret = ''
        p: Node = self.head.next

        if p is None:
            return 'empty linklist'
        else:
            while p is not None:
                ret += str(p.data)
                if p != self.tail:
                    ret += self.concat_symbol
                p = p.next
            return ret


class SingleLinkList(LinkList):
    """
    单向链表
    """
    def __init__(self, capacity: int = 10) -> None:
        super(SingleLinkList, self).__init__()
        self.capacity = capacity

    def append(self, data: int) -> None:
        if self.length >= self.capacity:
            raise Exception('the link list is full')
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.length += 1

    def delete_by_node(self, n: Node) -> bool:
        p_pre: Node = self.head
        p: Node = self.head.next

        while p is not None:
            if p == n:  # 找到需要删除的节点
                p_pre.next = p.next
                if p == self.tail:
                    self.tail = p_pre
                self.length -= 1
                return True
            else:
                p_pre = p_pre.next
                p = p.next

        return False

    def delete_by_value(self, v: int) -> bool:
        p_pre: Node = self.head
        p: Node = self.head.next

        while p is not None:
            if p.data == v:
                # found and delete node
                p_pre.next = p.next
                # 如果是尾部，需要更新尾部指针
                if p == self.tail:
                    self.tail = p_pre
                self.length -= 1
                return True
            else:
                p_pre = p_pre.next
                p = p.next

        return False

    def reverse(self) -> None:
        p_pre: Node = self.head.next
        if p_pre is None:
            return

        p: Node = p_pre.next
        p_pre.next = None

        while p is not None:
            tmp = p.next
            p.next = p_pre
            p_pre = p
            p = tmp

        # 更新head和tail
        self.head.next, self.tail = self.tail, self.head.next


class DoubleLinkList(LinkList):
    """
    双向链表
    """
    def __init__(self) -> None:
        super(DoubleLinkList, self).__init__()
        self.concat_symbol = ' <-> '

    def append(self, data) -> None:
        node = Node(data)
        self.tail.next = node
        node.pre = self.tail
        self.tail = node
        self.length += 1

    def delete_by_value(self, v: int) -> bool:
        p: Node = self.head.next
        while p is not None:
            if p.data == v:
                # found and delete node
                p.pre.next = p.next
                # 如果是尾部，需要更新尾部指针
                if p == self.tail:
                    self.tail = p.pre
                else:
                    p.next.pre = p.pre
                return True
            else:
                p = p.next

        return False


class CycleLinkList(LinkList):
    """
    循环链表
    """
    def __init__(self) -> None:
        super(CycleLinkList, self).__init__()
        self.tail.next = self.head

    def append(self, data: int) -> None:
        node = Node(data)
        self.tail.next = node
        self.tail = node
        node.next = self.head
        self.length += 1

    def delete_by_value(self, v: int) -> bool:
        p_pre: Node = self.head
        p: Node = self.head.next
        while p is not None:
            if p.data == v:
                # found and delete node
                p_pre.next = p.next
                # 如果是尾部，需要更新尾部指针
                if p == self.tail:
                    self.tail = p_pre
                return True
            else:
                p_pre = p_pre.next
                p = p.next

        return False

    def __repr__(self):
        ret = ''
        p: Node = self.head.next

        if p is None:
            return 'empty linklist'
        else:
            while p != self.tail:
                ret += str(p.data)
                ret += self.concat_symbol
                p = p.next
            ret += str(self.tail.data) + ' | ' + str(self.head.next.data)
            return ret


def merge_two_sorted_link(a: SingleLinkList, b: SingleLinkList) -> SingleLinkList:
    pa: Node = a.head.next
    pb: Node = b.head.next
    ret: SingleLinkList = SingleLinkList()

    while pa is not None and pb is not None:
        if pa.data <= pb.data:
            ret.append(pa.data)
            pa = pa.next
        else:
            ret.append(pb.data)
            pb = pb.next

    while pa is not None:
        ret.append(pa.data)
        pa = pa.next

    while pb is not None:
        ret.append(pb.data)
        pb = pb.next

    return ret


def get_middle_node(l: SingleLinkList) -> Node:
    fast = l.head.next
    slow = fast

    if fast is None:
        raise Exception('Link List is empty')

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


if __name__ == '__main__':
    # 1
    print('-' * 30)
    print('[Single Link List]:')
    sl = SingleLinkList()
    sl.append(1)
    sl.append(2)
    sl.append(3)
    print(sl)
    sl.reverse()
    print(sl)
    sl.delete_by_value(1)
    print(sl)

    # 2
    print('\n' + '-' * 30)
    print('[Double Link List]:')
    dl = DoubleLinkList()
    dl.append(1)
    dl.append(2)
    dl.append(3)
    print(dl)
    dl.delete_by_value(1)
    print(dl)

    # 3
    print('\n' + '-' * 30)
    print('[Cycle Link List]:')
    rl = CycleLinkList()
    rl.append(1)
    rl.append(2)
    rl.append(3)
    print(rl)
    rl.delete_by_value(1)
    print(rl)

    # 4
    print('\n' + '-' * 30)
    print('[Merge 2 sorted link]:')
    a = SingleLinkList()
    b = SingleLinkList()
    for i in range(5):
        a.append(2*i)
        b.append(2*i+1)
    print(a, '|', b)
    print(merge_two_sorted_link(a, b))

    # 5
    print('\n' + '-' * 30)
    print('[Get the middle node of link]:')
    l: SingleLinkList = SingleLinkList()
    for i in range(5):
        l.append(i)
    print(l)
    print(get_middle_node(l).data)
