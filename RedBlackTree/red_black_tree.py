#!/usr/bin/python
# -*- coding: UTF-8 -*-

from queue import Queue
import pygraphviz as pgv
import random

OUTPUT_PATH = 'E:/'


class TreeNode:
    def __init__(self, val=None, color=None):
        self.val = val
        assert color in ['r', 'b']
        self.color = 'red' if color == 'r' else 'black'

        self.left = None
        self.right = None
        self.parent = None

    def is_black(self):
        return self.color == 'black'

    def switch_color(self):
        self.color = 'red' if self.color == 'black' else 'black'
        return


class RedBlackTree:
    """
    红黑树实现
    """
    def __init__(self, val_list=None):
        self.root = None
        self.black_leaf = TreeNode(color='b')  # 共用的黑色叶子节点

        # 测试用
        if type(val_list) is list:
            for n in val_list:
                assert type(n) is int
                self.insert(n)

    def search(self, val):
        if self.root is None:
            return None

        n = self.root
        while n:
            if val < n.val:
                n = n.left
            elif val > n.val:
                n = n.right
            else:
                return n
        return None

    def insert(self, val):
        """
        插入
        :param val:
        :return:
        """
        assert type(val) is int

        new_node = TreeNode(val, 'r')  # 新插入的节点为红色

        # 根节点
        if self.root is None:
            self.root = new_node
        else:
            n = self.root
            while n != self.black_leaf:  # 黑色叶子节点
                p = n
                if val < n.val:
                    n = n.left
                elif val > n.val:
                    n = n.right
                else:
                    raise KeyError('val:{} already exists')  # 该值已存在，插入失败

            if val < p.val:
                p.left = new_node
            else:
                p.right = new_node
            new_node.parent = p

        new_node.left = new_node.right = self.black_leaf
        # 插入后调整
        self._adjust_after_insert(new_node)

    def _adjust_after_insert(self, node):
        """
        插入后的节点调整
        调整的情况如下：
        0. 两种特殊情况：n为根节点时，直接将颜色置黑；父节点p为黑色时，不需要额外调整
        1. 调整节点的父节点p是红色的，叔节点u也是红色
        2. 调整节点的父节点p是红色的，叔节点u是黑色，父节点p和调整节点n不在同一方向
        3. 调整节点的父节点p是红色的，叔节点u是黑色，父节点p和调整节点n在同一方向
        :param node:
        :return:
        """
        # 父p 叔u 祖父g
        p = self.parent(node)
        u = self.bro(p)
        g = self.parent(p)

        # case 0: 调整节点为根节点
        if node == self.root:
            self.root.color = 'black'
            return

        # case 0: 调整节点的父节点p是黑色的
        if p.is_black():
            return

        # case 1: 调整节点的父节点p是红色的，叔叔节点u也是红色
        if not u.is_black():
            p.switch_color()
            u.switch_color()
            g.switch_color()  # p和u是红色，g一定是黑色的
            self._adjust_after_insert(g)
            return

        # 调整节点的父节点p是红色的，叔叔节点u是黑色
        # 注意父节点左右子树需要分别处理，具有对称性
        # case2:
        if u.is_black():
            # 父节点是左子树
            if p == g.left and p.right == node:
                self.rotate_l(p)
                self._adjust_after_insert(p)
                return

            # 父节点是右子树
            if p == g.right and p.left == node:
                self.rotate_r(p)
                self._adjust_after_insert(p)
                return

        # case 3:
        if u.is_black():
            # 父节点是左子树
            if p == g.left and p.left == node:
                self.rotate_r(g)
                p.switch_color()
                g.switch_color()
                return

            # 父节点是右子树
            if p == g.right and p.right == node:
                self.rotate_l(g)
                p.switch_color()
                g.switch_color()
                return

    def rotate_l(self, node):
        if node is None:
            return

        if node.right is self.black_leaf:
            return
            # raise Exception('try rotate left , but the node "{}" has no right child'.format(node.val))

        p = self.parent(node)
        x = node
        y = node.right

        # node为根节点时，p为None，旋转后要更新根节点指向
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.left != self.black_leaf:
            y.left.parent = x

        x.right, y.left = y.left, x

    def rotate_r(self, node):
        if node is None:
            return

        if node.left is self.black_leaf:
            return
            # raise Exception('try rotate left , but the node "{}" has no left child'.format(node.val))

        p = self.parent(node)
        x = node
        y = node.left

        # 同左旋
        if p is not None:
            if x == p.left:
                p.left = y
            else:
                p.right = y
        else:
            self.root = y

        x.parent, y.parent = y, p

        if y.right is not None:
            y.right.parent = x

        x.left, y.right = y.right, x

    @staticmethod
    def bro(node):
        if node is None or node.parent is None:
            return None
        else:
            p = node.parent
            if node == p.left:
                return p.right
            else:
                return p.left

    @staticmethod
    def parent(node):
        if node is None:
            return None
        else:
            return node.parent

    def draw_img(self, img_name='Red_Black_Tree.png'):
        """
        画出树图
        :param img_name:
        :return:
        """
        tree = pgv.AGraph(directed=True, strict=True)

        q = Queue()
        q.put(self.root)

        while not q.empty():
            n = q.get()
            if n != self.black_leaf:  # 黑色叶子的连线由各个节点自己画
                tree.add_node(n.val, color=n.color)
                # ----- TEST
                # if n.parent is not None:
                    # print('child {} parent {}'.format(str(n.val), str(n.parent.val)))
                    # tree.add_edge(n.val, n.parent.val)
                # ------
                for c in [n.left, n.right]:
                    q.put(c)
                    color = 'red' if c == n.left else 'black'
                    if c != self.black_leaf:
                        tree.add_edge(n.val, c.val, color=color)
                    else:
                        tree.add_edge(n.val, 'None', color=color)

        tree.graph_attr['epsilon'] = '0.01'
        tree.layout('dot')
        tree.draw(OUTPUT_PATH + img_name)
        return True


if __name__ == '__main__':
    # nums = [5, 3, 6, 7, 8]
    # nums = list(range(1, 6))
    nums = []
    while len(nums) < 50:
        n = random.randint(1, 200)
        if n in nums:
            continue
        nums.append(n)

    rbt = RedBlackTree(nums)
    rbt.draw_img('rbt.png')

