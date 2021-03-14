# -*- coding: utf-8 -*-
# Nola
import array


def use_genexps(strings):
    """
    使用生成器表达式建立元组和数组
    :param strings:
    :return:
    """
    gen_tuple = tuple(ord(symbol) for symbol in strings)  # 生成器表达式是一个函数调用过程的唯一参数，不需要括号括起来
    gen_array = array.array("I", (ord(symbol) for symbol in strings))  # array构造方法需要两个参数，第一个参数指定数组种数字的存储方式
    return gen_tuple, gen_array


def cartesian_product(colors, sizes):
    for t_shirt in ("%s %s" %(c, s) for c in colors for s in sizes):
        return t_shirt


if __name__ == '__main__':
    strings = "@#$%^&*("
    gen_tuple, gen_array = use_genexps(strings)
    print(gen_tuple)
    print("@.@ " * 10 + "\n" * 2)
    print(gen_array)  # 如果只需一个包含数字的列表，那么array.array比list更高效
    print("@.@ " * 10 + "\n" * 2)
