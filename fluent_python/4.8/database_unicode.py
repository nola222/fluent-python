# -*- coding: utf-8 -*-
# Nola
"""
    Unicode数据库
"""
import unicodedata
import re

re_digit = re.compile(r'\d')  # 规则匹配数字

sample = '1\xbc\xb2\u0969\u136b\u216b\u2466\u2480\u3285'

for char in sample:
    print('U+%04x' % ord(char),  # U+0000格式的码位
          char.center(6),  # 长度为6的字符串中居中显示字符
          're_dig' if re_digit.match(char) else '_',
          'isdig' if char.isdigit() else '_',
          'isnum' if char.isnumeric() else '_',
          format(unicodedata.numeric(char), '5.2f'),  # 使用长度为5，小数点后保留2位的浮点数显示数值
          unicodedata.name(char),  # Unicode便准字符的名称
          sep='\t')
