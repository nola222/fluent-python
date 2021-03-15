# -*- coding: utf-8 -*-
# Nola
"""
    规范化文本匹配实用函数
"""
from unicodedata import normalize


def nfc_equal(str1, str2):
    """
    NFC规范化
    :param str1:
    :param str2:
    :return:
    """
    return normalize('NFC', str1) == normalize('NFC', str2)


def fold_equal(str1, str2):
    """
    不区分大小写比较
    :param str1:
    :param str2:
    :return:
    """
    return (normalize('NFC', str1).casefold() ==
            normalize('NFC', str2).casefold())


s1 = 'café'
s2 = 'cafe\u0301'
print(s1 == s2)  # False
print(nfc_equal(s1, s2))  # True
print(nfc_equal('A', 'a'))  # False
print('{:-^30}'.format('-'))

s3 = 'Straße'
s4 = 'strasse'
print(s3 == s4)  # False
print(nfc_equal(s3, s4))  # False
print(fold_equal(s3, s4))  # True
print(fold_equal('A', 'a'))  # True
