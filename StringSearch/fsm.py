#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bf_rk import *
from time import time


def fsm(main, pattern):
    """
    有限状态机匹配：
    1. 根据pattern的长度，定义m+1个状态
    2. 根据main, pattern建立状态转移表，大小为 m * len(set(main))
    3. 遍历main的字符，s记录当前的匹配状态
    4. 根据字符c和状态s，更新状态(s也表示当前已匹配的长度)
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
    # state also stands for how many characters have been matched
    s = 0
    state_switch_map = init_state(main, pattern, m)

    for i, c in enumerate(main):
        s = update_state(c, s, state_switch_map)
        if s == m:  # match all characters
            return i-m+1
    return -1


def update_state(c, cur_state, state_switch_map):
    """
    根据当前状态cur_state和当前字符c，查表返回下一状态
    :param c:
    :param cur_state:
    :param state_switch_map:
    :return:
    """
    return state_switch_map[cur_state][ord(c)]


def init_state(main, pattern, m):
    """
    根据main, pattern生成状态转移表state_switch_map
    步骤：
    1. 建立状态表state_map，目的是在建立转移表时，用后缀子串查哈希表，减少字符对比消耗
    2. 初始化状态转移表state_switch_map，大小为 m * len(set(main))
    *3. 给整张state_switch_map赋值，从状态0~m-1，对于每一个遇到的字符char，赋值新状态
        state_switch_map[cur_state][char] = new_state
    *4. 新状态new_state的赋值方法：当前状态cur_state表示在当前已经匹配了cur_state个字
        符，对于新增的字符char，先让tmp = pattern[:cur_state] + char，然后从长到短遍
        历所有后缀子串，如果有后缀子串suffix在state_map中出现，new_state则等于suffix
        所对应的状态state_map[suffix]，如果遍历完了都不存在这个suffix，则新状态是0
    :param main:
    :param pattern:
    :param m:
    :return:
    """
    char_set = set(main)
    # state_map: {'a': 1, 'ab': 2, 'abc': 3} (pattern = 'abc')
    state_map = {}
    for i in range(1, m+1):
        state_map[pattern[:i]] = i

    # state_switch_map: [{}, {}, ...]
    state_switch_map = [None] * m
    for i in range(m):
        state_switch_map[i] = {}
        for c in char_set:
            state_switch_map[i][ord(c)] = 0

    # build state_switch_map
    for i in range(m):
        matched = pattern[:i]
        for c in char_set:
            tmp = matched + c
            for j in range(len(tmp)):
                suffix = tmp[j:]
                if suffix in state_map:
                    state_switch_map[i][ord(c)] = state_map[suffix]
                    break
    # print(state_switch_map)
    return state_switch_map


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

    m_str = 'abc../3 55dcccdc'
    p_str = 'cccd'
    print('')
    print('--- search ---')
    print('[Built-in Functions] result:', m_str.find(p_str))
    print('[fsm] result:', fsm(m_str, p_str))