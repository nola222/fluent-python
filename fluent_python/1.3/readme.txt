# 特殊方法一览
> 跟运算符无关的特殊方法
```graph
|       类别         |                                            方法名                                             |
|:-----------------:|:--------------------------------------------------------------------------------------------:|
|字符串/字节序列表示形式|                            __repr__、__str__、__format__、__bytes__                            |
|     数值转换       |              __abs__、__bool__、__complex__、__int__、__float__、__hash__、__index__            |
|     集合模拟       |                   __len__、__getitem__、__setitem__、__delitem__、__contains__                 |
|     迭代枚举       |                                  __iter__、__reversed__、__next__                             |
|    可调用模拟      |                                           __call__                                           |
|    上下文管理      |                                       __enter__、__exit__                                     |
|   实例创建和销毁    |                                __new__、__init__、__del__                                     |
|     属性管理      |               __getattr__、__getattribute__、__setattr__、__delattr__、__dir__                 |
|    属性描述符      |                               __get__、__set__、__delete__                                    |
|   跟类相关的服务   |                        __prepare__、__instancecheck__、__subclasscheck__                       |

```
---

> 跟运算符相关的特殊方法
```graph
|       类别       |                                   方法名和对应的运算符                                            |
|:---------------:|:---------------------------------------------------------------------------------------------:|
|    一元运算符     |                              __neg__ -、__pos__ +、__abs__ abs()                               |
|  众多比较运算符    |             __lt__ <、__le__ <=、__eq__ ==、__ne__ !=、__gt__ >、__ge__ >=                      |
|     算术运算符    | __add__ +、__sub__ -、__mul__ *、__truediv__ /、__floordiv__ //、__mod__ %、__divmod__ divmod()、__pow__ **或pow()、__round__ round()|
|   反向算术运算符   | __radd__、__rsub__、__rmul__、__rtruediv__、__rfloordiv__、__rmod__、__rdivmod__、__rpow__       |
| 增量赋值算术运算符  |          __iadd__、__isub__、__imul__、__itruediv__、__ifloordiv__、__imod__、__ipow__           |
|     位运算符      |         __invert__ ~、__lshift__ <<、__rshift__ >>、__and__ &、__or__ |、__xor__ ^              |
|    反向位运算符    |                    __rlshift__ 、__rrshift__ 、__rand__ 、__ror__ 、__rxor__                     |
|  增量赋值位运算符   |                    __ilshift__ 、__irshift__ 、__iand__ 、__ior__ 、__ixor__                     |

```
**交换两个操作数，调用反向运算符(b * a)；增量赋值运算符是一种把中缀运算符变成赋值运算的捷径(a = a * b变成a *= b)**