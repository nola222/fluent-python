# -*- coding: utf-8 -*-
# Nola
"""
    用户定义的可调用类型
        不仅python函数时真正的对象，任何python对象都可以表现的像函数。为此，只需实现实例方法__call__。
"""
import random


class BingoCase(object):
    def __init__(self, items):
        self._items = list(items)  # __init__接受任何可迭代的对象，在本地构建一个副本，防止列表参数的以外副作用
        random.shuffle(self._items)  # 就地将序列的所有元素随机排序 返回None

    def pick(self):
        """取出一个元素"""
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCase')  # 若self._items为空，抛出异常，设定错误信息

    def __call__(self, *args, **kwargs):
        """使bingo(类的实例).pick()的快捷方式是bingo()"""
        return self.pick()


if __name__ == '__main__':
    l = [1, 2, 3, 4, 5]
    print(random.shuffle(l))
    print(l)

    bingo = BingoCase(range(3))
    print(bingo.pick())
    print(bingo())
    print(callable(bingo))
    print(bingo())
    print(bingo())  # 抛异常IndexError
