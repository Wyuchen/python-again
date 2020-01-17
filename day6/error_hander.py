#/usr/bin/env python
#异常处理
name=[1,2]
dic={'name':'wz','age':20}
class DatabaseException(Exception):
    '自定义异常'
    def __init__(self,msg):
        self.msg=msg
    # def __str__(self):     #可不用自行定义，默认__str__会返回报错信息
    #     return self.msg

try:
    raise DatabaseException('数据库异常')
    name[3]
    dic['dd111']

except (IndexError,KeyError) as e:  #指明错误的名称
    print('报错信息：',e)
except DatabaseException as e:
    print(e)
except Exception as e:              #用于抓取其他未知的错误
    print('未知报错信息：',e)
else:                               #当没有任何错误的时候执行else后面的语句
    print('没有任何错误,一切正常')
finally:
    print('不管有没有错，都执行finally后面的语句')

print('''
常用异常类型：
AttributeError 试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
IOError 输入/输出异常；基本上是无法打开文件
ImportError 无法引入模块或包；基本上是路径问题或名称错误
IndentationError 语法错误(的子类)；代码没有正确对齐----->无法被抓住
IndexError 下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError 试图访问字典里不存在的键
KeyboardInterrupt Ctrl+C被按下
NameError 使用一个还未被赋予对象的变量
SyntaxError Python代码非法,代码不能编译
TypeError 传入对象类型与要求的不符合
UnboundLocalError 试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，
导致你以为正在访问它
ValueError 传入一个调用者不期望的值，即使值的类型是正确的
''')