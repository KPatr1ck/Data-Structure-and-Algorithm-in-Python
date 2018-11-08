#!/usr/bin/python
# -*- coding: UTF-8 -*-


def radix_sort(num_list):
    """
    基数排序
    :param num_list: 
    :return:
    """
    # 数组内最大的数的位数
    count = len(str(max(num_list)))
    print(count)

    ret = num_list
    for i in range(count):
        ret = bucket_sort_ex(ret, i+1)
    
    return ret    


def bucket_sort_ex(num_list, pos):
    """
    扩展桶排序
    根据指定的位作为基准排序
    :param num_list: 数组
    :param pos: 指定位置，1,2,3……分别表示个十百……
    :return:
    """
    # 0-9，10个桶
    bucket = [[] for i in range(10)]

    for v in num_list:
        bucket[(v//10**(pos-1)%10)].append(v)

    ret = []
    for l in bucket:
        ret.extend(l)

    return ret


if __name__ == '__main__':
    a = [1581525952, 1562513503, 1591535246, 1360007606, 1767779654, 1767679493]
    print(radix_sort(a))
