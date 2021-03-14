# -*- coding: utf-8 -*-
# Nola

"""
    +=背后的特殊方法__iadd__就地加法，若一个类未实现该方法，Python会退一步调用__add__.
    a += b，__iadd__就像调用了a.extend(b)；__add__效果如同a = a + b
    同理+=概念适用于*=，对应__imul__
"""
import dis


def mul_imul(l, t):
    print(id(l))
    l *= 2
    print(id(l))  # 列表增量乘法后内存空间地址不变
    print("{:-<50}".format("-"))
    print(id(t))
    t *= 2
    print(id(t))  # 元组增量乘法后创建一个新的元组


def add_iadd(t):
    print("原始t：", t)
    try:
        t[2] += [50, 60]  # TypeError异常抛出 元组元素不支持赋值
    except TypeError:
        print("元组元素不可被赋值！")
    print(t)  # 但+=还是作用了元组
    t[2].extend([50, 60])  # 可执行不抛异常
    print(t)


def mystery_tuple_assign():
    bytescode = dis.dis("t[2] += [50, 60]")
    return bytescode


if __name__ == '__main__':
    l = [1, 2, 3]
    t = (1, 2, 3)
    x = (1, 2, [10, 20])
    mul_imul(l, t)
    add_iadd(x)
    bytescode = mystery_tuple_assign()
    """
      1           0 LOAD_NAME                0 (t)
              3 LOAD_CONST               0 (2)
              6 DUP_TOP_TWO
              7 BINARY_SUBSCR                              将x[2]的值存入TOS（Top Of Stack）栈的顶端
              8 LOAD_CONST               1 (50)
             11 LOAD_CONST               2 (60)
             14 BUILD_LIST               2
             17 INPLACE_ADD                                计算TOS += [50,60],因为TOS指向一个可变对象
             18 ROT_THREE
             19 STORE_SUBSCR                               x[2] = TOS赋值，这一步失败，是因为x是不可变的元组
             20 LOAD_CONST               3 (None)
             23 RETURN_VALUE

    """
    print(bytescode)
