#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import random
from quick_sort import *

bucket_num = 10


def bucket_sort(num_list):
    """
    桶排序
    根据数值分桶，桶内快排
    :param num_list:
    :return:
    """
    # 10个桶
    # 具体问题按需取值
    # 注意[[]] * 10 这种写法是浅复制10个空数组
    bucket = [[] for _ in range(bucket_num)]
    gap = math.ceil(max(num_list)/bucket_num)
    
    for v in num_list:
        bucket[v//gap].append(v)

    ret = []
    for l in bucket:
        quick_sort(l, 0, len(l)-1)
        ret.extend(l)
    return ret


if __name__ == '__main__':
    a = []
    for i in range(50):
        a.append(random.randint(1, 99))
    print(bucket_sort(a))
