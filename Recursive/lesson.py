#!/usr/bin/python
# -*- coding: UTF-8 -*-

import types

"""
递归三要素：
1. 可分解为有限个子问题
2. 子问题的求解方式与原问题完全相同
3. 存在终止条件
"""


# n阶台阶走法问题
def stair(n: int) -> int:
    if n == 2:
        return 2
    if n == 1:
        return 1

    if n < 1:
        raise Exception('n={} is illegal'.format(n))

    return stair(n-2) + stair(n-1)


# 递归优化
memo_op = {1: 1, 2: 2}
def stair_op(n: int) -> int:
    global memo_op    
    if n < 1:
        raise Exception('n={} is illegal'.format(n))

    if n in memo_op:
        return memo_op[n]

    memo_op[n] = stair_op(n-2) + stair_op(n-1)
    return memo_op[n]


# DP
def stair_dp(n: int) -> int:

    if n < 1:
        raise Exception('n={} is illegal'.format(n))

    if n == 2:
        return 2
    if n == 1:
        return 1
    
    memo = [None] * (n+1)
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
    

# 普通递归，有爆栈风险
def f(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return n + f(n-1)


# 尾递归优化
def fy(n: int, res=0):
    if n == 0:
        yield 0
    if n == 1:
        yield 1 + res

    yield fy(n-1, n + res) 


# 用生成器优化尾递归
def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)
    while isinstance(g, types.GeneratorType):
        g = next(g)
    return g


if __name__ == '__main__':
    # print(f(10))
    # print(tramp(fy, 10))
    # print(tramp(fy, 999))
    print(stair_op(40))
    print(stair_dp(40))
