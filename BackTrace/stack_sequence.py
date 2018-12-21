#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List

stack_sequence_list = []


def stack_sequence(nums: List, cur_stack: List, pop_nums: List):
    """
    输出nums所有的出栈序列

    回溯法，用一个栈记录当前已经出栈了的数字
    注意和排列组合不同，栈序列分别对当前栈和记录出栈数字的栈都进行回溯
    两个栈的大小之和代表当前处理过的数字个数，用于缩小范围
    :param nums:
    :param cur_idx:
    :param cur_stack:
    :param pop_nums:
    :return:
    """
    if len(pop_nums) == len(nums):
        stack_sequence_list.append(pop_nums.copy())
        # print(pop_nums)
    else:
        if len(cur_stack) + len(pop_nums) < len(nums):
            cur_stack.append(nums[len(cur_stack) + len(pop_nums)])
            stack_sequence(nums, cur_stack, pop_nums)
            cur_stack.pop()

        if len(cur_stack) > 0:
            pop_num = cur_stack.pop()
            pop_nums.append(pop_num)
            stack_sequence(nums, cur_stack, pop_nums)
            pop_nums.pop()
            cur_stack.append(pop_num)


if __name__ == '__main__':
    nums = [1, 2, 3,]

    print('--- list ---')
    print(nums)

    print('\n--- stack sequence ---')
    stack_sequence(nums, [], [])
    print(stack_sequence_list)

    print('\n--- size ---')
    print(len(stack_sequence_list))
