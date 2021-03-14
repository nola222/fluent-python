# -*- coding: utf-8 -*-
# Nola

"""
    +和*都遵循这个规律：
        不修改原有的操作对象
        构建一个全新的序列
"""


def plus_mul(l, s):
    l1 = l * 5
    s1 = 5 * s
    return l1, s1


def build_list_by_list(l):
    board = [l * 3 for i in range(3)]
    print(board)
    board[1][2] = 'X'
    return board


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    s = "abcd"
    l1, s1 = plus_mul(l, s)
    print(l1)
    print(s1)
    print("{:-<30}".format("-"))
    l = ["_"]
    board = build_list_by_list(l)
    print(board)