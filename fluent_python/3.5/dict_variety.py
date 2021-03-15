# -*- coding: utf-8 -*-
# Nola

"""
    - collections.OrderedDict:这个类型在添加键的时候会保持顺序，因此键的迭代次序总是一致的。
        OrderedDict的popitem方法默认删除并返回的字典里最后一个元素。
        my_odict.popitem(last=False)这样调用，删除并返回第一个被添加的元素。
    - collections.ChainMap:这个类型可以容纳数个不同的映射对象，进行键查找操作时，这些对象会被当作一个整体被逐个查找，直到找到为止。
    - collections.Counter:这个映射类型会给键准备一个整数计数器，每次更新一个键时都会增加这个计数器，这个类型可以给可散列表对象计数。
        most_common([n])会按照次序返回映射里最常见的n个键和它们的计数
    - collections.UserDict:这个类是把标准dict用纯Python实现了一遍，用来给用户继承写子类的。
"""
import builtins
import collections

pylookup = collections.ChainMap(locals(), globals(), vars(builtins))  # python变量查询规则

ct = collections.Counter('asbdfkhrsdgbfbg')
print(ct)
ct.update('aaaaaaayihbb')
print(ct)
print(ct.most_common(2))
