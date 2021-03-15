# -*- coding: utf-8 -*-
# Nola
"""
    处理UnicodeEncodeError
"""
# 编码成字节序列
city = 'São Paulo'
print(city.encode('utf_8'))  # utf_?能处理任何字符串
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))
# print(city.encode('cp437'))  # 无法处理带~的a，抛出UnicodeEncodeError 默认的错误处理方式strict
print(city.encode('cp437', errors='ignore'))  # 悄无声息跳过无法编码的字符
print(city.encode('cp437', errors='replace'))  # 把无法编码字符字符替换成？
print(city.encode('cp437', errors='xmlcharrefreplace'))  # 把无法编码字符字符替换成XML实体 ã 👉 &#227;

# 编解码器的错误处理方式可扩展，可以将errors参数注册额外的字符串，把一个名称和一个错误处理函数传给codecs.register_error函数
