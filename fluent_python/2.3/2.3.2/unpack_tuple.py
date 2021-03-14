# -*- coding: utf-8 -*-
# Nola
import os


def unpack_tuple():
    lax_cordinates = (-118.40687, 33.94251)  # 美国洛杉矶国际机场经纬度
    longitude, latitude = lax_cordinates
    return longitude, latitude


def parallel_assignment():
    a, b, *rest = range(5)
    print(a, b, rest)
    a, b, *rest = range(3)
    print(a, b, rest)
    a, b, *rest = range(2)
    print(a, b, rest)
    a, *rest, b = range(5)
    print(a, rest, b)
    *head, a, b = range(2)
    print(head, a, b)


if __name__ == '__main__':
    longitude, latitude = unpack_tuple()
    print("经度：", longitude)
    print("纬度：", latitude)
    print(divmod(20, 8))  # divmod(x,y)返回一个元组(x//y, x%y) 商和余数
    print(20 // 8, 20 % 8)
    print("@.@ " * 10 + "\n" * 2)
    t = divmod(35, 4)
    quotient, remainder = t
    print(quotient, remainder)
    x = (50, 12)
    print(divmod(*x))
    path, last_filename = os.path.split("/home/abc/test123/abc.py")
    print(path, last_filename)

    # 国际化软件 _不是一个理想的占位符，_是gettext.gettext函数的常用别名
    parallel_assignment()
