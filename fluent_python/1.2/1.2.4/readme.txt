# 自定义的布尔值
```python
# 默认情况下，我们自己定义的类的实例总是被认为是真的，除非这个类对__bool__或者__len__函数有自己的实现。
# bool(x)背后实际调用x.__bool__()的结果，若无__bool__方法，bool(x)会尝试调用x.__len__()。返回0，bool会返回False，否则返回True
# 前面向量实现时__bool__里面实现一个向量的模是0，返回False，其他返回True。bool(abs(self))把模值变成了布尔值
# 让Vector.__bool__更高效
def __bool__(self):
    return bool(self.x or self.y)

# 此种实现不易读，省掉abs从__abs__到平方再到平方根这些中间步骤。or运算符返回x或者y本身的值，通过bool把返回值显示转换为布尔值。
```