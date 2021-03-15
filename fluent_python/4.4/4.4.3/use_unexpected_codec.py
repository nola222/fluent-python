# -*- coding: utf-8 -*-
# Nola
"""
    使用预期之外的编码加载模块时抛出SyntaxError
    python3默认使用utf-8编码源码，python2从2.5开始默认使用ASCII，若加载.py模块中包含utf-8之外的数据，未声明编码会得到上面的错误
    python3允许在源码中使用非ASCII标识符
"""
