#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import TypeVar, Generic
from link_list import Node, SingleLinkList

T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self, size: int = 10) -> None:
        self.data = [None for i in range(size)]
        self.size = size
        self.head = 0
        self.tail = 0

    def enqueue(self, element: T) -> bool:
        if self.tail - self.head >= self.size:
            # raise Exception('The queue is full')
            return False

        if self.tail == self.size:  # 触发元素搬移
            for i in range(self.head, self.tail):
                self.data[i-self.head] = self.data[i]

            # 重置头尾指针
            self.tail = self.tail - self.head
            self.head = 0

        self.data[self.tail] = element
        self.tail += 1

    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception('The queue is empty')

        ret = self.data[self.head]
        self.head += 1
        return ret

    def is_empty(self) -> bool:
        return self.head == self.tail

    def __repr__(self) -> str:
        return str(self.data[self.head: self.tail])


class QueueL(Generic[T]):
    def __init__(self, size: int = 10) -> None:
        self.q_linklist: SingleLinkList = SingleLinkList()
        self.size = size
        self.length = 0

    def enqueue(self, element: T) -> bool:
        if self.length > self.size:
            return False

        self.q_linklist.append(element)
        self.length += 1
        return True

    def dequeue(self) -> T:
        head_node: Node = self.q_linklist.head.next
        ret = head_node.data
        self.q_linklist.delete_by_node(head_node)
        self.length -= 1
        return ret

    def is_empty(self) -> bool:
        return self.length == 0

    def __repr__(self) -> str:
        prt_str = ''
        p: Node = self.q_linklist.head.next

        while p is not None:
            prt_str += str(p.data)
            if p.next is not None:
                prt_str += ' -> '
            p = p.next

        return prt_str


class CycleQueue(Generic[T]):
    def __init__(self, size: int = 10) -> None:
        # 循环队列会浪费一个空间，所以是 size + 1
        self.data = [None for i in range(size + 1)]
        self.size = size
        self.head = 0
        self.tail = self.head

    def enqueue(self, element: T) -> bool:
        # if (self.head + self.size + 1 - self.tail) % self.size == 1:
        if self.head - self.tail == 1 or self.head + self.size + 1 - self.tail == 1:
            return False

        self.data[self.tail] = element
        self.tail += 1
        self.tail %= self.size + 1
        return True

    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception('The queue is empty')

        ret = self.data[self.head]
        self.head += 1
        self.head %= self.size + 1
        return ret

    def is_empty(self) -> bool:
        return self.head == self.tail

    def __repr__(self) -> str:
        ret = []
        p = self.head
        while p != self.tail:
            ret.append(self.data[p])
            p += 1
            p %= self.size + 1

        return str(ret) + ' ' + '( head: {}, tail: {} )'.format(self.head, self.tail)


if __name__ == '__main__':
    print('-'*30)
    print('q1: ')
    q1: Queue = Queue[int](5)
    for i in range(5):
        q1.enqueue(i+1)
    print(q1)
    print(q1.dequeue())
    print(q1)
    q1.enqueue(6)
    print(q1)
    print()

    print('-'*30)
    print('q2: ')
    q2: QueueL = QueueL[int](5)
    for i in range(5):
        q2.enqueue(i+1)
    print(q2)
    print(q2.dequeue())
    print(q2)
    q2.enqueue(6)
    print(q2)

    print('-'*30)
    print('q3: cycle queue ')
    q3: QueueL = CycleQueue[int](5)
    for i in range(5):
        q3.enqueue(i+1)
    print(q3)
    print(q3.dequeue())
    print(q3)
    q3.enqueue(6)
    print(q3)
