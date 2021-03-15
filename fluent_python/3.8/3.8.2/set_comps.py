# -*- coding: utf-8 -*-
# Nola

"""
    集合推导：
        Python2.7带来了集合推导和字典推导
"""
from unicodedata import name

s = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}  # name获取字符的名字 把编码在32~255之间的字符名字里有SIGN的单词挑出来放到一个集合中
print(s)
