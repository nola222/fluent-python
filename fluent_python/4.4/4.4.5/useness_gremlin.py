# -*- coding: utf-8 -*-
# Nola
"""
    BOM:有用的鬼符
    b'\xff\xfe'（十进制数255，254）就是BOM，字节序标记，指明编码时使用Intel CPU的小字节序
    小字节序设备中，在字节偏移的di2位和3位编码位69和0  UTF-16LE
    大字节序CPU中，编码顺序时相反的，0和69           UTF-16BE
"""

u16 = 'El Niño'.encode('utf_16')
print(u16)
print(list(u16))
print('-' * 30)

u16le = 'El Niño'.encode('utf_16le')
print(u16le)
print(list(u16le))
print('-' * 30)

u16be = 'El Niño'.encode('utf_16be')
print(u16be)
print(list(u16be))
print('-' * 30)

a = b'$'
b = bytes('￥'.encode('utf-8'))
print(len(a), type(a), len(b), type(b))
