# -*- coding: utf-8 -*-
# Nola

"""
    使用bisect.insort插入新元素
    排序很耗时，得到一个有序序列之后，最好能够保持它的有序。bisect.insort为了这个存在的。
    insort(seq, item) 把item插入到序列seq中，并能保持seq的升序顺序
"""
import bisect
import random

SIZE = 7
random.seed(1729)

my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)