# -*- coding: utf-8 -*-
# Nola
from array import array

a = array('i', [5, 6, 12, 15])
b = array(a.typecode, sorted(a, reverse=True))
print('a ->', a)
print('b ->', b)
# print(a.sort())   # python3.4开始数组类型 不支持list.sort()这种就地排序方法。

'''
    内存视图memoryview是一个内置类，能让用户在不复制内容的情况下操作同一个数组的不同切片。
    内存视图其实是泛化和去数学化的Numpy数组，让你在不需要复制内容的前提下，在数据结构之间共享内存。
    memoryview.cast会把同一块内存里的内容打包成一个全新的memoryview对象。
'''

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)  # 利用含5个短整型有符号整数的数组创建一个memoryview
print(len(memv))
print(memv[0])  # memv里的5个元素跟数组的没有区别

memv_oct = memv.cast('B')  # 把memv里面的内容转换成B类型，无符号字符
print(memv_oct.tolist())  # 以列表的形式查看memv_oct里面的内容
memv_oct[5] = 4  # 把位于位置5的字节赋值成4
print(memv_oct.tolist())
print(numbers)
