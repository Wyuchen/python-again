#/usr/bin/env python
import os,sys,platform
if platform.system()=='Windows':
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0,BASE_DIR)

from modules import course,grade,student,teacher

print(sys.path)

class School(object):
    '学校类：学校名称，学校地址，课程，班级，教师'
    def __init__(self,school_name,school_addr):
        self.school_name=school_name
        self.school_addr=school_addr
        self.school_course={}
        self.school_grade={}
        self.school_teacher={}

    def create_course(self,course_name,course_price,course_time):
        '创建课程'
        course_obj=course.Course(course_name,course_price,course_time)
        self.school_course[course_name]=course_obj
    def show_course(self):
        '课程查询'
        print('显示课程信息'.center(50,'-',),'\n')
        for key in self.school_course:
            course_obj=self.school_course[key]
            print('课程名称：%s\n课程价格：%s\n课程周期：%s'%(course_obj.course_name,course_obj.course_price,course_obj.course_time))
            print('------------')

    def create_grade(self,grade_name,course_obj):
        '创建班级'
        grade_obj=grade.Grade(grade_name,course_obj)
        self.school_grade[grade_name]=grade_obj

    def show_grade(self):
        '显示班级'
        print('显示班级信息'.center(50, '-', ), '\n')
        for key in self.school_grade:
            grade_obj=self.school_grade[key]
            print('班级名称：%s\n关联的课程名称：%s'%(grade_obj.grade_name,grade_obj.grade_course.course_name))
            print('------------')

    def show_grade_course(self):
        '显示班级及关联课程信息'
        print('显示班级及关联课程信息'.center(50, '-', ), '\n')
        for key in self.school_grade:
            grade_obj = self.school_grade[key]
            print('班级名称：%s\n关联的课程名称：%s\n课程价格:%s\n课程周期：%s' % (grade_obj.grade_name, grade_obj.grade_course.course_name,grade_obj.grade_course.course_price,grade_obj.grade_course.course_time))
            print('------------')

    def create_teacher(self,teacher_name,teacher_age,teacher_salary,grade_name,grade_obj):
        '创建教师'
        teacher_obj=teacher.Teacher(teacher_name,teacher_age,teacher_salary)
        teacher_obj.teacher_add_grade(grade_name,grade_obj)
        self.school_teacher[teacher_name]=teacher_obj

    def update_teacher_grade(self,teacher_name,grade_name,grade_obj):
        '更新教师信息'
        teacher_obj=self.school_teacher[teacher_name]
        teacher_obj.teacher_add_grade(grade_name,grade_obj)

    def show_teacher(self):
        '显示教师信息'
        print('教师信息'.center(50,'-'),'\n')
        for key in self.school_teacher:
            teacher_obj=self.school_teacher[key]
            grade_list=[]
            for i in teacher_obj.teacher_grade:
                grade_list.append(i)
            print('教师姓名：%s\n教师年龄:%s\n教师薪资：%s\n关联班级：%s'%(teacher_obj.teacher_name,teacher_obj.teacher_age,teacher_obj.teacher_salary,grade_list))
            print('------------')

    def create_student(self,student_name,student_age,grade_choice):
        '注册学生'
        student_obj=student.Student(student_name,student_age) #学生实例
        grade_obj=self.school_grade[grade_choice]  #获取学生所注册班级的实例对象
        grade_obj.grade_student[student_name]=student_obj #班级实例里添加学生信息
        self.school_grade[grade_choice]=grade_obj #学校班级字典更新

    def show_teacher_grade_info(self,teacher_name):
        print('教师关联班级课程下的学生信息：\n'.center(10,'-'))
        teacher_obj=self.school_teacher[teacher_name]
        for key in teacher_obj.teacher_grade:
            grade_obj=self.school_grade[key]
            student_list=[]
            for key1 in grade_obj.grade_student:
                student_list.append(key1)
            print('教师姓名：%s\n班级名称：%s\n关联课程：%s\n学生信息：%s'%(teacher_name,grade_obj.grade_name,grade_obj.grade_course.course_name,student_list))

