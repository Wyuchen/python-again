#python3  

##Pycharm 快捷键汇总  

1.代码格式化：alt+crtl+l  
2.单行注释：ctrl+/  

##day1中学习内容：  

**1.注释的使用:**  
  1）单行注释使用#号  
  2）多行注释使用成对的三个单引号或者双引号
    
**2.变量:**  
  1）变量名是由字母、数字、下划线构成  
  2）变量的首位不可以为数字  
  3）变量名称过长的时候尽可能使用下划线分开，或者采用驼峰命名  
  4）取变量名不要和关键字相同  
  5）变量名称区分大小写  
  
**3.编码的发展过程**   
  ASCII(8位,共255个,只是用了127个)--->gb2312--->gbk--->gb1803--->unicode(16位-2**16)--->utf8(可缺省的unicode编码)  

**4.用户交互式程序和格式化输出**   
  1)input()   
  2)格式化输出(%s代表str类型，%d代表int类型)：  
  print("name is %s" %(Name))  
  print("name:{name}".format(name=Name))  
  print("name:{0}".format(Name))  
  3)密码隐藏(pycharm中无法实现，只能在其他尝试)：  
  ```
  impot getpass  
  passwd=getpass.getpass('passwd:')
  ```
***5.条件判断、循环语句***
```
注意此处while和else的意义
age=30
num=3
while num>0:
  Age=int(input("Age:"))
  if Age == age:
      print("ok")
      break
  elif Age > age:
      print("older")
  else:
      print("yonger")
  num -= 1
else:
    print("you have tried too many times.")
```
***6.错误代码汇总***  
1)IndentationError 缩进错误  
2)TypeError   类型错误

  
