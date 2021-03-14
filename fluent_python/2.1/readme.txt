# 内置序列类型概览
```python
"""
Python标准库用C实现了丰富的序列类型:
    - 容器序列
        - list、tuple和collections.deque这些序列能存放不同类型的数据。存放的是它们所包含的任意类型的对象的引用。
    - 扁平序列
        - str、bytes、bytearray、memoryview和array.array，这种序列只能容纳一种类型。存放的是值，更紧凑。
按照可修改不可修改分类：
    - 可变序列
        - list、bytearray、memoryview、array.array和collections.deque
    - 不可变序列
        - str、tuple和bytes

"""
```