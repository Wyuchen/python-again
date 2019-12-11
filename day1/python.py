#/usr/bin/env python
'''
#判断文件是否存在
import os
while True:

    if os.path.exists("login.txt"):
       pass
    else:
        f=open("login.txt",'a+')
        f.close()

print()
'''
'''
#用户交互
_name='wz'
_age=22
Name = input("please input your name:")
Age = int(input("please input your age:"))
#查看变量类型type()
print("type of age:",type(Age))
#多种格式化输出-%s代表str类型，%d代表int类型
print("格式化输出方法1\nyour name is %s" %Name,"\nyour age is: %d" %Age)
print("格式化输出方法2\nyour name:{name}\nyour age is {age}".format(name=Name,age=Age))
print("格式化输出方法3\nyour name:{0}\nyour age is {1}".format(Name,Age))
'''
'''
  #秘文输入密码，导入getpass，该方法在pycharm无法使用
  impot getpass  
  passwd=getpass.getpass('passwd:')
'''
'''
#条件判断
if _name==Name and _age==Age:
    print("hello {name}".format(name=Name))
else:
    print("Invalid name or age")
'''

'''
#元祖使用
t1=(1,)
t2=(1)
t=(1,2,3,1)
print(t,t.index(3),t.count(1),type(t1),type(t2))
'''
'''
import copy
#列表使用
l=['wz','yc','xw','wz',[1,2,3]]
l.append('wyc')        #在列表最后添加元素
l.count('wz')          #查看列表中元素出现的次数
l1=l.copy()            #浅复制
#l1=copy.deepcopy(l)   #深复制
l[1]='wyc'             #修改一层列表数据之后列表的变化
l[4][1]=3
l.extend([4])          #将新列表元素添加到类表中
l.index('wyc')         #出现元素的下标
l.insert(1,'yc')       #在下标为1的地方添加元素
l.pop()                #移除列表最后一个元素并返回该值
l.reverse()            #列表翻转，直接就翻转了，无需在复制给其他
l.remove([1,3,3])      #移除元素
l.sort()               #排序，针对同一类型
l.clear()              #清空列表

###字符串的使用
var='\thello-WorlD'    #字符出现的次数
var.center(20,'*')     #字符居中，共20字符，其他字符用*补充
var.capitalize()       #首字母大写
var.casefold()         #将字符串中的所有大写字母变成小写字母,不仅仅是针对ASICC码
var.encode()           #转为二进制格式
var.expandtabs(5)      #将tab的4个空格换成5个空格
var.endswith('D')      #判断字符是否是以D结束的，返回True或者False
'secret:{passwd}'.format(passwd='123')        #格式化输出
'secret:{passwd}'.format_map({'passwd':456})  #使用字典格式化输出
var.find('D')           #查找字符的位置
var.index('h')          #查看字符的下标
'-'.join(var)           #使用-分割字符串
var.rjust(20,"*")       #右对齐不够的用*补充
var.ljust(20,"*")       #左对齐不够用*补充
var.lower()             #转为小写字母，针对ASICC码
var.lstrip()            #删除左边的空格和制表符
var.partition('l')      #将字符串使用给定的字符进行分割称三部分
var.rfind('l')          #从右边开始出现的第一个
var.rstrip()            #删除右边的空格和制表符
var.rindex('l')         #从右边开始出现的第一个
var.replace('D','d')    #替换字符
var.strip()             #删除两边的空格和制表符
var.swapcase()          #大小写转换
var.startswith('\t')    #判断是否以给定字符开头，返回True或者False
var.split('-')          #以给定字符分割转换成列表
var.upper()             #转换成大写字母
var.zfill(20)           #在字符前面使用0将长度增加到20

####字典的使用
info={'stu_name2':'wz','stu_name':'yc','stu_name1':'wyc'}
info['stu_name1']='xw'         #修改内容
info['stu_name3']='ww'         #出入一条记录
info.get('stu_name')      #若key存在返回value，不存在返回None
info.keys()               #字典中的key值
info.values()             #字典中的value值
info1=info.copy()         #浅复制
info.setdefault('stu_name4','www')  #设置字典的默认值
info.update({'stu_name5':'wz','sex':'M'})       #将字典合并，若有一样的key更新
del info['stu_name']           #删除记录
info.pop('stu_name1')
info.popitem()                 #随机删除
info.items()                #转换成列表
info.clear()             #清空字典成为空字典
for i in info:
    print(i,info[i])
print('\n')

for k,v in info.items():
    print(k,v)
'''

#集合也是无序的：1）去重 2）关系测试
from collections import Counter
l=[1,2,2,3,4,3,5,1]
l1=[5,6,7]
#print(list.intersection(l1))   #交集
#print(l.union(l1))             #并集
#print(l.difference(l1))        #差集
dic=dict(Counter(l))
set1=set(l)
print(dic)
print(set1,type(set1))


