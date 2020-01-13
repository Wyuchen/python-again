#/usr/bin/env python
'''
class School(object):
    def __init__(self,addrss,name,course_obj):
        self.name=name
        self.address=addrss
        self.course=course_obj
    def Add_course(self,obj):
        self.course.append(obj.name)
        print('course_addr:%s,course_name:%s'%(self.address,obj.name))


class Course(object):
    def __init__(self,name,price,course_time):
        self.name=name
        self.price=price
        self.course_time=course_time

py=Course('python','1000','18')

bj=School('beijing','北京老男孩教育中心')
bj.Add_course(py)
'''
'''
#定义学校类
import pickle,json
class School(object):
    def __init__(self,name):
        self.name=name

    def  create_course(self): #创建课程
        print('欢迎创建课程'.center(50,'-'),'\n')
        course_name=input("请输入课程名称：").strip()
        course_price=input("请输入课程价格：").strip()
        course_time=input('请输入课程周期：').strip()
        course_obj=Course(course_name,course_price,course_time) #课程实例化
        print('课程创建成功'.center(50,'-'),'\n')
        courses['course_name']=course_obj
        course_dic={'课程名称':course_name,'课程价格':course_price,'课程周期':course_time}
        f_course=open('course_info','wb')
        f_course.write(pickle.dumps(course_dic))
        course_obj.show_course_info()
        #control_view()  #从新调用选择功能函数

    def create_grade(self):
        print('欢迎创建班级'.center(50,'-'),'\n')
        grade_name=input('请输入班级名称：').strip()
        grade_time=input('请输入班级周期：').strip()
        grade_obj=Grade(grade_name,grade_time)  #班级实例化
        print('班级创建成功'.center(50,'-'))
        grades[grade_name]=grade_obj
        grade_dic={'班级名称':grade_name,'班级周期':grade_time}
        grade_obj.show_grade_info()
        f_grade=open('grade_info','wb')
        f_grade.write(pickle.dumps(grade_dic))
        #control_view()#从新调用选择功能函数

    def create_teacher(self):
        print('欢迎录入教师信息'.center(50,'-'),'\n')
        #print(教师所教课程：%s'
        teacher_name=input('请输入教师姓名：').strip()
        teacher_sex = input('请输入教师性别：').strip()
        teacher_age = input('请输入教师年龄：').strip()
        teacher_school = input('请输入教师所在学校：').strip()
        teacher_grade = input('请输入教师所教班级：').strip()
        teacher_course = input('请输入教师所教课程：').strip()
        teacher_obj=Teacher(teacher_name,teacher_sex,teacher_age,teacher_school,teacher_grade,teacher_course)
        print('录入教师信息成功'.center(50,'-'),'\n')
        teachers['teacher_name']=teacher_obj
        teacher_dic={'教师姓名':teacher_name,'教师性别':teacher_sex,'教师年龄':teacher_age,'教师所在学校':teacher_school,'教师所教班级':teacher_grade,'教师所教课程':teacher_course}
        f_teacher=open('teacher_info','wb')
        f_teacher.write(pickle.dumps(teacher_dic))
        teacher_obj.show_teacher_info()
        #control_view()


#定义课程类---属性：course_name(课程名称),course_price(课程价格),course_time(课程周期)
#        ---方法：show_course_info
class Course(object):
    def __init__(self,course_name,course_price,course_time):
        self.course_name=course_name
        self.course_price=course_price
        self.course_time=course_time
    def show_course_info(self):
        print('课程名称：%s\n课程价格%s\n课程周期%s'%(self.course_name,self.course_price,self.course_time))

#定义班级类---属性--grade_name(班级名称),grade_time(班级周期)
#        ---方法：show_grade_info
class Grade(object):
    def __init__(self,grade_name,grade_time):
        self.grade_name=grade_name
        self.grade_time=grade_time
    def show_grade_info(self):
        print('班级名称：%s\n班级周期：%s'%(self.grade_name,self.grade_time))

class Person(object):
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
#定义教师类
class Teacher(Person):
    def __init__(self,name,sex,age,teacher_school,teacher_grade,teacher_course):
        super(Teacher, self).__init__(name,sex,age)
        self.teacher_school=teacher_school
        self.teacher_grade=teacher_grade
        self.teacher_course=teacher_course
    def show_teacher_info(self):
        print('教师姓名：%s\n性别：%s\n年龄：%s\n教师所在学校：%s\n教师所在班级：%s\n教师所教课程：%s'%(self.name,self.sex,self.age,self.teacher_school,self.teacher_grade,self.teacher_course))

# t=Teacher('wz','M',20,'bj','linux','linux')
# t.show_teacher_info()
#定义学生类
class Student(Person):
    def __init__(self,name,sex,age,student_school,student_course,student_id,student_coursetime):
        super(Student, self).__init__(name,sex,age)
        self.student_school=student_school
        self.student_id=student_id
        self.student_course=student_course
        self.student_coursetime = student_coursetime
    def show_teacher_info(self):
        print('学生姓名：%s\n性别：%s\n年龄：%s\n学生所在学校：%s\n学生学号：%s\n学生报名课程：%s\n课程学习周期：%s'%(self.name,self.sex,self.age,self.student_school,self.student_id,self.student_course,self.student_coursetime))

def Create_student():
    print('请录入学生信息'.center(50,'-'),'\n')
    student_name = input('请输入学生姓名：').strip()
    student_sex = input('请输入学生性别：').strip()
    student_age = input('请输入学生年龄：').strip()
    student_school = input('请输入学生所在学校：').strip()
    student_id = input('请输入学生学号：').strip()
    student_course = input('请输入学生报名课程：').strip()
    student_coursetime=input('请输入学生课程学习周期：').strip()
    student_obj=Student(student_name,student_sex,student_age,student_school,student_id,student_course,student_coursetime)
    print('学生信息录入成功')
    students['student_name']=student_obj
    student_dic={'学生姓名':student_name,'学生性别':student_sex,
                 '学生年龄':student_age,'学生所在学校':student_school,
                 '学生学号':student_id,'学生报名课程':student_course,'学生课程学习周期':student_coursetime}
    student_obj.show_teacher_info()
    f_student=open('student_info','a')
    f_student.write('\n',json.dumps(student_dic))

def student_view():
    print('\033[1;31m以下学生视图：\n\033[0m1.注册个人信息\n2.选择班级\n3.缴费\n4.返回上一级目录')
    student_choice=int(input('请选择需要操作的内容编号：').strip())
    if student_choice ==1:
        Create_student()
    elif student_choice==2:
        pass
    elif student_choice==3:
        pass
    elif student_choice==4:
        select_fun()
    else:
        exit()


def select_school():
    global  school_id
    print('1.工大\n2.交大\n0.退出\n')
    school_choice=int(input('请选择学校前的编号：').strip())
    if school_choice ==1:
        school_id=school1
        print('您选择的学校是%s'% "\033[1;31m",school_id.name,"\033[0m")
    elif school_choice==2:
        school_id = school2
        print('您选择的学校是%s' % "\033[1;31m",school_id.name,"\033[0m")
    elif school_choice==0:
        exit()
    else:
        print('输入学校编号错误，请重现输入！')
        select_school()
def select_fun():
    print('1.学员视图\n2.教师视图\n3.管理视图\n4.返回上一级\n0.退出程序')
    fun_id=int(input('请选择功能界面：').strip())
    if fun_id==1:
        student_view()
       #pass
    elif fun_id==2:
        #teacher_view()
       pass
    elif fun_id==3:
        #control_view()
        pass
    elif fun_id==4:
        select_school()
    elif fun_id==0:
        exit()
    else:
        print('功能界面编号选择错误，请重新选择')
        select_fun()



def main():
    while True:
        select_school()
        while True:
            select_fun()

if __name__=='__main__':
   grades={}
   courses={}
   teachers={}
   students={}
   school1=School('工大')
   school2=School('交大')
   main()
'''

class A():
    name='python'
    def func(self):
        print('python-func')


if hasattr(A,'name'):
    print(getattr(A,'name'))

if hasattr(A(),'func'):
    getattr(A(),'func')()

import shelve
f=shelve.open('shelve')
f['stu_info']={'name':'egon','age':18,'hobby':['piao','smoking','drinking']}
print(f['stu_info'])
f.close()


