# -*- coding: utf-8 -*-
# Nola
"""
    获取关于参数的信息
"""
import bobo

"""
    HTTP微框架Bobo有个使用函数内省的好例子，bobo.query装饰器把一个普通的函数与框架的请求处理机制集成起来。
    Bobo会内省hello函数，发现它需要一个名为person的参数，然后从请求中获取那个名称对应的参数，将其传给hello函数，因此程序员根本不用触碰请求对象。
"""


@bobo.query('/', method=('GET',))
def hello(person):
    return 'Hello %s!' % person
