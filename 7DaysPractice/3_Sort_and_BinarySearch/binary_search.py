#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def binary_search(l: List[int], v: int) -> int:     # 如果搜到了返回idx，否则-1
    start, end = 0, len(l)-1
    while start <= end:
        mid = (start + end)//2
        if v < l[mid]:
            end = mid - 1
        elif v > l[mid]:
            start = mid + 1
        else:   # found
            return mid
    return -1


def binary_search_fl(l: List[int], v: int) -> int:
    # first large
    start, end = 0, len(l)-1
    while start <= end:
        mid = (start + end)//2
        if v < l[mid]:
            if mid == 0 or v > l[mid-1]:
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1
    return -1


if __name__ == '__main__':
    l = [3, 5, 8, 18, 18, 22]
    print('-'*30)
    print('The array: {}'.format(l))
    print()

    v = 22
    print('-'*30)
    print('serch for {}, result: {}'.format(v, binary_search(l, v)))
    print()

    v = 6
    print('-'*30)
    print('serch for {}, result: {}'.format(v, binary_search(l, v)))
    print()

    print('-'*30)
    v = 17
    idx = binary_search_fl(l, v)
    print('serch for the first number larger than {}, idx: {}, result: {}'.format(v, idx, l[idx]))
