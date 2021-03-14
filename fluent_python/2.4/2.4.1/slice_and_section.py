# -*- coding: utf-8 -*-
# Nola

"""
    - 当只有最后一个位置信息时，可以看出切片和区间里面由几个元素
    - 当起始位置信息都可见时，可以快速计算出切片和区间的长度。(start - stop)
    - 利用任意下标把序列分割成不重叠的两部分
"""


def use_slice(l):
    slice2 = l[:2]  # 在下标2的地方分割
    slice3 = l[2:]
    return slice2, slice3


if __name__ == '__main__':
    l = [20, 30, 40, 50, 60, 70]
    s1, s2 = use_slice(l)
    print(s1)
    print(s2)
