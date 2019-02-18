#!/usr/bin/python
# -*- coding: UTF-8 -*-

from typing import List


def fibonacci(n: int) -> int:
    """
    f(n) = f(n-1) + f(n-2)
    :param n:
    :return:
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


class Permutation:
    def __init__(self, l: List[int]) -> None:
        self.data = l
        self.perm_res: List[List[int]] = []
        self.picks: List[int] = [None for i in range(len(self.data))]

    def generate(self) -> List[List[int]]:
        self._generate(0)
        return self.perm_res

    def _generate(self, count) -> None:
        if count >= len(self.data):
            self.perm_res.append(self.picks.copy())
        else:
            for i in range(len(self.data)-count):
                self.picks[count] = self.data[i]

                self.data[i], self.data[len(self.data)-1-count] = self.data[len(self.data)-1-count], self.data[i]
                self._generate(count+1)
                self.data[i], self.data[len(self.data)-1-count] = self.data[len(self.data)-1-count], self.data[i]


perm_res: List[List[int]] = []
picks: List[int] = []
def permutation(l: List[int], count=0) -> None:
    if count >= len(l):
        perm_res.append(picks.copy())
    else:
        for i in range(len(l)-count):
            # pick one
            picks.append(l[i])
            # swap
            l[i], l[len(l)-1-count] = l[len(l)-1-count], l[i]
            permutation(l, count+1)
            l[i], l[len(l)-1-count] = l[len(l)-1-count], l[i]
            # recovery
            picks.pop()


if __name__ == '__main__':
    print('-'*30)
    print('fibonacci: ')
    for i in range(1, 5):
        print(fibonacci(i))
    print()

    print('-'*30)
    print('factorial: ')
    for i in range(1, 5):
        print(factorial(i))
    print()

    print('-'*30)
    print('permutation: ')
    p_list = [1, 2, 3]
    p = Permutation(p_list)
    print(p.generate())
    # permutation(p_list)
    # print(len(perm_res))
    # print(perm_res)
    print()
