#/usr/bin/env python
'班级类，包括班级名称，课程，学生'
class Grade(object):
    def __init__(self,grade_name,course_obj):
        self.grade_name=grade_name
        self.grade_course=course_obj    #班级关联课程类
        self.grade_student={}     #学生字典
