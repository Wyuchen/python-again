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

print('返回assic对应的值：',chr(50))      #返回assic对应的值

print('对应值的assic码：',ord('2'))       #对应值的assic码

b=()
print('内部方法：',dir(b))                 #返回函数的内部方法

print('返回除法的商和余数:',divmod(5,2))            #返回除法的商和余数

for k,i in enumerate([1,2,3]):           #显示下标
    print(k,i)

print('字符串转换成字典：',eval("{'name':'wz'}"))   #字符串转换成字典

lambda i:i*2        #匿名函数
