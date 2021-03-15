# -*- coding: utf-8 -*-
# Nola
"""
    高阶函数：
        接受函数为参数，或者把函数作为结果返回的函数是高阶函数higher-order function 如map,sorted可选参数key提供一个函数
"""
# from __future__ import absolute_import
import os
import sys

from .func_as_object import fact, factorial

print(os.path.dirname(__file__))  # 获取父目录

sys.path.append('.')
sys.path.append('..')

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=len))


def reverse_word(word):
    return word[::-1]


print(reverse_word('testing'))
print(sorted(fruits, key=reverse_word))

"""
    在函数式编程范式中，最为人熟知的高阶函数有map、filter、reduce和apply（在python3中移除）
    python3中引入列表推导和生成器表达式，它们变得没那么重要了
"""
print('计算阶乘，map和filter与列表推导式比较')
l = list(map(fact, range(6)))
print(l)

x = [fact(n) for n in range(6)]
print(x)

m = list(map(factorial, filter(lambda n: n % 2, range(6))))
print(m)

v = [factorial(n) for n in range(6) if n % 2]
print(v)
