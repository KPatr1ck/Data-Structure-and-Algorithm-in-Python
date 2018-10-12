#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Link import *


def cycle_detect(link):
    """
    链表中环的检测
    :param link: 原始链表
    :return: boolean, True/False
    """
    p = link.get_first_node()
    p_one, p_two = p, p

    while p_one and p_two:
        p_one = p_one.p_next
        p_two = p_two.p_next.p_next if p_two.p_next else None
        
        if p_one == p_two and p_one:
            return True

    return False


if __name__ == '__main__':
    link = Link()
    for i in range(5):
        link.append(i)
    print(link)
    print(cycle_detect(link))
    p = link.get_last_node()
    p.p_next = link.get_first_node()
    print(cycle_detect(link))
    

