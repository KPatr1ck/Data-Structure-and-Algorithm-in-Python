#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def merge_sort(l: List[int], start: int, end: int) -> None:  # 原地稳定， 但merge中有空间消耗
    if start >= end:
        return

    mid = (start + end)//2
    merge_sort(l, start, mid)
    merge_sort(l, mid+1, end)
    merge(l, start, mid, end)


def merge(l: List[int], start: int, mid: int, end: int) -> None:
    tmp = []

    i, j = start, mid+1
    while i <= mid and j <= end:
        if l[i] <= l[j]:
            tmp.append(l[i])
            i += 1
        else:
            tmp.append(l[j])
            j += 1

    while i <= mid:
        tmp.append(l[i])
        i += 1
    while j <= end:
        tmp.append(l[j])
        j += 1

    l[start: end+1] = tmp


if __name__ == '__main__':
    sort_list = [3, 6, 2, 4, 5, 1]
    print('origin list: ', sort_list)

    merge_sort(sort_list, 0, len(sort_list)-1)
    print('sorted list: ', sort_list)
