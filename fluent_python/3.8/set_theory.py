# -*- coding: utf-8 -*-
# Nola

"""
    集合论：
        集概念在Python中算比较年轻的，使用概率也比较低。set和它的姊妹不可变类型frozenset直到Python2.3才首次以模块的形式出现，后在Python2.6
        升级为内置类型。
        中缀运算符：集合a,b
            并集：a | b
            交集：a & b
            差集：a - b

"""

l = ['span', 'div', 'span', 'div']  # 集合元素必须是可散列的，set类型本身是不可散列的，但是frozenset可以
print(set(l))  # 去重
print(list(set(l)))
haystack = {'123@qq.com', '456@qq.com', '789@qq.com'}
needles = {'456@qq.com', '201@qq.com', '789@qq.com'}

# 使用set求相同元素出现的次数

# 方法一
print(len(haystack & needles))

# 方法二
found = 0
for n in needles:
    if n in haystack:
        found += 1
print(found)

# 方法三
x = [c for c in needles if c in haystack]
print(len(x), x)

# 任何可迭代对象
haystack = ['123@qq.com', '456@qq.com', '789@qq.com']
needles = ['456@qq.com', '201@qq.com', '789@qq.com']
# 方法一
found = len(set(needles) & set(haystack))
print(found)

# 方法二
found = len(set(needles).intersection(haystack))  # intersection返回两个集合的交集
print(found)
