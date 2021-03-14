# -*- coding: utf-8 -*-
# Nola

"""
    接受表达式的元组可以是嵌套式的，如(a, b, (c, d))，只要这个接受元组嵌套结构符合表达式本身的嵌套结构符合表达式本身的嵌套结构。
"""


def nesting_tuple():
    metro_areas = [
        ("Tokyo", "JP", 36.235, (35.6545545, 123.1345654)),
        ("Delhi NCR", "IN", 29.135, (28.1235444, 77.16626354)),
        ("Mexico City", "MX", 20.142, (19.0231234, -99.1364566)),
        ("New York-Newark", "US", 20.104, (40.58542224, -74.15624232)),
        ("Sao Paulo", "BR", 19.649, (-23.4544511, -46.652311666)),
    ]

    print('{:15} | {:^9} | {:^9} |'.format('', 'lat.', 'long.'))  # 格式控制{参数序号:格式控制标记} ^居中 <左对齐 >右对齐 宽度 精度 类型
    fmt = '{:15} | {:9.4f} | {:9.4f} |'
    for name, cc, pop, (latitude, longitude) in metro_areas:
        if longitude < 0:  # 西半球
            print(fmt.format(name, latitude, longitude))


if __name__ == '__main__':
    nesting_tuple()
    print("{0:-^30}".format("format()用法："))
    print("{}-{}".format("if", "else"))  # 返回新字符串，逗号分割参数
    print("圆周率{{{1}-{2}}}是{0}".format("无理数", 3.1415926, "..."))  # 连接不同类型，参数从0开始编号，第一个位置的参数对应0，输出大括号{{{0}}}
    s = "python"
    print("{0:*^30}".format(s))  # 用*填充宽度
    print("{0:>30}".format(s))  # 默认用空格填充宽度
    print("{0:<20}".format(s))
    print("{0:-^20,}".format(123456789))  # (, )格式标记中，表示千位分隔符
    print("{0:.3f}".format(1235.3654))  # 精度
    print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425))  # 类型 b-整数二进制，c-整数对应的unicode字符，doxX-十/八/小写十六/大写十六进制
    print("{0:e},{0:E},{0:f},{0:%}".format(3.14))  # 浮点类型，e-小写e的指数，E-大写E的指数形式，f-浮点数标准浮点形式，%-输出浮点数百分形式
