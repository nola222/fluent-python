# -*- coding: utf-8 -*-
# Nola

"""
    不可变映射类型：
        标准库里的所有映射都是可变的。从Pyhton3.3开始，types模块引入一个封装类MappingProxyType，给这个类一个映射，返回一个只读的映射视图。
        虽然是只读视图，但是是动态的。对原映射做出的改动，可以通过这个视图可以观察到，无法通过这个视图对原映射做出修改。
"""

from types import MappingProxyType

d = {1: 'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])  # 可以通过d-proxy看到

# d_proxy[2] = 'B'  # mappingproxy不支持赋值操作 通过d_proxy不能做任何修改
d[2] = 'B'
print(d_proxy)  # d_
# proxy是动态的 对d做的任何改动都会反馈到它上面
print(d_proxy[2])
print(d)

