#/usr/bin/env python

# 定义函数式编程
def func():
    'function_test'
    print("in the function")
    return 0
x = func()


# 定义面向过程（没有返回值的函数）
def func1():
    'func1_function'
    print('in the function1')

y=func1()
print(x,y)

#定义有参数的函数
def func2(x,y=4):
    '定义有参数的函数，x和y代表形参，形参和实参一一对应'
    print(x,y)

func2(1,3)  #1和3代表实参，位置参数
func2(x=2,y=5) #关键字参数
func2(3,y=6)   #关键字参数必须在位置参数后面

#参数组--元祖
def func3(x,y=2,*args):
    print(x,y,args)

func3(1,2,7,8)
func3(1,2,*[1,2,3])   #将列表直接转换成元祖(1,2,3)
func3(1,2,[1,2,3])    #将整个列表作为元祖的一个值
#参数组---字典
def func4(**kwargs):
    print(kwargs)

func4(name='wz',age=18)
#参数组---元祖和字典，位置参数混合
def func5(x,*args,**kwargs):
    print(x,args,kwargs)

func5(1,2,3,4,name='wz',age=18,sex='k')

#局部变量
name='wz'
names=['wz','wyc','yc']
def func6():
     global name
     print(name)
     name='ceshi'    #不要再函数里面改全局变量，尤其是在外面没有定义该变量
     print(name)
     names.append('zz')
     print(names)
func6()
'''
递归函数，函数内部自己调用自己：
1.必须有明确的结束条件
2.每次进入更深一层递归，问题规模相比上一次递归都应有所减少
3.递归效率不高，可能会出现栈溢出
'''
def calc(num):
    print(num)
    if int(num / 2) > 0:
        calc(int(num / 2))
calc(10)

#高阶函数
def count(x,y,f):
    print(f(x)+f(y))

count(5,-3,abs)