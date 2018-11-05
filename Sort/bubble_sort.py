#!/usr/bin/python
# -*- coding: UTF-8 -*-


def bubble_sort(num_list):
    """
    冒泡排序
    :param num_list:
    :return:
    """
    n = len(num_list)

    for i in range(n-1):
        # 如果有一次没有数据交换，则排序已完成
        swap_flag = False
        for j in range(n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                swap_flag = True
        if not swap_flag :
            break

    return num_list


if __name__ == '__main__':
    print(bubble_sort([1, 3, 4, 5, 2]))
    print(bubble_sort([1, 2, 3, 4, 5]))
    print(bubble_sort([5, 4, 3, 2, 1]))
