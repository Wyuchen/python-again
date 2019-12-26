#/usr/bin/env python

''''
装饰器:为其他函数添加其他功能
1.装饰器需要注意的事项：不能修改被装饰的函数的源代码和调用方法
2.装饰器=>高级函数和嵌套函数
         高阶函数：把一个函数名当做实参传给另外一个函数，返回值中包含函数名
'''

import time
'''
#不带参数的装饰器
def wapper(f):
    def fun():
        start_time=time.time()
        f()
        stop_time=time.time()
        print("function run time: %s" %(stop_time-start_time))
    return fun
@wapper
def function():
    time.sleep(2)
    print('in function running')
# function=wapper(function)
print(wapper(function))
function()
'''

'''
#带参数的装饰器
def wapper(fun):
    def timer(*args,**kwargs):
        start_time=time.time()
        fun(*args,**kwargs)
        stop_time=time.time()
        print('run time %s' %(stop_time-start_time))
    return timer
@wapper   #test1=wapper(test1)=>test1=timer
def test1():
    time.sleep(2)
    print('in the test1')
@wapper   #test2=wapper(test2(name,age))=>test2=timer
def test2(name,age):
    time.sleep(1)
    print('name:%s,age:%s'%(name,age))
test1()    #test1()=>timer()
test2('wz',20)  #test2('wz',20)=>timer('wz',20)
'''

'''
#带参数的装饰器
name='wz'
passwd='123'
def wapper(auth_type):
    def auth(f):
        def login(*args,**kwargs):
            if auth_type=='local':
                user = input("user_name:").strip()
                password = input('password:').strip()
                if(user==name and password==passwd):
                    print('login success!')
                    return f(*args,**kwargs)
                else:
                    print("login fail!")
            else :
                print('ldap')
        return login
    return auth
def index():
    print("in the index_page")
@wapper(auth_type='local')
def home():
    print('in the home page')
    return 'from home'
@wapper(auth_type='ldap')
def bbs():
    print('in the bbs page')
index()
print(home())  #返回home中return的内容
bbs()
'''

'''
#生成器  只有在调用的时候才会生成相应的数据,只记录当前的位置，省内存
l=[1,2,3,4,5]
print(l)
print(len([i*2 for i in range(10)]))
gener=(i*2 for i in range(10))
print(type(gener))
print(gener.__next__())
print(gener.__next__())

#斐波那契规律
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n+=1
fib(10)

#斐波那契规律--->换生成器
def fib_ger(max):
    n,a,b=0,0,1
    while n<max:
        yield b    #print(b)
        a,b=b,a+b
        n+=1
    return 'done'  #异常时候打印的信息

print(fib_ger(10))
f=fib_ger(10)
print(f.__next__())
for i in f:
    print i



#生产者消费者模型
def consume(name):
    print("%s开始吃包子"%name)
    while True:
        baozi=yield
        time.sleep(1)
        print('第%s包子,被[%s]吃了'%(baozi,name))

def product(name):
    print("开始做包子了")
    c = consume(name)
    c.__next__()
    for i in range(6):
        c.send('%d'%(i+1))
product('w')
'''

'''
#可迭代对象，可迭代对象可以通过iter()转化为迭代器
from collections import Iterable
print('列表是可迭代对象：%s'%isinstance([],Iterable))
print('元祖是可迭代对象：%s'%isinstance((),Iterable))
print('字典是可迭代对象：%s'%isinstance({},Iterable))
print('字符串是可迭代对象：%s'%isinstance('abc',Iterable))

#迭代器必须有next方法
from collections import Iterator
print('列表是迭代器：%s'%isinstance([],Iterator))
print('列表转化为迭代器：%s'%isinstance(iter([]),Iterator))
print(isinstance((i for i in range(10)),Iterator))
'''

print('describtion')


