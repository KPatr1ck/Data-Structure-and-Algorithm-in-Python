#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bf_rk import *
from time import time


def fsm(main, pattern):
    """
    有限状态机匹配：
    1. 根据pattern的长度，定义m+1个状态
    2. 用指针i遍历main的字符，用s记录当前的匹配状态
    3. 根据i和s，更新状态
    :param main:
    :param pattern:
    :return:
    """
    assert type(main) is str and type(pattern) is str
    n, m = len(main), len(pattern)

    if m == 0:
        return 0

    if n <= m:
        return 0 if main == pattern else -1

    # state init
    s = 0
    state_map = init_state(pattern, m)

    for i in range(n):
        s = update_state(main[i], s, state_map)
        if s == m:
            return i-m+1
    return -1


def init_state(pattern, m):
    """
    根据pattern初始化state_map
    state_map的长度是m+1，状态从0-m

    示例：
    pattern = 'abc'
    state_map = ['', 'a', 'ab', 'abc']
    :param pattern:
    :return:
    """
    # state from 0 - m
    state_map = [None] * (m+1)
    for i in range(len(state_map)):
        state_map[i] = pattern[:i]
    # print('state_map for pattern: {}'.format(state_map))
    return state_map


def update_state(c, cur_state, state_map):
    """
    根据cur_state和输入c，计算最新的状态并返回
    0是初始状态，m是匹配完成状态，主串中的字符是输入，状态根据输入跳转

    跳转的情况如下：
    1. state_map[cur_state] + c == state_map[cur_state] + 1，则状态加1
    2. 1不成立，从state_map[cur_state][1:] + c中，寻找可以返回之前状态的最长
       的后缀子串，如果找到，则返回对应状态
    3. 2中找不到任何后缀子串，回到状态0
    :param c:
    :param cur_state:
    :param state_map:
    :return:
    """
    if c == state_map[cur_state+1][-1]:     # match one char, so update s to s+1
        return cur_state+1
    else:
        new_str = state_map[cur_state][1:] + c  # not match, try to find new s
        length = len(new_str)                   # or length = cur_state

        # find the max sub suffix from the state map
        for i in range(length):
            if new_str[i:] == state_map[length-i]:
                return length-i
        return 0


if __name__ == '__main__':
    m_str = 'a' * 10000
    p_str = 'a' * 200 + 'b'

    print('--- time consume ---')
    t = time()
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time() - t))

    t = time()
    print('[fsm] result:', fsm(m_str, p_str))
    print('[fsm] time cost: {0:.5}s'.format(time() - t))

    m_str = 'abcdcccdc'
    p_str = 'cccd'
    print('')
    print('--- search ---')
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[fsm] result:', fsm(m_str, p_str))