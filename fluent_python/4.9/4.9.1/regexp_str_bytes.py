# -*- coding: utf-8 -*-
# Nola
"""
    正则表达式中的字符串和字节序列
"""
import re

re_numbers_str = re.compile(r'\d+')
re_word_str = re.compile(r'\w+')
re_numbers_bytes = re.compile(rb'\d+')
re_word_bytes = re.compile(rb'\w+')

text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"  # 要搜索的Unicode文本，包括1729的泰米尔数字
            " as 1729 = 1³ + 12³ = 9³ + 10³.")

text_bytes = text_str.encode('utf_8')

print('Text', repr(text_str), sep='\n ')
print('Numbers')
print(' str :', re_numbers_str.findall(text_str))  # 字符串模式\d+能匹配泰米尔数字和ASCII数字
print(' bytes :', re_numbers_bytes.findall(text_bytes))  # 字节序列中只能匹配ASCII字节中的数字
print('Words')
print(' str :', re_word_str.findall(text_str))  # 字符串\w+能匹配字母、上标、泰米尔数字和ASCII数字
print(' bytes :', re_word_bytes.findall(text_bytes))  # 字节序列模式只能匹配ASCII字节中的字母和数字
