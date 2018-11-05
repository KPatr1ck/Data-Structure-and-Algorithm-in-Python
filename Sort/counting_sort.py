#!/usr/bin/python
# -*- coding: UTF-8 -*-


def counting_sort(num_list):
    """
    计数排序
    可以看成是一种特殊的桶排序，每个桶容纳的数值唯一
    :param num_list:
    :return:
    """
    # 假设数组中的每个数都是大于等于0的正数
    count = [0] * (max(num_list) + 1)
    ret = [0] * len(num_list)

    for v in num_list:
        count[v] += 1

    for i in range(1, len(count)):
        count[i] = sum(count[i-1:i+1])

    # 反向是为了稳定
    for i in range(len(num_list)-1, -1, -1):
        v = num_list[i]
        ret[count[v]-1] = v
        count[v] -= 1
    return ret


if __name__ == '__main__':
    a = [0, 1, 5, 4, 2, 6]
    print(counting_sort(a))
