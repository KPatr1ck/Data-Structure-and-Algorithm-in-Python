#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

combinations_list = []  # 全局变量，用于记录每个输出


def combinations(nums: List, n: int, start: int, pick_nums: List):
    """
    从nums选取n个数组合

    回溯法，用一个栈记录当前路径信息
    当满足n==0时，说明栈中的数已足够，输出并终止遍历
    :param nums:
    :param n:
    :param start:
    :param pick_nums:
    :return:
    """
    if n == 0:
        combinations_list.append(pick_nums.copy())
        # print(pick_nums)
    else:
        for i in range(start, len(nums)-n+1):
            # 范围从左滑到右，模拟人为穷举法
            pick_nums.append(nums[i])
            combinations(nums, n-1, i+1, pick_nums)
            pick_nums.pop()


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    n = 2
    print('--- list ---')
    print(nums)

    print('\n--- pick num ---')
    print(n)

    print('\n--- combinations ---')
    combinations(nums, n, 0, [])
    print(combinations_list)

    print('\n--- size ---')
    print(len(combinations_list))
