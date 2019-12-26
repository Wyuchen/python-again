#/usr/bin/env python
#内置方法介绍

print('绝对值',abs(-1),abs(2))  #绝对值

print(all([0,2,3]),all([1,2,3]))    #如果可迭代对象中的元素不存在0则返回True，否则为False

print(any([0,2,3]),any([0]),any([]))    #可迭代对象中的元素中只要有一个不是0，则为True

print('十进制转换成二进制:',bin(2))                #将十进制转换成二进制

print('布尔类型：',bool(1),bool(()))            #布尔类型

print(bytes('abc',encoding='utf-8'))          #不可修改的二进制字符串

a=bytearray('abc',encoding='utf-8')           #可修改的二进制字符串
print('未修改之前：',a)
a[0]=50
print('可修改的二进制字符串:',a)

def f(): pass                           #判断是否是可以调用的
print('是否是可以调用',callable([]),'函数可以调用：',callable(f))

print('返回ascii对应的值：',chr(50))      #返回ascii对应的值

print('对应值的ascii码：',ord('2'))       #对应值的ascii码

b=()
print('内部方法：',dir(b))                 #返回函数的内部方法

print('返回除法的商和余数:',divmod(5,2))            #返回除法的商和余数

exec("print('exec命令执行')")                 #exec命令执行
for k,i in enumerate([1,2,3]):           #显示下标
    print(k,i)

print('字符串转换成字典：',eval("{'name':'wz'}"))   #字符串转换成字典

lambda i:i*2        #匿名函数


c=filter(lambda i:i>5,[3,4,5,6,7])   #filter(判断函数,可迭代对象)
for i in c:
    print('使用filter过滤出来的数值{}'.format(i))#forma的使用

print('forzenset()使集合set不可变')

print('打印全局变量:',globals())         #打印全局变量

print('打印本地变量:',locals())          #打印本地变量

print('hash()函数返回对象唯一hash值')

print('id()函数返回对象的内存地址：',id(c))   #id()函数返回对象的内存地址

print('isinstance()函数来判断一个对象是否是一个已知的类型:',isinstance(b,tuple))

from collections import Iterator
print(isinstance(iter([1,2,3,4]),Iterator))
print('iter()函数将可迭代对象转换成迭代器')

d=map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
for j in d:
    print(j)
print('map()函数根据提供的函数条件对指定序列做映射')

print('pow(2,8)函数阶乘：',pow(2,8))

print('repr()转换成字符串：',type([1,2,34]),type(repr([1,2,34])))

print('round()函数四舍五入(默认保留整数)：',round(10.123),round(10.123,1))

print('切片:',[1,2,3,4][slice(2)])
print('slice()函数实现切片对象,slice(stop),slice(start, stop[, step])')


print('sorted()函数对所有可迭代的对象进行排序操作',sorted([2,1,3,2]))

print('vars()函数返回对象object的属性和属性值的字典对象:',vars())

e=zip([1,2,3],['w','z','x'])
for ii in e:
    print(ii)
print('zip()用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象')


print('__import__() 函数用于动态加载类和函数')
__import__('describtion')   # 相当于import describtion


'''
面向对像的内置方法后续补充
super()
setattr()
getattr()
delattr()
hasattr()
issubclass()
staticmethod() 
classmethod()
property()
'''