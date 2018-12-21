#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

permutations_list = []  # 全局变量，用于记录每个输出


def permutations(nums: List, n: int, pick_nums: List):
    """
    从nums选取n个数的全排列

    回溯法，用一个栈记录当前路径信息
    当满足n==0时，说明栈中的数已足够，输出并终止遍历
    :param nums:
    :param n:
    :param pick_nums:
    :return:
    """
    if n == 0:
        permutations_list.append(pick_nums.copy())
        # print(pick_nums)
    else:
        for i in range(len(nums)-len(pick_nums)):
            pick_nums.append(nums[i])
            # 将已选元素放到后面，下层通过已选元素的个数计算遍历范围，范围逐层缩小
            nums[i], nums[len(nums)-len(pick_nums)] = nums[len(nums)-len(pick_nums)], nums[i]
            permutations(nums, n-1, pick_nums)
            nums[i], nums[len(nums)-len(pick_nums)] = nums[len(nums)-len(pick_nums)], nums[i]
            pick_nums.pop()


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    n = 3
    print('--- list ---')
    print(nums)

    print('\n--- pick num ---')
    print(n)

    print('\n--- permutations ---')
    permutations(nums, n, [])
    print(permutations_list)

    print('\n--- size ---')
    print(len(permutations_list))
