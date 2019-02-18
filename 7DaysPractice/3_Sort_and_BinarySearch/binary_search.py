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


if __name__ == '__main__':
    l = [3, 5, 8, 18, 18, 22]
    v = 22
    print(binary_search(l, v))
    v = 6
    print(binary_search(l, v))
