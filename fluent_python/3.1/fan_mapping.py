# -*- coding: utf-8 -*-
# Nola
from collections import abc

"""
    可散列的数据类型:
        如果一个对象是可散列的,在这个对象的生命周期中,它的散列值是不变的,而且这个对象需要实现__hash__()方法,__qe__()方法.
        如果两个可散列对象是相等的,那么它们的散列值一定是一样的.
"""

my_dict = {}
print(isinstance(my_dict, abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))

t1 = (1, 2, [30, 40])  # 元组只有当一个元组包含所有元素都是可散列类型的情况下，才是可散列的。
# print(hash(t1))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

"""
    原子不可变数据类型(str、bytes和数值类型)都是可散列类型，frozenset(生成不可变集合，冻结的集合)也是可散列的，其可容纳可散列类型
    Python里所有不可变类型都是可散列的，这个说法不准确
"""
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a, '\n', b, '\n', c, '\n', d, '\n', e)
print(a == b == c == d == e)
