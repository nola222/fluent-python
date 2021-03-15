# -*- coding: utf-8 -*-
# Nola
"""
    集合的操作
        a、b、c、d四个聚合类型的合集，a必须是集合，其他几个为任何类型的可迭代对象
"""
a = {1, 2}
b = [3, 4]
c = ['5', '6']
d = [7, 8, (9, 10)]
print(a.union(b, c, d))
a.discard(2)  # 传入元素在集合中存在的话删除
a.discard(2)  # 与remove不同的是删除的元素不在set中 不会抛出KeyError的异常
print(a)
