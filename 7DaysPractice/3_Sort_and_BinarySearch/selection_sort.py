#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def selection_sort(l: List[int]) -> None:  # 原地稳定
    if len(l) == 0 or len(l) == 1:
        return

    for i in range(len(l)-1):
        idx = i
        for j in range(i+1, len(l)):
            if l[idx] > l[j]:
                idx = j
        l[i], l[idx] = l[idx], l[i]


if __name__ == '__main__':
    sort_list = [3, 6, 2, 4, 5, 1]
    print('origin list: ', sort_list)

    selection_sort(sort_list)
    print('sorted list: ', sort_list)
