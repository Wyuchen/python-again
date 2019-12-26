#/usr/bin/env python

#内置模块
import time,datetime
print(time.time())                          #时间戳
print(time.gmtime())
print(time.gmtime(time.time()))            #将时间戳转换成utc时间(struct_time)
print(time.localtime())
print(time.localtime(time.time()))         #将时间戳转换成(utc+8)时间(struct_time)
print(time.localtime().tm_year)            #获取年
print(time.mktime(time.localtime()))       #转换成时间戳
print(time.strftime("%Y-%m-%d %H:%M:%S"))  #时间格式化输出
print(time.strptime('2019-12-26 21:47:05',"%Y-%m-%d %H:%M:%S"))  #将格式化输出转换成struct_time
print(time.asctime())
print(time.asctime(time.localtime()))  #将struct_time元祖格式转换成字符串
print(time.ctime(time.time()))         #将时间戳转换成字符串

print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(+3))   #当前时间加3天
print(datetime.datetime.now()+datetime.timedelta(-3))   #当前时间减3天
print(datetime.datetime.now()+datetime.timedelta(hours=-3,weeks=-2,seconds=+10,minutes=-5,days=+3))
print(datetime.datetime.now().replace(year=2018,month=8,day=8,hour=8,minute=8,second=8))

import random
print(random.random())      #随机数0-1（包括小数）
print(random.uniform(1,10)) #随机数1-10（包括小数）
print(random.randint(1,5))  #随机数1-5整数
print(random.randrange(1,3))  #随机数1-3整数
print(random.choice('asdfghjk')) #随机来自于后面的值，字符串，元祖列表等
print(random.sample('asdfgh',2))  #随机取出2个字符
l=[1,2,3,4,5]
random.shuffle(l)
print(l)    #随机打乱列表

#验证码=数字+大写/小写字母
print(''.join(random.sample('qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM',4)))
#验证码=数字+大写字母
var=''
for i in range(0,4):
    num=random.randrange(0,4)
    if i==num:
        random_tmp=chr(random.randint(65,90))
    else:
        random_tmp=random.randint(1,9)
    var+=str(random_tmp)
print(var)

#os模块
import os