#/usr/bin/env python

'''
#面向对象编程
1.只要是对象，就肯定属于某种品类，只要是对象就会有属性
2.类class：一个类即是对一类拥有相同属相的对象的抽象。
3.对象object：一个对象即时一个类实例化后的实例，一个类可以实例化多个对象，
            每个对象可以拥有不同的属性
4.封装：在类中对数据的赋值、内部调用对外部用户是透明的，
       这使类变成了一个胶囊或容器，里面包含着类的数据和方法
5.继承：一个类可以派生出子类，在这个父类里定义的属性、方法自动被子类继承

6.多态：一个基类中派生出了不同的子类，且每个子类在继承了同样的方法名的同时又对父类的方法做了不同的实现，
       这就是同一种事物表现出的多种形态
7.类变量和实例变量
8.析构函数：在实例释放或者销毁的时候自动执行的，通常用于做一些收尾工作，比如：关闭数据库连接，文件关闭等
9.私有属性：在属性前面添加__,如果想访问私有方法必须在写一个函数获取私有方法
'''
'''
class Role:
    n=123  #类变量
    def __init__(self,name,age,life_value=100):  #构造函数，类的初始化
        self.name=name  #实例变量,作用域是实例本身(静态属性)
        self.age=age
        self.__life_value=life_value   #私有属性
    def buy_gun(self):      #类的方法
        print('%s buy gun' % self.name)
    def show_life(self):  #通过函数访问私有属性
        print('life_value:',self.__life_value)
    def __del__(self):  #析构函数
        print('%s is exit game'%self.name)

print(Role,Role.n)
r1=Role('xx',20,'98')
print('实例变量age查询:',r1.age)
r1.age=30
print('实例变量age修改:',r1.age)
r1.money=200    #外面实例化
print('实例变量money增加:',r1.money)
# del r1.money
# print('实例变量删除:',r1.money)
#修改类变量
r1.n=234
print('修改类变量:',Role.n,r1.n)
#私有属性查询
r1.show_life()
'''
#继承实例
#class Person：   #经典类写法
class Person(object):   #新式类写法
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.friends=[]
    def eat(self):
        print('%s eat food' %self.name)

class Relation(object):
    def makeFriend(self,obj):
        print('%s have a friend %s'%(self.name,obj.name))
        self.friends.append(obj)
        #self.friends.append(obj.name)  #此处如果写成obj.name，则会写死name，而不会根据name的变化而变化
class Man(Person):
    def __init__(self,name,age,money):    #重构构造函数
        Person.__init__(self,name,age)    #经典类写法
        #super(Man, self).__init__(name,age)  #新式类写法
        self.money=money

    def smarking(self):
        print("%s is smarking"%self.name)

    def eat(self):  #重构父类方法
        Person.eat(self)
        print('man is eating')

class Woman(Relation,Person):  #多继承：Person和Relation
    def have_baby(self):
        print('%s have baby' %self.name)

m1=Man('wz',20,10)
print('name:',m1.name,'age:',m1.age,'money:',m1.money)
m1.eat()
m1.smarking()

w1=Woman('xx',22)
print('woman_name:',w1.name,'woman_age:',w1.age)
w1.have_baby()
w1.makeFriend(m1)
print('friend_name:',w1.friends[0].name)
#m1.name='ww'                      #对应上面obj.name，修改name的值，返回结果没有变化
#print('friend_name:',w1.friends[0])

'''
#多继承查找:广度优先(默认优先)，深度优先
广度优先：D继承B和C，先查B的构造函数，如果B没有再查C，C没有再找A的构造方法--->python3
深度优先：D继承B和C，先查B的构造函数，如果B没有再查A，A没有再找C的构造方法 --->python2
python2--->经典类按照深度优先继承的，新式类是按广度优先继承
python3--->经典类和新式类都是按照广度优先继承的
'''

class A:
    def __init__(self):
        print("a")
class B(A):
    pass
    # def __init__(self):
    #     print("b")
class C(A):
    def __init__(self):
        print("c")
class D(B,C):
    pass

d=D()