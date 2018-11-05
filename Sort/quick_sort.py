#!/usr/bin/python
# -*- coding: UTF-8 -*-


def quick_sort(num_list, start, end):
    """
    快速排序
    :param num_list: 数组
    :param start: 起点
    :param end: 终点
    :return: none，原地排序
    """
    if start >= end:
        return 
    
    # 自顶向下，先处理，后递归子问题
    p = partition(num_list, start, end)
    quick_sort(num_list, start, p-1)
    quick_sort(num_list, p+1, end)


def partition(num_list, start, end):
    """
    分区
    1. 选择锚点
    2. 数组指针i，用于表示num_list[:i]内所有值满足<p
    3. 数组指针j，用于遍历
    :param num_list:
    :param start:
    :param end:
    :return:
    """
    # 方便实现，先取锚点为最后一个值
    p = end

    i = start
    for j in range(start, end):
        # 遍历过程中遇到比锚点小的值，就往i处交换
        if num_list[j] < num_list[p]:
            num_list[i], num_list[j] = num_list[j], num_list[i]
            i += 1
    
    num_list[i], num_list[p] = num_list[p], num_list[i]
    return i


if __name__ == '__main__':
    a = [1, 4, 7, 1, 5, 5, 3, 85, 34, 75, 23, 75, 2, 0]
    quick_sort(a, 0, len(a)-1)
    print(a)