#/usr/bin/env python

''''
装饰器:为其他函数添加其他功能
1.装饰器需要注意的事项：不能修改被装饰的函数的源代码和调用方法
2.装饰器=>高级函数和嵌套函数
         高阶函数：把一个函数名当做实参传给另外一个函数，返回值中包含函数名
'''

import time
def function():
    time.sleep(2)
    print('function running')

def fun(f):
    start_time=time.time()
    f()
    stop_time=time.time()
    print("function run time: %s" %(stop_time-start_time))

fun(function)

