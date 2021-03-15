# -*- coding: utf-8 -*-
# Nola

"""
    用bisect来搜索：
        bisect(haystack, needle)在haystack里搜索needle针的位置，该位置满足的条件时，把needle插入这个位置之后，haystack还能保持升序。
        即在这个函数返回的位置前面的值都小于或等于needle的值。haystack必须时有序的序列。
        bisect查找位置的index，再用haystack.insert(index, needle)来插入新值。
"""

import bisect
import sys

HAYSTACK = [1, 5, 6, 8, 12, 45, 16, 65, 89, 53, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}      {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 用bisect函数计算元素应该出现的位置
        offset = position * '    |'  # 利用该位置来算出需要几个分隔符号
        print(ROW_FMT.format(needle, position, offset))  # 把元素和其他应该出现的位置打印出来


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


if __name__ == '__main__':
    if sys.argv[-1] == 'left':
        bisect_fn = bisect.bisect_left
    else:
        bisect_fn = bisect.bisect

    print('DEMO:', bisect_fn.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect_fn)

    # 根据一个分数，找到它对应的成绩
    l = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(l)
