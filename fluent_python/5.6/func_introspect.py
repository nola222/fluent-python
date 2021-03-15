# -*- coding: utf-8 -*-
# Nola
"""
    函数内省：
     把函数视作对象，把函数赋予属性
"""
from functools import partial


def factorial(n):
    """
    求n的阶乘
    :param n: 要求阶乘的数
    :return: int 阶乘之后的结果
    """
    return 1 if n < 2 else n * factorial(n - 1)


print(dir(factorial))
print('{:-^100}'.format('-'))
# print(dir(builtins))
print(partial.__doc__)

print('{:-^100}'.format('-'))
print("列出常规对象没有而函数有的属性")


class C: pass


obj = C()


def func(): pass


print(sorted(set(dir(func)) - set(dir(obj))))  # 计算差集 排序 得到类的实例没有而函数有的属性列表
