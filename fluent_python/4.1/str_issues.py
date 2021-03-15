# -*- coding: utf-8 -*-
# Nola
"""
    字符问题：
        Unicode标准把字符的标识和具体的字节表述进行明确区分：
            - 字符的标识：即码位，是0~1 114 111的数字（十进制），在Unicode标准中以4~6个十六进制数字表示，加前缀“U+”。如字母A的码位是U+0041。
            - 字符的具体表述取决于所用的编码。编码是在码位和字节序列之间转换时使用的算法。在UTF-8编码中A的码位编码成单个字节\x41，而在UTF-16LE
            编码中编码成两个字节\x41\x00

        把码位转换成字节序列的过程是编码；把字节序列转换成码位的过程是节码。
"""

s = 'caf￥'
print(len(s))  # cafe有4个Unicode字符

b = s.encode("utf8")  # 以utf8编码  把str对象编码成bytes对象
print(b)  # bytes字面量以b开头
print(len(b))  # 字节序列b有6个字节  在utd-8中￥的码位编码成3个字节

print(b.decode("utf8"))  # 使用utf-8把bytes对象解码成str对象

"""
    .decode()和.encode()区别：
        想象【字节序列】为晦涩难懂的机器磁芯转储，【unicode字符串】为人类可读的文本。
        字节序列变成人类可读的文本字符串就是解码，而把字符串变成用于存储或传输的字节序列就是编码。
"""