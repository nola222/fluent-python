# -*- coding: utf-8 -*-
# Nola
"""
    字节概要
        python内置了两种基本的二进制序列类型：
            python3引入的不可变bytes类型和python2.6添加的可变bytearray类型。
            （python2.6也引入bytes类型，但那只不过是str类型的别名，与python3的bytes类型不同）

"""
import array

cafe = bytes("caf￥", encoding="utf-8")  # bytes对象是可以从给定的编码构建
print(cafe)
print(cafe[0])  # 各元素是range(256)内的整数
print(cafe[:1])  # bytes对象的切片还是bytes对象

# str[0] == str[:1]  这个只对str这个序列类型成立  对其他序列类型来说，s[i]返回的是一个元素，s[i:i+1]返回的是一个相同类型的序列

cafe_arr = bytearray(cafe)  # bytearray对象没有字面量句法，以bytearray()和字节序列字面量参数的形式显示
print(cafe_arr)
print(cafe_arr[-1:])  # bytearray对象切片还是bytearray对象

# 二进制序列有个类方法是str没有的，fromhex，作用是解析十六进制数字对(数字对之间的空格是可选的)，构建二进制序列：
print(bytes.fromhex('12 5E 3D 4F'))

# 使用数组中的原始数据初始化bytes对象
numbers = array.array('h', [-2, -1, 0, 1, 2])  # 类型代码h 创建一个短整数(16位)数组
octets = bytes(numbers)  # octets为numbers字节序列的副本
print(octets)  # 5个短整数的10个字节
