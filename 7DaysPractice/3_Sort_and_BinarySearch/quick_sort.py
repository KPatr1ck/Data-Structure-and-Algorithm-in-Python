#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def quick_sort(l: List[int], start: int, end: int) -> None:  # 原地非稳定
    if start >= end:
        return

    pivot = partition(l, start, end)
    quick_sort(l, start, pivot-1)
    quick_sort(l, pivot+1, end)


def partition(l: List[int], start: int, end: int) -> int:
    p = l[end]
    i = start - 1
    for j in range(start, end):
        if l[j] <= p:
            l[i+1], l[j] = l[j], l[i+1]
            i += 1

    l[i+1], l[end] = l[end], l[i+1]
    return i+1


if __name__ == '__main__':
    sort_list = [3, 6, 2, 4, 5, 1]
    print('origin list: ', sort_list)

    quick_sort(sort_list, 0, len(sort_list)-1)
    print('sorted list: ', sort_list)
