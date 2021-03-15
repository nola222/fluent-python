# -*- coding: utf-8 -*-
# Nola
"""
    Unicode文本排序
    python比较任何类型的序列时，会一一比较序列里的各个元素。对字符串来说比较的是码位。
    python中非ASCII文本的标准排序方式是使用locale.strxfrm函数，把字符串转换成适合所在区域进行比较的形式，使用此函数需先进行区域设置
"""
import locale
import pyuca

# 巴西水果
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))

locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8')  # 区域设置是全局的，不推荐在库中调用setlocale函数。应用或框架应在进行程序启动时进行设定区域设置。
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)

# 使用Unicode排序算法排序  PyUCA库是它的纯Python实现 只支持python3.x

coll = pyuca.Collator()
sorted_fruit = sorted(fruits, key=coll.sort_key)  # 使用pyuca.Collator.sort_key方法
print(sorted_fruit)
