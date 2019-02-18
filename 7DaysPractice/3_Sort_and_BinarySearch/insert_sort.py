#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def insert_sort(l: List[int]) -> None:  # 原地稳定
    if len(l) == 0 or len(l) == 1:
        return

    for i in range(1, len(l)):     # 表示l下标从0到i的子序列是有序的
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                l[j], l[j-1] = l[j-1], l[j]
            else:
                break


if __name__ == '__main__':
    sort_list = [3, 6, 2, 4, 5, 1]
    print('origin list: ', sort_list)

    insert_sort(sort_list)
    print('sorted list: ', sort_list)
