# -*- coding: utf-8 -*-
# Nola
"""
    处理UnicodeDecodeError
    陈旧的8位编码如cp1252 iso8859_1 koi8_r能解码任何字节序列流而不抛出错误，得到是无用输出
    乱码字符称为鬼符
"""
octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
# print(octets.decode('utf-8'))  # utf_8编解码器检测到octets不是有效的utf-8字符串 抛出UnicodeDecodeError
print(octets.decode('utf-8', errors='replace'))
