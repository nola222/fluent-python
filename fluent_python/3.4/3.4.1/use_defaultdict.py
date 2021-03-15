# -*- coding: utf-8 -*-
# Nola

"""
    defaultdict：处理找不到的键
    创建defaultdict对象时候，需要给他配置一个找不到键创造默认值的方法（可调用的对象），这个可调用对象在__getitem__时找到不键时被调用，让
    __getitem__返回某种默认值
    背后其实是特殊方法__missing__,它会在defaultdict遇到找不到的键时候调用default_factory。
"""
import collections

index = collections.defaultdict(list)  # 把list构造方法作为default_factory来创建一个defaultdict
