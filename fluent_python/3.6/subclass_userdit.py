# -*- coding: utf-8 -*-
# Nola
"""
    创造自定义的映射类型，以UserDict为基类，比普通的dict为基类来得方便。UserDict不是dict的子类，它的data属性是dict的实例，是UserDict存储数据的地方。
"""

import collections


class StrKeyDict(collections.UserDict):  # StrKeyDict是对UserDict的扩展

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str[key]]

    def __contains__(self, key):
        return str(key) in self.data  # contains更简洁，在self.data上查询就好了，不需要self.keys()

    def __setitem__(self, key, item):
        self.data[str(key)] = item  # 把所有的key转换成字符串
