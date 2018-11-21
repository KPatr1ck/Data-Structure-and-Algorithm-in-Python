#!/usr/bin/python
# -*- coding: UTF-8 -*-


def cell_num(n, cell_list=[0, 0, 1]):
    """
    1个细胞的生命周期是3小时，1小时分裂一次。求n小时后，容器内有多少细胞？
    :param n: n小时
    :param cell_list: 不同寿命对应的细胞树
    :return:
    """
    assert(n >= 0)

    while n > 0:
        # 存活时间剩1,2,3小时的细胞
        cell_0, cell_1, cell_2 = cell_list
        # 3->2,3
        cell_list[1] += cell_2

        # 2->1,3
        cell_list[1] -= cell_1
        cell_list[2] += cell_1
        cell_list[0] += cell_1

        # 1->0,3
        cell_list[0] -= cell_0
        cell_list[2] += cell_0

        n -= 1

    # print(cell_list)
    return sum(cell_list)


def cell_num_recursive(n, cell_num=1, cell_life=3):
    if n == 0:
        return cell_num

    # 寿命只剩一小时
    if cell_life == 1:
        return cell_num_recursive(n-1, cell_num, 3)
    else:
        # 分裂
        return cell_num_recursive(n-1, cell_num, cell_life-1) + cell_num_recursive(n-1, cell_num, 3)


if __name__ == '__main__':
    print(cell_num(6))
    print(cell_num_recursive(6))
















