# -*- coding: utf-8 -*-
# Nola
"""
    双向队列和其他形式的队列
    collections.deque类(双向队列)是一个线程安全,可以快速从两端添加
    或者删除元素的数据类型.
    若想要有一种数据类型来存放"最近用到的几个元素",deque是一个好的选择.在新建一个双向队列的时候,可以指定这个队列的大小,
    队列满员,从反向端删除过期的元素,在尾端添加新的元素.

    popleft和rotate,从队列的中间删除元素会慢一些,因为它只对头尾的操作进行了优化.
    append和popleft都是原子操作,deque在多线程程序中安全地当作先进先出的栈使用,而不用需要担心资源锁的问题.
"""

from collections import deque

dq = deque(range(10), maxlen=10)  # maxlen可选参数,代表队列可容纳的元素的数量,一旦设定属性不能修改
print(dq)
print('-' * 20)

dq.rotate(3)  # 队列的旋转操作,n>0时,队列右边n个元素会移动到队列左边;反之,最左边n个元素会被移动到右边.
print(dq)
print('-' * 20)

dq.rotate(-3)
print(dq)
print('-' * 20)

dq.appendleft(-1)  # 当一个已满的队列做尾部添加操作时候,头部元素会被删除掉.
print(dq)
print('-' * 20)

dq.extend([11, 22, 33])  # 在尾部添加几个元素 左端会挤掉几个元素
print(dq)
print('-' * 20)

dq.extendleft([10, 20, 30, 40])  # 会把迭代器里的元素逐个添加到双向队列的左边,因此迭代器里的元素会逆序出现在队列里.40 30 ...
print(dq)
print('-' * 20)

"""
    其他python标准库对队列的实现:
        queue:提供了同步(线程安全)类Queue,LifoQueue和PriorityQueue.可选参数maxsize,满员会被锁住,直到另外的线程移除了某个元素来腾出位置.
        multiprocessing:实现了自己的Queue,类似queue.Queue,设计给进程间通信用的.
        asyncio:Python3.4新提供的包,为异步编程里的任务管理提供了专门的便利.
        heapq:没有队列类,提供了heappush和heappop方法,可以把可变序列当作堆队列或者优先队列来使用.
"""
