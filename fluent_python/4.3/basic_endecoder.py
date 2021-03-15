# -*- coding: utf-8 -*-
# Nola
"""
    基本的编解码器
        Python自带超过100种编解码器，用于在文本和字节之间相互转换。

    典型编码介绍：
        - latin1(iso8859_1):其他编码的基础，如cp1252和Unicode
        - cp1252:Microsoft制定的latin1超集，添加了有用的符号
        - cp437:IBN PC最初的字符集，包含框图符号，与latin1不兼容
        - gb2312:用于编码简体中文的陈旧标准，这是亚洲语言中使用较为广泛的多字节编码之一
        - utf-8:目前web中最常见的8位编码与ASCII兼容（纯ASCII文件是有效的utf-8文本）
        - utf-16le:utf-16的16位编码方案的一种形式
"""

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'E1 Niño'.encode(codec), sep='\t')
