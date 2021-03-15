# -*- coding: utf-8 -*-
# Nola


"""
    编码默认值：一团糟
"""

import sys, locale

# 探索编码默认值
expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdin.encoding
        sys.stderr.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """

my_file = open('dummy', 'w')

for expression in expressions.split():
    value = eval(expression)  # 转换为表达式
    print(expression.rjust(30), '->', repr(value))  # str输出不带引号

my_file.close()



# def calculate(exp):
#     val = eval(exp)
#     print(val)
#
# if __name__ == '__main__':
#     x = 1
#     y = 2
#     exp = "x + y"
#     calculate(exp)
