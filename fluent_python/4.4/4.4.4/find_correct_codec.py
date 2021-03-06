# -*- coding: utf-8 -*-
# Nola
"""
    如何找出字节序列的编码
        不能，必须有人告诉你
        通过试探和分析找出编码：
            b'\x00'字节经常出现，可能时16或者32位编码，不是8位编码，因为纯文本中不能含空字符
            b'\x20\x00'字节经常出现，可能是utf-16le编码中的空格字符（U+0020）
        统一字符编码侦测包Chardet，能识别支持的30种编码，是一个python库，也提供命令行工具chardetect
"""
