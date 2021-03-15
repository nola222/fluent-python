# -*- coding: utf-8 -*-
# Nola
"""
    极端规范化：去掉变音符号（重音符、下加符等）
"""
import unicodedata
import string


def shave_mark(txt):
    """
    去掉全部变音符号
    :param txt:
    :return:
    """
    norm_txt = unicodedata.normalize('NFD', txt)  # 把所有字符分解成基本字符和组合记号
    shaved = ''.join(c for c in norm_txt
                     if not unicodedata.combining(c))  # 过滤掉所有组合记号  返回规范化组合类
    return unicodedata.normalize('NFC', shaved)  # 重组所有字符


order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
print(shave_mark(order))
Greek = 'Zέφupoς, Zéfiro'
print(shave_mark(Greek))


def shave_marks_latin(txt):
    """
    把拉丁基字符中的所有变音符号删除
    :param txt:
    :return:
    """
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:  # 基字符为拉丁字母时，跳过组合记号
            continue  # 忽略拉丁基字符上的变音符号
        keepers.append(c)  # 保存当前字符
        # 若不是组合字符，那就是新的基字符
        if not unicodedata.combining(c):  # 检测新的基字符，判断是不是拉丁字母
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)  # 重组所有字符


# 更彻底的规范化是把西文文本中常见符号替换成ASCII中的对等字符
single_map = str.maketrans(""",ƒ,,†ˆ‹‘’“”•––˜›""",
                           """'f''*^<''""---~>""")  # 构建字符替换字符的映射表
# table = {ord('€'): ord('<euro>')}
# print(table)
multi_map = str.maketrans({'‰': '<per mille>', '€': '<euro>', '…': '...', '™': '(TM)', '‡': '**'})
table1 = str.maketrans('OE', 'OE')
table2 = str.maketrans('oe', 'oe')

# multi_map = str.maketrans({'€': '<euro>','…': '...','OE': 'OE','™': '(TM)','oe': 'oe','‰': '<per mille>','‡': '**',})
#
multi_map.update(single_map)  # 合并两个映射表
multi_map.update(table2)
multi_map.update(table1)


def dewinize(txt):
    """
    把win1252符号替换成ASCII字符或序列
    :param txt:
    :return:
    """
    return txt.translate(multi_map)  # 不影响ASCII或latin文本，只替换Microsoft在cp1252中为latin1额外添加的字符


def asciize(txt):
    """
    把文本中的常见符号转换成ASCII字符
    :param txt:
    :return:
    """
    no_marks = shave_marks_latin(dewinize(txt))  # 调用dewinize去掉变音符
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)  # 使用NFKC规范化把字符和与之兼容的码位组合起来


print(dewinize(order))
print(asciize(order))
