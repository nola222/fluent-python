# -*- coding: utf-8 -*-
# Nola
"""
    大小写折叠：
        把所有文本变成小写，再做其他转换。使用str.casefold()方法python3.3新增
        对于只包含lantin1字符的字符串，此方法相当于str.lower()
        唯有两个例外：
            微符号'µ'会变成小写的希腊字母“μ”；德语 Eszett（“sharp s”，ß）会变成“ss”
"""
from unicodedata import name

micro = 'µ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)
print('{:-^30}'.format('-'))
eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)
