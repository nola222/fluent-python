# -*- coding: utf-8 -*-
# Nola
"""
    匿名函数
        lambda关键字在python表达式内创建匿名函数
        除了作为参数传给高阶函数之外，Python很少使用匿名函数
        句法限制，lambda表达式要么难以阅读，要么无法写出
        lambda句法只是语法糖：
            与def语句一样，lambda表达式会创建函数对象。这是python中几种可调用对象的一种。
"""

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits, key=lambda word: word[::-1]))  # 使用lambda表达式反转拼写
