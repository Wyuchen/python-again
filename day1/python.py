#/usr/bin/env python
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
  #秘文输入密码，导入getpass，该方法在pycharm无法使用
  impot getpass  
  passwd=getpass.getpass('passwd:')
'''
#条件判断
if _name==Name and _age==Age:
    print("hello {name}".format(name=Name))
else:
    print("Invalid name or age")

