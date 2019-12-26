#/usr/bin/env python
import import_module,time
import_module.fun()
print(time.time())

#from import_module import fun  #导入指定模块中的指定的定义方法，且本文件中不能出现重名的方法
from import_module import fun as fun_import_module
def fun():
    print('in the modules')

fun()
fun_import_module()

#跨目录下的模块导入
import os,sys
#print(__file__) #相对路径
print(os.path.abspath(__file__)) #绝对路径

print(os.path.dirname(os.path.abspath(__file__))) #上一级目录

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #上上级目录

BASE_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_PATH)
print(sys.path)

from day2 import function

function.func()

#导入包
import import_package   #运行包内的__init__.py

from import_package import import_bao  #或者在__init__.py文件中添加from 。importimport_bao

import_bao.bao()

#import_package.import_bao.bao()  #使用__init__.py中的添加了import命令，调用bao方法