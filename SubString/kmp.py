#!/usr/bin/python
# -*- coding: UTF-8 -*-


def kmp(main, pattern):
    """
    kmp搜索算法

    注意：
    1. 这个算法没有严格参考书上的写，是根据自己的思路翻译,
    仅供理解kmp算法思想作为参考。
    2. 在循环那里对j==0做了特殊处理，防止i和j的指针都不走。
    这样是因为首字符不匹配的话，必须去main中取下一个字符了。
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

    # generate next list
    next = generate_next(pattern)

    i, j = 0, 0
    while i < n and j < m:
        if main[i] == pattern[j]:
            if j == m-1:
                # print(i, j, m)
                return i-m+1
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = next[j]
    return -1


def generate_next(pattern):
    """
    根据pattern创建next数组

    注意：
    kmp原理与fsm在本质上是一样的，都是切换状态
    不同点在于，fsm *考虑上当前从main中读入的字符*，从长到短截取后缀子串，
    去pattern中找是否存在前缀子串与其匹配(也就是去找能不能回到之前的状
    态)；
    而kmp，是在当前字符不匹配时，*不考虑当前的字符*，而是在之前的匹配中，从
    长到短截取后缀子串，去pattern中找是否存在前缀子串与其匹配，然后将 *匹配
    字符* 对齐，继续进行比较。
    :param pattern:
    :return:
    """
    m = len(pattern)

    # all valid prefix
    prefix_map = {}
    for i in range(1, m):
        prefix_map[pattern[:i]] = i

    # next list
    next = [0] * m

    # next[i] 表示pattern[0:i]中，存在前缀子串和后缀子串相匹配的最长的长度
    for i in range(m):
        for j in range(1, i):
            if pattern[j:i] in prefix_map:
                next[i] = prefix_map[pattern[j:i]]
                break

    return next


if __name__ == '__main__':
    m_str = 'abc../3 55dcccdc'
    p_str = 'cccd'
    print(m_str.find(p_str))
    print(kmp(m_str, p_str))
