# -*- coding: utf-8 -*-
# Nola

"""
    需要一个只包含数字的列表，array.array比list更高效
    数组支持所有跟可变序列有关的操作.pop、.insert、.extend，数组还支持从文件读取和存入文件的方法，.frombytes和.tofile
"""

from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))  # 利用一个可迭代对象来建立一个双精度浮点数组(类型码是d)，这里可迭代对象是一个生成器表达式
print(floats[-1])

with open('floats.bin', 'wb') as fp:
    floats.tofile(fp)  # 把数组存入一个二进制文件里


floats2 = array('d')  # 新建一个双精度浮点空数组

with open('floats.bin', 'rb') as fp:
    floats2.fromfile(fp, 10**7)  # 把1000万个浮点数从二进制文件里读取出来 只需0.1秒比从文本文件读取要快60倍

print(floats2[-1])

print(floats2 == floats)  # 检查两个数组内容是否一致

c = [1, 2, 3]
c.extend([5,6])
c.extend([1])
print(c)  # [1, 2, 3, 5, 6, 1]
