#/usr/bin/env python
'''
#file—operation
file=open('file.txt','r+')
print(file.readline())
for line in file.readlines():
    print(line)
print(file.tell())
file.seek(0)
print(file.tell())
for i in file:
    print(i.strip())
print(file.tell())
print(file.writable())
print(file.readable())
file.seek(2)
print(file.tell())
file.write('hello world')
file.seek(0)
print(file.tell())
print(file.read())
print(file.seekable())
print(file.closed)
print(file.encoding)
print(file.errors)
print(file.fileno())
print(file.isatty())
print(file.mode)
print(file.name)
file.truncate(3)
file.writelines("hahahh")
file.close()

#进度条展示
import sys,time
for i in range(10):
    sys.stdout.write("#")
    sys.stdout.flush()
    time.sleep(1)
'''



# import python

'''
#简单测试
msg='北京'
print('北京'.encode(encoding='utf-8').decode(encoding='utf-8'))
t1=(1)
t=(1,2,1)
print(t,type(t1),t.count(1),t.index(2))
l=[1,2,3,4]
'''

'''import sys
import os
print(sys.path)
print(sys.argv)

#date=os.system('date')

print(os.popen('date').read())
#os.mkdir('day2')
#os.rmdir('day2')
'''


'''
var=input('input:')
l=[]
f=open("login_error_username.txt",'a+')
for line in f.readlines():
    line=line.strip()
    l.append(line)
if var not in l:
    f.write(var)
    f.write('\n')
f.close()
#print(l)
'''

"""
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
  if num ==0:
      confire=input("can you three try again:")
      if confire !="N":
          num=3
"""
# else:
#     print("you have tried too many times.")

'''
for i in range(3):
    Age = int(input("Age:"))
    if Age == age:
        print("ok")
        break
    elif Age > age:
        print("older")
    else:
        print("yonger")
else:
    print("you have tried too many times.")
'''