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
print('打印当前目录：',os.getcwd())
#os.chdir('/home/wz/')  #切换目录
print(os.listdir('.'))     #显示当前目录的结构
print('文件详细信息:',os.stat('inner_modules.py'))  #查看文件详细信息print(
print('当前系统的目录分隔符：',os.sep)   #当前系统的目录分隔符
print('行分隔符：',os.linesep)   #行分隔符\n，win是\r\n
print('环境变量分隔符为',os.pathsep)
print('系统环境变量：',os.environ) #查看换将变量
print(os.name)      #查看当前系统是win-->(nt)还是linux-->(posix)
os.system('date')   #执行系统命令
print('绝对路径：',os.path.abspath('/usr/local/java/bin/java'))  #返回绝对路径
print(os.path.split('/usr/local/java/bin/java'))  #将目录分为文件和路径元祖
print('目录名：',os.path.dirname('/usr/local/java/bin/java'))
print('文件名：',os.path.basename('/usr/local/java/bin/java'))
print('pycharm是否存在',os.path.exists('/usr/local/pycharm'))
print('路径拼接：',os.path.join('/usr/local/pycharm','pycharm'))

import  sys
#打印参数列表 sys.argv
print('模块的搜索路径:',sys.path)   #模块的搜索路径
print('平台名称:',sys.platform)        #平台名称

import shutil
#shutil.copyfile('a','b')  #将a复制成b
#shutil.make_archive('包名','zip','需要压缩的目录')

import xml.etree.ElementTree as ET
tree=ET.parse('xml_code.xml')
root=tree.getroot()
print(root.tag)
#遍历xml文档
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text,i.attrib)
#只遍历rank
for node in root.iter('rank'):
    print('名称：',node.tag,'内容：',node.text,'属性：',node.attrib)

#修改xml
# for node1 in root.iter('year'):
#     new_year=int(node1.text)+1
#     node1.text=str(new_year)
#     node1.set('update_content','year_add')
# tree.write('xml_code.xml')

#删除xml
# for country in root.findall('country'):
#     year=int(country.find('year').text)
#     if year > 2011:
#         root.remove(country)
# tree.write('xml_code.xml')

#创建xml文件
new_xml=ET.Element('namelist')
info=ET.SubElement(new_xml,'info',attrib={"enrolled":'yes'})
age=ET.SubElement(info,'age',attrib={'checked':'no'})
sex=ET.SubElement(info,'sex')
name=ET.SubElement(info,'name')
name.text='wz'
age.text='23'
sex.text='F'
info2=ET.SubElement(new_xml,'info',attrib={"enrolled":'no'})
age=ET.SubElement(info2,'age')
sex=ET.SubElement(info2,'sex',attrib={'checked':'yes'})
name=ET.SubElement(info2,'name')
age.text='20'
sex.text='M'
name.text='wc'
et=ET.ElementTree(new_xml) #生成文档对象
et.write('info.xml',encoding='utf-8',xml_declaration=True)
ET.dump(new_xml) #打印生成的格式

#自行生成conf文件
import configparser
config=configparser.ConfigParser()

config['DEFAULT']={'ServerAliveInterval':'45',
                   'Compression':'yes',
                   'CompressionLevel':'9',
                   'ForwardX11':'yes'}
config['bitbucket.org']={}
config['bitbucket.org']['User']='hg'


# with open('example.conf','w')  as configfile:
#     config.write(configfile)
f=open('example.conf','w')
config.write(f)
f.close()

#读取conf文件中的内容
config_read=configparser.ConfigParser()
config_read.read('example.conf')     #读取文件

print(config_read.sections())      #打印除default的所有节点名称
print(config_read.default_section)  #打印default节点名称
print(config_read.defaults())       #打印default节点的内容

print('打印节点名称:',config_read['bitbucket.org'])
print('打印节点内容:',config_read['bitbucket.org']['User'])

#删除节点信息
#sec=config_read.remove_section('bitbucket.org')  #移除bitbucket.org
#config_read.remove_option('bitbucket.org','User')  #移除bitbucket.org下面的User
#config_read.write(open('example.conf','w'))   #重新写入到文件中

#添加节点
config_read.add_section('topsecret.server.com')
config_read.set('topsecret.server.com','Port','33060')
config_read.write(open('example.conf','w'))

import hashlib
m1=hashlib.md5()
m1.update(b'123456')
print(m1.hexdigest())