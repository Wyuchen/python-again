#python3  

##Pycharm 快捷键汇总  

1.代码格式化：alt+crtl+l  
2.单行注释：ctrl+/   
3.整体向右移动代码：鼠标选中+tab      
4.整体向左移动代码：鼠标选中+(shift+tab)  
5.查看源代码：鼠标选中+ctrl
   

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
3)ValueError  列表不存在  
4)KeyEroor  字典key不存在


##day2中学习内容：  
***1.模块的认识***  
1)sys.path  查找导入模块的目录顺序，文件名称不要和模块名称一样  
2)sys.argv 返回脚本的绝对路径  
3)os.system('date') 执行shell中的命令，返回值是0，如果要返回命令结果使用os.popen('date').read()  
4)os.mkdir('文件名') 创建目录，os.rmdir('文件名') 删除文件  

***2.string和bytes之间的转换***  
string--->encode---->bytes  
bytes---->decode---->string  
'北京'.encode(encoding='utf-8').decode(encoding='utf-8')  

***3.元祖的使用***  
1)元祖的定义：t=()  空元祖  
2)单元素的tuple： t1=('w',)如果没有逗号，t1为整型  
3）tuple的方法：  
t1.index()   ---->返回元祖中值的下标  
t1.Count()   ---->返回元祖中元素在元祖中出现的次数  

***4.列表的使用***  
```
import copy  
l=['wz','yc','xw','wz',[1,2,3]]  
l.append('wyc')        #在列表最后添加元素  
l.count('wz')          #查看列表中元素出现的次数  
l1=l.copy()            #浅复制  
l1=copy.deepcopy(l)    #深复制  
l[1]='wyc'             #修改一层列表数据之后列表的变化  
l[4][1]=3              #赋值
l.extend([4])          #将新列表元素添加到类表中  
l.index('wyc')         #出现元素的下标  
l.insert(1,'yc')       #在下标为1的地方添加元素  
l.pop()                #移除列表最后一个元素并返回该值  
l.reverse()            #列表翻转，直接就翻转了，无需在复制给其他  
l.remove([1,3,3])      #移除元素  
l.sort()               #排序，针对同一类型  
l.clear()              #清空列表    
```
***5.字符串*** 
```   
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
```
***6.字典使用*** ---> 字典是无序的
```
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
``` 

***7.***



  
