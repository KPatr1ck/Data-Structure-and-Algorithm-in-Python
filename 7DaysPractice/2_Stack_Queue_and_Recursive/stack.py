#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import TypeVar, Generic
from link_list import SingleLinkList

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, size: int = 10) -> None:
        self.data = [None for i in range(size)]
        self.size = size
        self.length = 0

    def push(self, element: T) -> bool:
        if self.length >= self.size:
            return False

        self.data[self.length] = element
        self.length += 1
        return True

    def pop(self) -> T:
        if self.length == 0:
            raise Exception('Stack is empty')

        ret = self.data[self.length-1]
        self.length -= 1
        return ret

    def clear(self) -> None:
        if self.length > 0:
            self.pop()

    def is_empty(self) -> bool:
        return self.length <= 0

    def __repr__(self) -> str:
        if self.length == 0:
            return 'Stack is empty'
        else:
            return str(self.data[:self.length])


class StackL(Generic[T]):
    def __init__(self) -> None:
        self.data_linklist = SingleLinkList()
        self.length = 0

    def push(self, element) -> bool:
        self.data_linklist.append(element)
        self.length += 1
        return True

    def pop(self) -> T:
        if self.length == 0:
            raise Exception('Stack is empty')

        ret = self.data_linklist.tail.data
        self.data_linklist.delete_by_node(self.data_linklist.tail)
        self.length -= 1
        return ret

    def is_empty(self) -> bool:
        return self.length <= 0

    def __repr__(self) -> str:
        if self.length == 0:
            return 'Stack is empty'
        else:
            return self.data_linklist.__repr__()


class Browser:
    def __init__(self) -> None:
        self.back_stack = Stack[str]()
        self.forward_stack = Stack[str]()
        self.current_page = None

    def browse(self, page) -> None:
        if self.current_page is not None:
            self.back_stack.push(self.current_page)
        self.forward_stack.clear()
        self.current_page = page

    def forward(self) -> None:
        if self.forward_stack.is_empty():
            return

        self.back_stack.push(self.current_page)
        self.current_page = self.forward_stack.pop()

    def back(self) -> None:
        if self.back_stack.is_empty():
            return

        self.forward_stack.push(self.current_page)
        self.current_page = self.back_stack.pop()

    def __repr__(self):
        prt_str = 'current_page: {}'.format(self.current_page)
        prt_str += '\n'
        prt_str += '[back_stack] : {}'.format(self.back_stack)
        prt_str += '\n'
        prt_str += '[forward_stack] : {}'.format(self.forward_stack)
        return prt_str


if __name__ == '__main__':
    s1 = Stack()
    s2 = StackL()
    for i in range(5):
        s1.push(i+1)
        s2.push(i+1)
    print('s1: ', s1)
    print('s2: ', s2)
    print('')

    print('-'*30)
    print('s1 pop elements: ')
    while s1.length > 0:
        print(s1.pop(), end=', ')

    print('\n')
    print('-'*30)
    print('s2 pop elements: ')
    while s2.length > 0:
        print(s2.pop(), end=', ')

    print('\n')
    print('-'*30)
    print('web browser actions:')
    browser = Browser()
    browser.browse('www.baidu.com')
    browser.browse('www.google.com')
    browser.browse('www.bing.com')
    print(browser, '\n')

    print('go back:')
    browser.back()
    print(browser, '\n')

    print('go forward:')
    browser.forward()
    print(browser)
