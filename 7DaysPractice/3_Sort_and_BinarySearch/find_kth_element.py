#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List
import random


def find_kth_element(l: List[int], start: int, end: int, k: int) -> int:
    """
    o(n)时间内，查找l中的第k大/小元素，这里找小
    用quick_sort的思想处理，分治，然后根据分区点继续定位查找区间
    :param l:
    :param k:
    :return:
    """
    pivot = partition(l, start, end)

    if pivot == k - 1:
        return l[pivot]
    elif pivot > k - 1:
        return find_kth_element(l, start, pivot-1, k)
    else:
        return find_kth_element(l, pivot+1, end, k)


def partition(l: List[int], start: int, end: int) -> int:
    i = start-1
    p = l[end]

    for j in range(start, end):
        if l[j] <= p:
            l[i+1], l[j] = l[j], l[i+1]
            i += 1

    l[i+1], l[end] = l[end], l[i+1]
    return i+1


if __name__ == '__main__':
    l = []
    random.seed(0)
    for i in range(10):
        l.append(random.randint(1, 10))
    print(l)
    lc = l.copy()
    lc.sort()
    print(lc)

    k = 3
    print(find_kth_element(l, 0, len(l)-1, k))

