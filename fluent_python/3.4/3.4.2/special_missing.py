# -*- coding: utf-8 -*-
# Nola
"""
    特殊方法__missing__
"""


class StrKeyDict0(dict):  # 继承dict

    def __missing__(self, key):
        if isinstance(key, str):  # 若找不到的key本身就是字符串 抛出KeyError
            raise KeyError(key)
        return self[str[key]]  # 若找不到的键不是字符串，转换成字符串再进行修改

    def get(self, key, default=None):
        try:
            return self[key]  # get方法把查找工作用self[key]形式委托给__getitem__，这样在宣布失败之前，还可以通过__missing__再给某个键一次机会。
        except KeyError:  # 抛出KeyError说明__missing__也失败了，返回default
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()  # 先按照传入key原本值查找，再转换成str再次查找。 dict.keys()返回值是一个“视图”
