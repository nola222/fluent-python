# 如果使用特殊方法
```python
特殊方法的存在是为了被python解释器调用的，自己并不需要调用它。没有my_object.__len__()这种方法，应该使用len(my_object)
python内置类型，bytearray(字节序列)，CPython，__len__实际上会直接返回PyVarObject里面的ob_size属性。

很多时候特殊方法的调用时隐式的for i in x:这个语句背后其实是用iter(x),而这个函数的背后是x.__iter__()方法。

不要自己想当然地随意添加特殊方法，如__foo__之类的，虽然现在这个名字没有被python内部使用，以后就不一定了。
```