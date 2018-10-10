#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Link import *


def reverse_link(link):
    """
    实现一个链表的翻转
    :param link: 原始链表
    :return: 无
    """
    prev_p = None
    p = link.get_first_node()

    while p:
        next_p = p.p_next
        p.p_next = prev_p
        # node指针前进
        prev_p = p
        p = next_p

    # 循环过后prev_p指向原来链表的尾部
    link.head.p_next = prev_p


if __name__ == '__main__':
    link = Link()
    for i in range(5):
        link.append(i)

    print('orignal link: {}'.format(link))
    reverse_link(link)
    print('reversed link: {}'.format(link))

