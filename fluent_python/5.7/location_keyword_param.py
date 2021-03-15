# -*- coding: utf-8 -*-
# Nola
"""
    从定位参数到仅限关键字参数：
         Python最好特性之一是提供了极为灵活的参数处理机制，Python3进一步提供了关键字参数。
"""


def tag(name, *content, cls=None, **attrs):  # cls关键字参数只能通过关键字参数指定，不会捕获未命名的定位参数。若想指定仅限关键字参数，要把它们放到前面有*的参数后面
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls  # 避免属性与class关键字重名使用cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value)
                           for attr, value
                           in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' %
                         (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)


print('{:-^50}'.format("生成多个html标签"))
print(tag('br'))  # 传入单个定位参数
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world'))  # 第一个参数后面任意个参数会被*content捕获，存入一个元组
print(tag('p', 'hello', id=33))  # cls参数只能作为关键字参数传入
print(tag('p', 'hello', 'world', cls='sidebar'))
print(tag(content='testing', name='img', src='www.baidu.com'))  # 即便是第一个参数也能作为关键字传入
my_tag = {'name': 'img', 'src': './sunshine.gif',
          'title': 'Sunny Day', 'cls': 'framed'}
print(tag(**my_tag))  # 字典中的所有元素作为单个元素传入，同名键会绑定到对对应的具名参数(name)上，余下被**attrs捕获。


def f(s, *, d):  # 不想支持数量不定的定位参数，但是想支持仅限关键字参数，在前面加一个*
    return s, d


print(f(1, d=4))
