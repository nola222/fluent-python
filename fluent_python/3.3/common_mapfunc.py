# -*- coding: utf-8 -*-
# Nola
"""
    常见的映射方法：
        dict、defaultdict和OrderedDict的常见方法，后两个数据类型是dict的变种，位于collections模块内。
        可选参数用[...]表示。
"""

# 用setdefault处理找不到的键，当字典d[k]找不到正确键时，Python会抛出异常，这个行为符合Python所信奉的“快速失败”哲学。
my_dict = {}
my_dict.setdefault(1, ['one']).append('two')  # 通过查找插入新值
print(my_dict)
