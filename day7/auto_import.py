#/usr/bin/env python
#动态导入模块

mod=__import__('day6.example')
print(mod)
print(mod.example)
print(mod.example.C)
obj=mod.example.C()
print('name:%s'%obj.name)


import importlib
obj1=importlib.import_module('day6.example').C()
print(obj1)
print('name:%s'%obj1.name)

#断言--其实和if判断没有什么区别
assert  type(obj1.name) is str
print('type(obj1.name) is str')



