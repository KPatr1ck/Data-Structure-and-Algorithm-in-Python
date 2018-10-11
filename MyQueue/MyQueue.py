#!/usr/bin/python
# -*- coding: UTF-8 -*-


class MyQueue:
    """
    用数组实现队列，入队enqueue，出队dequeue
    """
    def __init__(self, n=10):
        self.length = n
        self.data = [None] * self.length
        self.head = self.tail = 0

    def enqueue(self, data):
        if self.is_full():
            return False
        # tail为None表示此时的尾部已经不能插入，需要搬移数据
        if self.tail > self.length - 1:
            self._shift_data()

        self.data[self.tail] = data
        self.tail += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        ret = self.data[self.head]
        self.head += 1
        return ret

    def _shift_data(self):
        for i in range(self.length - self.head):
            self.data[i] = self.data[i+self.head]
        self.tail = self.length - self.head
        self.head = 0

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.head == 0 and self.tail > self.length - 1

    def __repr__(self):
        return ','.join(map(str, self.data[self.head:self.tail]))
