#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Tuple, List
from queue import Queue


class Node:
    def __init__(self, idx_range: Tuple, val: int) -> None:
        self.range = idx_range
        self.val = val
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums: List) -> None:
        self.root = self.build_segment_tree(nums, (0, len(nums)-1))

    def build_segment_tree(self, nums: List, idx_range: Tuple) -> Node:
        """
        构建线段树：
        1. 一分为二，分别创建左右子节点
        2. 左右子节点取最大值为当前节点的值
        3. 递归
        :param nums:
        :param nums:
        :param idx_range:
        :return:
        """
        n = Node(idx_range, 0)
        start, end = idx_range

        if start == end:    # 叶节点
            n.val = nums[start]
        else:
            mid = (start + end)//2
            # 创建左右子节点lc, rc
            lc = self.build_segment_tree(nums, (start, mid))
            rc = self.build_segment_tree(nums, (mid+1, end))
            n.val = max(lc.val, rc.val)
            n.left, n.right = lc, rc

        return n

    def update(self, i: int, val: int):
        self._update(self.root, i, val)

    def _update(self, n: Node, i: int, val: int) -> int:
        """
        更新节点:
        1. 从根节点开始递归，直到找到叶子节点，将新值赋给叶子节点
        2. 从当前叶节点的父节点开始，递归向上更新节点值
        :param i:
        :param val:
        :return:
        """
        start, end = n.range

        if start == end == i:
            n.val = val
        else:
            mid = (start + end)//2
            if i <= mid:
                n.val = max(self._update(n.left, i, val), n.right.val)
            else:
                n.val = max(n.left.val, self._update(n.right, i, val))

        return n.val

    def range_get(self, find_range: Tuple) -> int:
        return self._range_get(self.root, find_range)

    def _range_get(self, n: Node, find_range: Tuple) -> int:
        """
        数据范围的操作:
        1. 如果寻找的范围和当前节点的范围一致，直接返回当前节点的值
        2. 如果不一致，先计算mid，然后根据f_start, mid和f_end的关系，三种情况处理
        :param n:
        :param find_range:
        :return:
        """
        # print('[Source Node]', n.range, n.val)
        # print('[Find Range ]', find_range)
        if n.range == find_range:
            return n.val

        start, end = n.range
        f_start, f_end = find_range
        mid = (start + end)//2

        if f_end <= mid:        # <<
            return self._range_get(n.left, find_range)
        elif f_start <= mid:    # <>
            return max(self._range_get(n.left, (f_start, mid)), self._range_get(n.right, (mid+1, end)))
        else:                   # >>
            return self._range_get(n.right, find_range)

    def print_tree(self):
        """
        bfs打印
        :return:
        """
        q = Queue()
        q.put(self.root)

        while not q.empty():
            n = q.get()
            if n is not None:
                print(n.range, n.val)
                q.put(n.left)
                q.put(n.right)

    def __repr__(self):
        return print(self.print_tree())


if __name__ == '__main__':
    nums = [2, 5, 6, 9, 3]
    print('Nums Idx   : {}'.format(list(range(len(nums)))))
    print('Origin Nums: {}'.format(nums))
    st = SegmentTree(nums)
    # st.print_tree()

    # print('-' * 20)
    # st.update(1, 5)
    # st.print_tree()
    #
    # print('-' * 20)
    # st.update(1, 1)
    # st.print_tree()

    print('-' * 20)
    idx_range = (0, 3)
    print('The max of {} is {}.'.format(idx_range, st.range_get(idx_range)))
