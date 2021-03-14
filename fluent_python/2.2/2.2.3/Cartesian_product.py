# -*- coding: utf-8 -*-
# Nola

"""
    列表里是3中不同尺寸的T恤衫，每个尺寸都有2个颜色
    使用列表推导式算出这个列表，6种组合。

    列表推导式作用只有一个：生成列表
    要想生成其他类型的序列，使用生成器表达式。
"""


def cartesian_product(colors, sizes):
    t_shirts = [(color, size) for color in colors
                for size in sizes]
    return t_shirts


if __name__ == '__main__':
    colors = ["black", "white"]
    sizes = ["S", "M", "L"]
    t_shirts = cartesian_product(colors, sizes)
    print(t_shirts)
