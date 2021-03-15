# -*- coding: utf-8 -*-
# Nola
"""
    处理文本文件
        最佳实践“Unicode三明治”
           -----
        -         -   bytes → str  解码输入的字节序列
        |----------|  100% str     只处理文本
        -         -   str → bytes  编码输出的文本
           -----
"""
import os

with open('cafe.txt', 'w', encoding='utf-8') as f:  # open函数采用文本模式，返回一个TextIOWrapper对象
    f.write('café')  # 写入4个字符

# 一个平台上的编码问题 不能依赖默认编码 多台设备或多种场合下云行代码，打开文件始终应该明确传入encoding参数

with open('cafe.txt', mode='r', encoding='cp1252') as f:
    content = f.read()
    print(content)
    print(f.encoding)
    print(os.stat('cafe.txt').st_size)  # 读取5个字符 é占两个字节

with open('cafe.txt', mode='rb') as f:  # 二进制模式读取文件 返回的时BufferReader对象  除非想判断编码(Chardet)，否则不要使用此模式
    content = f.read()  # 读取返回的字节序列
    print(content)
    print(os.stat('cafe.txt').st_size)  # 读取5个字符 é占两个字节
