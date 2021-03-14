# -*- coding: utf-8 -*-
# Nola

from math import hypot


class Vector(object):
    """
    实现一个简单的二维向量类
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """
        返回一个向量对象
        :return:
        """
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)  # 返回欧几里得范数 sqrt(x的平方 + y的平方)

    def __bool__(self):
        return bool(abs(self))  # abs内置函数，输入整数或浮点数返回的是输入值的绝对值；输入复数返回复数的模 此处根据向量模大小判断实例对象的真假

    def __add__(self, other):
        """
        向量加法
        :param other:
        :return:
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        向量乘法
        :param scalar: 向量
        :return:
        """
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    # 向量加法
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)
    print("@.@" * 10 + "\n" * 2)

    # 输出向量模
    v = Vector(3, 4)
    print(abs(v))  # 向量的模计算公式：根号下3的平方 + 4的平方 开方
    print("@.@" * 10+ "\n" * 2)

    # 标量乘法（向量与数的乘法，与正数相乘得到向量方向与原向量一致，模变大；与负数相乘，向量方向相反）
    print(v * 3)
    print(abs(v * 3))  # 返回向量模
    print("@.@" * 10 + "\n" * 2)
