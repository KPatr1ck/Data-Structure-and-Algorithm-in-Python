#!/usr/bin/python
# -*- coding: UTF-8 -*-


def cell_num(n):
    """
    1个细胞的生命周期是3小时，1小时分裂一次。求n小时后，容器内有多少细胞？
    :param n: n小时
    :param cell_list: 不同寿命对应的细胞树
    :return:
    """
    assert(n >= 0)

    cell_list = [0, 0, 1]
    while n > 0:
        # 存活时间剩1,2,3小时的细胞
        cell_0, cell_1, cell_2 = cell_list[:]
        # 3->2,3
        cell_list[1] += cell_2

        # 2->1,3
        cell_list[1] -= cell_1
        cell_list[0] += cell_1
        cell_list[2] += cell_1

        # 1->0,3
        cell_list[0] -= cell_0
        cell_list[2] += cell_0

        n -= 1

    return sum(cell_list)


def cell_num_recursive(n):
    """
    递归解法
    f(n) = 2*f(n-1) - f(n-4)
    第n时刻的细胞数目，等于 *** n-1时刻的细胞数*2 - 在n时刻恰好死的数目(n-1存活，n死) ***
    :param n:
    :return:
    """
    base_res = {0: 1, 1: 2, 2: 4, 3: 7}
    if n in base_res:
        return base_res[n]

    return 2*cell_num_recursive(n-1) - cell_num_recursive(n-4)


if __name__ == '__main__':
    n = 25
    for n in range(1, 10):
        print('cell_num: {}'.format(cell_num(n)))
        print('cell_num_recursive: {}'.format(cell_num_recursive(n)))
        print('-'*20)
















