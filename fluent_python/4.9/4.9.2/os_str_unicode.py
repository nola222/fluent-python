# -*- coding: utf-8 -*-
# Nola
"""
    os函数中的字符串和字节序列：
        在GUN/Linux内核不理解Unicode，在文件名中使用字节序列都是无效的，无法解码成字符串。
        为了规避这个问题，os模块中的所有函数、文件名或路径名参数既能使用字符串，也能使用字节序列。
"""
import os

# 把字符串和字节序列传给listdir
print(os.listdir('.'))
print(os.listdir(b'.'))

# 使用surrogateescape错误处理方式
name_bytes = os.listdir(b'.')[0]
name_str = name_bytes.decode('ascii', 'surrogateescape')
print(name_str)
print(name_str.encode('ascii', 'surrogateescape'))
