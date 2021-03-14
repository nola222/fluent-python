# -*- coding: utf-8 -*-
# Nola

"""
    lambda：匿名函数，第一个参数为函数参数，第二个参数为表达式。如果程序中这个函数只使用一次，那么使用lambda大大简化程序。(lambda :1+1)() 无参数 结果2
    filter：第一个参数一个函数，第二个参数是一个序列，把传入的函数依次作用于每个元素，根据返回值True or False判断是否舍弃该元素。返回一个迭代器
    map：第一个参数是函数，第二个参数是可迭代对象(iterable)，把传入的函数依次作用于序列的每个元素，并把新的iterator返回。
"""


def use_listcomps(strings):
    """
    使用列表推导返回Unicode code
    :param strings:
    :return:
    """
    beyond_ascii = [ord(s) for s in strings if ord(s) > 40]
    return beyond_ascii


def use_filter_and_map(strings):
    """
    使用filter和map组合返回Unicode code
    :param strings:
    :return:
    """
    beyond_ascii = list(filter(lambda s: s > 40, map(ord, strings)))
    return beyond_ascii


if __name__ == '__main__':
    strings = "#$%^&*(@"
    a = map(ord, strings)  # 返回一个iterator
    a1 = list(a)
    print(a1)
    c = filter(lambda b: b > 40, a1)   # 返回一个iterator
    c1 = list(c)
    print(c1)
    print((lambda: c1[0] + c1[1])())
