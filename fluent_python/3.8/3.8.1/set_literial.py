# -*- coding: utf-8 -*-
# Nola
"""
    集合字面量：
        像{1, 2, 3}这样的字面量，Pyhton会用一个专门的叫做BUILD_SET的字节码来创建集合
"""
from dis import dis

s = {1}
print(type(s))
print(s)
print(s.pop())
print(s, '\n' * 3)

# 使用dis.dis反汇编函数查看字节码
print(dis('{1}'))  # 检查{1}字面量背后的字节码
print('-' * 30)
print(dis('set[1]'))  # set[1]的字节码

"""
    Pyhton里没有针对frozenset的特殊字面量句法，只能采用构造方法
"""
print(frozenset(range(10)))
