# -*- coding: utf-8 -*-
# Nola

"""
    s[a:b:c]形式对s在a和b之间以c为间隔取值。
"""


def obj_slice(s):
    s3 = s[::3]  # 间隔3个取值
    s2 = s[::-2]  # 从右至左间隔2个取值
    s1 = s[::-1]  # 取反
    return s1, s2, s3


if __name__ == '__main__':
    s = "bicycle"
    s1, s2, s3 = obj_slice(s)
    print(s1, s2, s3)
