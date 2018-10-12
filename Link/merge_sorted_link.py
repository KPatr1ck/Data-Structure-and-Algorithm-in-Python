#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Link import *


def merge_sorted_link(link1, link2):
    """
    合并两个有序的链表(默认从小到大)
    :param link1: 原始有序链表1
    :param link2: 原始有序链表2
    :return: Link, 合并后的有序链表
    """

    link_merged = Link()
    p1 = link1.get_first_node()
    p2 = link2.get_first_node()

    while p1 or p2:
        if not p1:
            link_merged.cat_with_node(p2)
            break
        elif not p2:
            link_merged.cat_with_node(p1)
            break
        else:
            if p1.data >= p2.data:
                link_merged.append(p2.data)
                p2 = link2.get_next_node(p2)
            else:
                link_merged.append(p1.data)
                p1 = link1.get_next_node(p1)

    return link_merged


if __name__ == '__main__':
    link1 = Link()
    link2 = Link()
    for i in range(5):
        link1.append(2*i+1)
        link2.append(2)
    print(merge_sorted_link(link1, link2))
