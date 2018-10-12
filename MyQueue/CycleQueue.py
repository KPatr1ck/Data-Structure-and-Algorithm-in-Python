#!/usr/bin/python
# -*- coding: UTF-8 -*-


class CycleQueue:
    """
    用数组实现循环队列
    """
    def __init__(self, n=10):
        self.length = n
        self.data = [None] * self.length
        self.head = self.tail = 0

    def enqueue(self, data):
        if self.is_full():
            return False

        self.data[self.tail] = data
        self.tail = (self.tail + 1)%self.length
        return True

    def dequeue(self):
        if self.is_empty():
            return False

        ret = self.data[self.head]
        self.head = (self.head + 1)%self.length
        return ret

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.length - self.tail)%self.length == 1

    def __repr__(self):
        return ','.join(map(str, self.data[self.head:self.tail] if self.head <= self.tail else self.data[self.head:] + self.data[:self.tail]))


if __name__ == '__main__':
    cq = CycleQueue()
    for i in range(9):
        cq.enqueue(i)
    print(cq)
    cq.dequeue()
    cq.enqueue(9)
    print(cq)
