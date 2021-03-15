# -*- coding: utf-8 -*-
# Nola
"""
    结构体和内存视图：
        struct模块提供一些函数，把打包的字节序列转换成不同类型字段组成的元组，还有一些函数用于执行反向转换，把元组转换成打包的字节序列。
        struct模块能处理bytes、bytearray和memoryiew对象。
"""
import struct

fmt = '<3s3sHH'  # <是小字节序  3s3s是两个3字节序列  HH是两个16位二进制整数
with open('1.gif', 'rb') as fp:
    img = memoryview(fp.read())  # 使用内存中的文件内容创建一个memoryview对象
print(img)
header = img[:10]  # 使用切片创建一个memoryview对象，这里不会复制字节序列 是一个新的memoryview对象
print(bytes(header))  # 转换成字节序列 为了显示 这里复制了10字节
print(struct.unpack(fmt, header))  # 拆包memoryview得到一个元组，包含类型、版本、宽度和高度
del header  # 删除引用 释放memoryview实例所占的内存
del img
