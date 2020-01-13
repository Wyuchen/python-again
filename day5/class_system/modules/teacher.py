#/usr/bin/env python
'教师类：教师姓名，教师年龄，教师工资，包含一个teacher_add_grade方法'
class Teacher(object):
    def __init__(self,teacher_name,teacher_age,teacher_salary):
        self.teacher_name=teacher_name
        self.teacher_age=teacher_age
        self.teacher_salary=teacher_salary
        self.teacher_grade={}  #教师和班级关联
    def teacher_add_grade(self,grade_name,grade_obj):
        self.teacher_grade[grade_name]=grade_obj
