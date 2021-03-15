# -*- coding: utf-8 -*-
# Nola
"""
    dict和set的背后
        一个关于效率的测试:
            在一个有1000万个键的字典里查找1000个数，花在每个数上的时间不过是0.337微秒，相当于每个数差不多三分之一的微秒。
            最快时间来自集合交集花费的时间，最糟糕的来自列表花费时间。
            由于列表没有散列表来支持in运算符，每次搜索都需要扫描一次完整的列表，导致所需的时间根据列表大小呈线性增长。
"""