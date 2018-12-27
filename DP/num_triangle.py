#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
求解问题：
在上面的数字三角形中寻找一条从顶部到底边的路径，
使得路径上所经过的数字之和最大。路径上的每一步。
每次只能往 左下 或 右下走，求出这个最大和，不必
给出具体路径。


数字三角示例：
        7
      3   3
    8   1   0
  2   7   4   4
4   5   2   6   5
"""


# DP解法，时间O(n2),空间O(n)
def num_triangle(num_list):
    """
    num_list: 二维的list
    """
    n = len(num_list)
    memo = [None] * n

    # 最后一排
    for i in range(n):
        memo[i] = num_list[n-1][i]

    # 只需要从倒数第二排开始计算
    for i in range(n-2, 0, -1):
        for j in range(len(num_list[i])):
            memo[j] = num_list[i][j] + max(memo[j], memo[j+1])
        # print(memo)

    return num_list[0][0] + max(memo[0], memo[1])


# 递归解法
def num_triangle_r(num_list, i=0, j=0):
    n = len(num_list)
    # 递归结束条件，最后一排
    if i == n-1:
        return num_list[i][j]
    return num_list[i][j] + max(num_triangle_r(num_list, i+1, j), num_triangle_r(num_list, i+1, j+1))


if __name__ == '__main__':
    num_list = [[7], [3, 3], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(num_triangle(num_list))
    print(num_triangle_r(num_list))
