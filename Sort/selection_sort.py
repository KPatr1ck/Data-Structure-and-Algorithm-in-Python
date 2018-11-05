#!/usr/bin/python
# -*- coding: UTF-8 -*-


def selection_sort(num_list):
    """
    选择排序
    :param num_list:
    :return:
    """
    n = len(num_list)

    for i in range(n-1):
        # 从未排序的元素中找出最小值
        unsorted_min = min(num_list[i:])
        unsorted_min_idx = num_list[i:].index(unsorted_min) + i

        num_list[i], num_list[unsorted_min_idx] = num_list[unsorted_min_idx], num_list[i]

    return num_list


if __name__ == '__main__':
    print(selection_sort([1, 3, 4, 5, 2]))
    print(selection_sort([1, 2, 3, 4, 5]))
    print(selection_sort([5, 4, 3, 2, 1]))
