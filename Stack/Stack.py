#!/usr/bin/python
# -*- coding: UTF-8 -*-


class Stack:
    """
    基础栈
    """
    # n为栈的最大存储空间
    def __init__(self, n=10):
        self.data = []
        self.length = 0
        self.max = n

    def push(self, data):
        if self.is_full():
            raise Exception("this stack ia already full...")
        self.data.append(data)
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise Exception("this stack is empty...")
        self.length -= 1
        return self.data.pop() 

    def is_empty(self):
        return self.length == 0

    def is_full(self):
        return self.length >= self.max

    def __repr__(self):
        return ','.join(map(str, self.data))


class AdaptiveStack(Stack):
    """
    动态扩容栈
    """
    def push(self, data):
        if self.is_full():
            raise Exception("this stack ia already full...")
        # 模拟扩容
        if self.length == self.max:
            self.max *= 2
            new_data = self.data.copy()
            del self.data
            self.data = new_data

        self.data.append(data)
        self.length += 1

    def is_full(self):
        return False


if __name__ == '__main__':
    stack = AdaptiveStack()
    for i in range(11):
        stack.push(i)
    print(stack)

    while not stack.is_empty():
        print(stack.pop())







