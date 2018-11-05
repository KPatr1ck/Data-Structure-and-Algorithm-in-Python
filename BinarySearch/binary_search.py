#!/usr/bin/python
# -*- coding: UTF-8 -*-


def binary_search_recursive(source, start, end, element):
    """
    二分查找，递归
    :param source: 源
    :param start: 起点
    :param end: 终点
    :param element: 查找的元素
    :return: 返回元素在源的索引值，若搜不到则返回-1
    """
    if start > end:
        return -1

    mid = (start + end)//2
    if source[mid] == element:
        return mid
    elif source[mid] > element:
        return binary_search_recursive(source, start, mid-1, element)
    else:
        return binary_search_recursive(source, mid+1, end, element)


def binary_search(source, element):
    """
    二分查找，非递归
    :param source:
    :param element:
    :return:
    """
    start = 0
    end = len(source) - 1

    while start <= end:
        mid = (start + end)//2
        if source[mid] == element:
            return mid
        elif source[mid] > element:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def binary_search_ll(source, element):
    """
    二分查找变体
    找到最后一个小于等于element的数(last less)
    :param source:
    :param element:
    :return:
    """
    start = 0
    end = len(source) - 1

    while start <= end:
        mid = (start + end)//2
        if source[mid] > element:
            end = mid - 1
        else:
            if mid == len(source)-1 or source[mid+1] > element:
                return mid
            else:
                start = mid + 1

    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    se = 3
    print(binary_search(a, se))
    print(binary_search_recursive(a, 0, len(a)-1, se))
