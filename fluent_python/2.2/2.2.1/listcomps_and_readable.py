# -*- coding: utf-8 -*-
# Nola

"""
    通常原则，只用列表推导式来创建新的列表，并且尽可能保持简短。
    python2.x中，在列表推导式中for关键词之后赋值操作可能会影响列表推导上下文中的同名变量；python3.x中不存在

"""


def change_unicode(strings):
    """
    str转为unicode码位的列表
    :param strings:
    :return:
    """
    codes = []
    for symbol in strings:
        codes.append(ord(symbol))  # ord(string) 将字符串转为Unicode code
    return codes


def change_unicode_too(strings):
    list_codes = [ord(symbol) for symbol in strings]
    return list_codes


if __name__ == '__main__':
    codes = change_unicode("$#%^&*@")
    print(codes)
    print("@.@ " * 10 + "\n" * 2)
    list_codes = change_unicode_too("$#%^&*@")
    print(list_codes)
    print("@.@ " * 10 + "\n" * 2)
