# -*- coding: utf-8 -*-
# Nola


def slice_assignment(l):
    l[2:5] = [20, 30]  # 切片赋值
    print(l)
    del l[5:7]  # 切除
    print(l)
    l[3::2] = [11, 12]
    print(l)
    l[2:5] = [100]  # 赋值只能是iterable 不能写100
    return l


if __name__ == '__main__':
    l = list(range(10))
    l = slice_assignment(l)
    print(l)
