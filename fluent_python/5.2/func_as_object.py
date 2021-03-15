# -*- coding: utf-8 -*-
# Nola
"""
    把函数视作对象
"""


def factorial(n):
    """return n!"""
    return 1 if n < 2 else n * factorial(n - 1)


print(factorial(1))
print(factorial(3))
print(factorial(5))
print(factorial.__doc__)  # 生成对象的帮助文本
# print(help(factorial))  # 输出__doc__属性
print(type(factorial))
print('{:-^30}'.format('======='))
# 通过别名使用函数 再把函数作为参数传递
fact = factorial
print(fact)
print(fact(4))
map_obj = map(factorial, range(10))
print(map_obj)
print(list(map_obj))
print(list(map(fact, range(10))))
