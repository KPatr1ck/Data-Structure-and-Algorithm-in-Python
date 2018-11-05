#!/usr/bin/python
# -*- coding: UTF-8 -*-

from binary_search import *


def square_root(num, acc):
    """
    求一个数的平方根，二分查找实现
    :param num: 数
    :param acc: 精度
    :return: 根
    """

    v = list(range(int(num)))
    res = v[binary_search_ll([i**2 for i in v], num)]

    for p in range(acc):
        v = [round(res + i/10**(p+1), p+1) for i in range(10)]
        res = v[binary_search_ll([i**2 for i in v], num)]

    return res


if __name__ == '__main__':
    print(square_root(28.8, 5))