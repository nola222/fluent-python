# -*- coding: utf-8 -*-
# Nola
"""
    凭借着Numpy和SciPy提供的高阶数组和矩阵操作，Python成为科学计算应用的主流语言。
    Numpy实现了多维同质数组和矩阵，这些数据结构不但能处理数字，还能存放其他由用户定义的记录。

    SciPy是基于Numpy的另一个库,提供了很多科学计算有关的算法，专为线性代数、数值积分和统计学设计。
    SciPy的高效基于背后的C和Fortran代码，而这些跟计算有关的部分都源自于Netlib库
    SciPy把基于C和Fortran的工业级数学计算功能用于交互式且高度抽象的Python包装起来。
"""

import numpy
from time import perf_counter as pc

a = numpy.arange(12)  # 新建一个0~11的整数的numpy.ndarray
print(a)
print(type(a))  # 查看类型
print(a.shape)  # 查看数组的纬度,它是一个一维的,有12个元素的数组
a.shape = 3, 4  # 把数组变成一个二维的数组
print(a)
print("-" * 20)
print(a[2])  # 打印第二行
print("-" * 20)
print(a[2, 1])  # 打印第二行第一列
print("-" * 20)
print(a[:, 1])  # 打印第一列
print("-" * 20)
print(a.transpose())  # 行列交换
print("-" * 20)

floats = numpy.random.rand(10**7)
print(floats[-3:])
floats *= .5
print(floats[-3:])
t0 = pc()
floats /= 3
c = pc() - t0  # 使用精度和性能比较高的计时器 p3.3即以上版本有这个库  处理1000万个浮点数,所需时间不足40毫秒
print(c)  # 计算操作耗时(秒)
numpy.save('floats-10M', floats)
floats2 = numpy.load('floats-10M.npy', 'r+')  # 把数据存入后缀为.npy的二进制文件  load方法利用了一种叫做内存映射的机制,在内存不足的情况下仍可以对数组切片.
floats2 *= 6
print(floats2[-3:])
