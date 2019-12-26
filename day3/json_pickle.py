#/usr/bin/env python
import json
'''
dic={'name':'wz','age':20}
#转换成字符串： type(repr(dic)),type(str(dic)) =>序列化
f=open('json-file','w')
#f.write(repr(dic))             #学习json之前
#f.write(json.dumps(dic))相当于json.dump(dic,f)
f.write(json.dumps(dic))      #将写入文件的内容序列化，就是将内容转换成字符串
f.close()

'''

'''
#将字符串反序列化
f=open('json-file','r')
#print(eval(f.read())['name'])
dic1=json.loads(f.read())     #相当于json.load(f)
print('name:',dic1['name'],'age:',dic1['age'])
f.close()
'''

import pickle

def sayhi(name):
    print('name:',name)
'''
###存在函数的基础上序列化
dic2={'addr':'bj','phone':'123','fun':sayhi}
f=open('json-file','wb')
#pickle.dumps(dic2) 处理之后是二进制的,所以打开的文件必须是二进制
#print(pickle.dumps(dic2))
f.write(pickle.dumps(dic2))   #f.write(pickle.dumps(dic2))相当于pickle.dump(dic2,f)
f.close()
'''

'''
###存在函数的基础上反序列化
f1=open('json-file','rb')
data_1=pickle.loads(f1.read())   #data_1=pickle.loads(f1.read())相当于data_1=pickle.load(f)
print(data_1)
f1.close()
'''


#多次序列化和只能反序列化一次，最好一次dump一次load
'''
dic={'name':'wz','age':20}
f=open('json-file','w')
json.dump(dic,f)
dic['age']=23
json.dump(dic,f)
f.close()
'''

