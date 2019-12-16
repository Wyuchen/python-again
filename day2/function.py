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

#参数组
def func3(x,y=2,*args):
    print(x,y,args)

func3(1,2,7,8)
func3(1,2,*[1,2,3])   #将列表直接转换成元祖(1,2,3)
func3(1,2,[1,2,3])    #将整个列表作为元祖的一个值
