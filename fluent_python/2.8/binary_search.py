# -*- coding: utf-8 -*-
# Nola

"""
    二分查找算法：
        从有序列表的侯选区data[0:n]开始，通过对待查找的值与候选区的值比较，可以使候选区减少一半

        - 在一段数字内，找到中间值，判断要找的值和中间值大小的比较
        - 若中间值大一些，则在中间值的左侧区域继续按照上述方式查找
        - 若中间值小一些，则在中间值的右侧区域继续按照上述方式查找
        - 直到找到目标数字。
"""
import time


def cal_time(func):
    """
    闭包（内部函数调用外部函数参数，返回内部函数）实现函数执行计时器 装饰器
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s执行时间为：%s" % (func.__name__, t2 - t1))
        return result

    return wrapper


@cal_time
def binary_search_algorithm(data, target_val):
    low = 0  # 最小下标
    high = len(data) - 1  # 最大下标

    # 最小下标小于等于最大下标时存在中间值
    while low <= high:
        middle = (low + high) // 2  # 中间值下标
        if data[middle] == target_val:
            # 中间下标对应的值为目标查找值，返回中间下标
            return middle
        elif data[middle] > target_val:
            high = middle - 1
        else:
            low = middle + 1
    # 未找到
    return


if __name__ == '__main__':
    data = list(range(20))
    target_index = binary_search_algorithm(data, 15)
    target_val = data[target_index]
    print(target_index, target_val)
