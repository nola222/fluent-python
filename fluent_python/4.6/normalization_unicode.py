# -*- coding: utf-8 -*-
# Nola
"""
    为了正确比较而规范化Unicode字符串
    Unicode有组合字符（变音符号和附加到前一个字符上的记号，打印时作为一个整体）
    'é'和'e\u0301'这样的序列叫“标准等价物”，应用程序应该把它们视作相同的字符。
    解决方案：
        unicodedata.normalize函数提供的Unicode规范化。
        第一个参数有：NFC 、NFD 、NFKC 、NFKD 后两种形式只能在特殊情况中使用，如搜索和索引，不能用于持久存储，因为这两种转换会导致数据损失。
"""
from unicodedata import normalize

s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)  # python看到的是不同码位序列，判定不等
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))  # 西方键盘通常可以输出组合字符，因此用户输入的文本默认是NFC形式，最好通过函数清洗字符串。
print(normalize('NFC', s1) == normalize('NFC', s2))  # NFC也是W3C推荐的规范化形式
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFD', s1) == normalize('NFD', s2))
