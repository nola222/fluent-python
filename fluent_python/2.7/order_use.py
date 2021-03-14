# -*- coding: utf-8 -*-
# Nola

"""
    list.sort方法就地排序列表，不会把原列表复制一份，所以返回None，就像random.shuffle随机给序列排序
    sorted相反，会返回一个新的list，可接受任何形式的可迭代对象作为参数，包括不可变序列或生成器，不管参数，最后都会返回一个列表。
    sorted参数：
        reverse=True降序，默认False；
        key一个只有一个参数的函数，函数被用在序列每个元素，产生结果是排序算法依赖的对比关键字。
        key默认是恒等函数，即默认用元素自己的值来排序。
"""


def order_something(l):
    print("sorted排序l：")
    print(sorted(l))
    print("原始l：")
    print(l)
    print("sorted降序：")
    print(sorted(l, reverse=True))
    print("sorted使用关键词排序：")
    print(sorted(l, key=len, reverse=True))
    print("原始l：")
    print(l)
    print("使用list.sort")
    new_l = l.sort()
    return new_l, l


if __name__ == '__main__':
    l = ['graph', 'berry', 'pine', 'lemon', 'banana']
    new_l, l = order_something(l)
    print(new_l)
    print(l)
