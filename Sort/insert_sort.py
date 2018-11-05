#!/usr/bin/python
# -*- coding: UTF-8 -*-


def insert_sort(num_list):
    """
    插入排序
    :param num_list:
    :return:
    """
    n = len(num_list)

    for i in range(n-1):
        # 从后往前比较
        value = num_list[i+1]
        for j in range(i, -1, -1):
            if num_list[j] > value:
                num_list[j+1] = num_list[j]
                # 可能是python的一个坑
                if j == 0:
                    j -= 1
            else:
                break

        num_list[j+1] = value

    return num_list


if __name__ == '__main__':
    print(insert_sort([1, 3, 4, 5, 2]))
    print(insert_sort([1, 2, 3, 4, 5]))
    print(insert_sort([5, 4, 3, 2, 1]))

