# -*- coding: utf-8 -*-
# Nola

"""
    具名元组除了从普通元组那里继承的属性之外，还有一些自己的专有属性。
    _fields类属性
    _make(iterable)类方法
    _asdict()实例方法  返回一个有序字典
"""

from collections import namedtuple


class UseFunc(object):
    def __init__(self):
        # 参数一类名，参数儿可由字符串组成的迭代对象，或者由空格隔开的字段名组成的字符串。
        self.City = namedtuple("City", "name country population coordinates")
        self.LatLong = namedtuple("LatLong", "lat long")

    def use_class_attr(self):
        """
        具名元组类属性
        :return:
        """
        return self.City._fields

    def use_class_method(self):
        """
        具名元组类方法
        :return:
        """
        delhi_data = ("Delhi NCR", "IN", 21.935, self.LatLong(28.4364521, 77.526642332))
        delhi = self.City._make(delhi_data)  # 接收一个可迭代对象来生成这个类的一个实例，类似City(*delhi_data)
        return delhi

    def use_inst_method(self):
        """
        具名元组实例方法
        :return:
        """
        delhi = self.use_class_method()
        for key, value in delhi._asdict().items():
            print(key + ":", value)


if __name__ == '__main__':
    use_func = UseFunc()
    fields = use_func.use_class_attr()
    print(fields)
    delhi = use_func.use_class_method()
    print(delhi)
    use_func.use_inst_method()
