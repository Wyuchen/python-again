#/usr/bin/env python

#静态方法
print('静态方法开始'.center(50,'-'))
class Dog(object):
    def __init__(self,name):
        self.name=name

    def eating(self,food):
        print('%s is eating %s'%(self.name,food))
    @staticmethod #静态方法和类没有什么关系(不会传入self等参数),相当于单纯的函数
    def eating2():
        print('旺旺2 is eating angthing')
d=Dog('旺旺')
d.eating('骨头')

d.eating2()

print('静态方法结束'.center(50,'-'),'\n')

#类方法
print('类方法开始'.center(50,'-'))
class Dog(object):
    name='旺旺2'
    def __init__(self,name):
        self.name=name

    def eating(self,food):
        print('%s is eating %s'%(self.name,food))
    @classmethod  #只能访问类变量不能访问实例变量
    def eating2(self):
        print('%s is eating angthing'%self.name)
d=Dog('旺旺')
d.eating('骨头')

d.eating2()
print('类方法结束'.center(50,'-'),'\n')

#属性方法
print('属性方法开始'.center(50,'-'))
class Dog(object):
    def __init__(self,name):
        self.name=name
    def eating(self,food):
        print('%s is eating %s'%(self.name,food))
    @property  #属相方法把一个方法变成一个静态属性
    def eating2(self):
        print('%s is eating angthing'%self.name)

    @eating2.setter
    def eating2(self,food):
        print('%s is eating %s'%(self.name,food))

    @eating2.deleter
    def eating2(self):
         print('eating2 is deleted!')

d=Dog('旺旺')
d.eating('骨头')
d.eating2
d.eating2='骨头2'
del d.eating2
print('属性方法结束'.center(50,'-'),'\n')


#类的特殊成员方法
print('类的特殊成员方法'.center(50,'-'))
class Dog(object):
    'Dog类说明'
    def __init__(self,name):
        self.name=name

    def eating(self,food):
        print('%s is eating %s'%(self.name,food))

    def __call__(self, *args, **kwargs):
        print('running:',*args, **kwargs)

    def __str__(self):
        return self.name

    def __getitem__(self, item):
        print("__getitem__",item)

    def __setitem__(self, key, value):
        print('__setitem__',key,value)

    def __delitem__(self, key):
        print('__delitem__',key)


print('1.__doc__(类描述信息)：%s' % Dog.__doc__)
print('2.__module__(显示当前模块来自哪里,从哪导入的)：%s'%Dog.__module__)
print('3.__class__(当前操作的对象类):%s'%Dog.__class__)
print('4.__init__(构造方法)')
print('5.__del__(析构方法，当对象在内存中被释放时，自动触发执行)')
d=Dog('旺旺')
d('112','23223')
print('6.__call__(对象后面加括号，触发执行)')
print('7.__dict__(查看类中的所有成员):%s'% Dog.__dict__)
print('8.__dict__(查看对象中的所有成员):',d.__dict__)
print('9.__str__(在打印对象时，默认输出该方法的返回值):%s' %d)
print('10.__getitem__和__setitem__和__delitem__')
d1=Dog('花花')
d1['name']          #自动触发执行 __getitem__
d1['name']='huahua' #自动触发执行 __setitem__
del d1['name']
print('11.d对象是来自：%s,Dog对象是来自：%s'%(type(d),type(Dog)))
print('''Dog类的构造方法和eating方法的另类写法:
def __init__(self,name):
    self.name=name

def eating(self, food):
    print('%s is eating %s' % (self.name, food))

Dog1=type('Dog1',(object,),{'__init__':__init__,'eating':eating})
#type()中三个参数：类名，当前类的基类，类的方法或者属性
d2=Dog1('dingdang')
d2.eating('rourou')
''')
print('类的特殊成员方法结束'.center(50,'-'))
