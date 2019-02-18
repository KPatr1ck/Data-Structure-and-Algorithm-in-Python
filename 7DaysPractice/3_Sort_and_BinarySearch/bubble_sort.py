#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def bubble_sort(l: List[int]) -> None:  # 原地稳定
    if len(l) == 0 or len(l) == 1:
        return

    for i in range(len(l)-1):
        for j in range(len(l)-1, i, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]


if __name__ == '__main__':
    sort_list = [3, 6, 2, 4, 5, 1]
    print('origin list: ', sort_list)

    bubble_sort(sort_list)
    print('sorted list: ', sort_list)
