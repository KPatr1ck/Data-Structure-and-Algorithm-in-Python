#!/usr/bin/python
# -*- coding: UTF-8 -*-


def merge(l1, l2):
    """
    merge函数，将两个有序list合并成一个新的有序list
    :param l1: 有序list1
    :param l2: 有序list2
    :return: 合并后的有序序列
    """
    # 容错
    if len(l1) == 0 and len(l2) == 0:
        return -1

    ret = []

    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            ret.append(l1[i])
            i += 1
        else:
            ret.append(l2[j])
            j += 1

    ret.extend(l1[i:])
    ret.extend(l2[j:])
    return ret


def merge_sort(num_list):
    """
    归并排序
    :param num_list:
    :return:
    """
    if len(num_list) == 0 or len(num_list) == 1:
        return num_list
    else:
        mid = len(num_list)//2
        return merge(merge_sort(num_list[:mid]), merge_sort(num_list[mid:]))


if __name__ == '__main__':
    a = [6, 3, 10, 8, 7, 4, 1, 5, 2, 9, 11]
    print(merge_sort(a))

