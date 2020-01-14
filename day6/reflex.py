#/usr/bin/env python

#反射的应用

def bulk(self):
    print('%s is yelling'%self.name)

class Dog(object):
    def __init__(self,name):
        self.name=name

    def eating(self,food):
        print('%s is eating %s'%(self.name,food))

d =Dog('旺旺')
choice=input('请输入需要使用的方法：').strip()

print('判断obj对象里是否存在字符串为func_str的方法-hasattr(obj,func_str)：',hasattr(d,'eating'))

if hasattr(d,choice):
    getattr(d,choice)('gutou')
else:
    # setattr(d,choice,None)
    # print('setattr-在obj类中设置对象或者方法：',getattr(d,choice))
    setattr(d,choice,bulk)
    getattr(d,choice)(d)
    #将方法装订到类中，需要将self传到bulk中，此时
    # getattr(d,choice)获取到的方法名是choice对应字符换的方法而不是bulk

print('getattr(obj,func_str)根据字符func_str串获取obj对象中对应的方法的内存地址：',getattr(d,'eating'))
