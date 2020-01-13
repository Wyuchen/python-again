#/usr/bin/env python
import os,sys,shelve,platform
if platform.system()=='Windows':
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.insert(0,BASE_DIR)

from conf import setting
from modules import school
from core import main

class Manage_center(object):
    def __init__(self):
        pass
    def run(self):
        while True:
            print("欢迎进入CLASS_SYS系统\n1.学生视图\n2.教师视图\n3.管理视图\n4.退出CLASS_SYS系统\n")
            user_choice=input('请选择进入的视图编号：').strip()
            if user_choice =='1':
                print('欢迎进入学生视图\n')
                main.Manage_student()
            elif user_choice =='2':
                print('欢迎进入教师视图\n')
                main.Manage_teacher()
            elif user_choice =='3':
                print('欢迎进入管理视图\n')
                main.Manage_school()
            elif user_choice =='4':
                print('\033[34;1m感谢使用CLASS_SYS系统，您已退出\033[0m')
                exit()
            else:
                print('\033[31;1m请输入正确的视图编号\033[0m')

class Manage_school(object):
    '管理视图'
    def __init__(self):
        if os.path.exists(setting.school_db_file+'.db'):
            self.school_db=shelve.open(setting.school_db_file)
            self.run_school_manage()
            #self.school_db.close()
        else:
            print('初始化学校信息')
            self.iniialize_school()
            self.run_school_manage()
            #self.school_db.close()
    def iniialize_school(self): #初始化school信息
        self.school_db=shelve.open(setting.school_db_file)
        self.school_db['bj'] = school.School('bj','CN-bj')
        self.school_db['sh'] = school.School('sh', 'CN-sh')
    def run_school_manage(self):
        while True:
            for key in self.school_db:
                print('学校名称：',key)
            choice_school=input('请选择注册的学校名称：').strip()
            if choice_school in self.school_db:
                self.choice_school=choice_school
                self.school_obj=self.school_db[choice_school]
                while True:
                    print("欢迎来到%s校区\n1.增加课程-add_course\n"
                          "2.增加班级-add_grade\n"
                          "3.招聘教师-add_teacher\n"
                          "4.查看课程-check_course\n"
                          "5.查看班级-check_grade\n"
                          "6.查看教师-check_teacher"
                          "\n7.退出程序-exit\n " %choice_school)
                    user_view=input('请选择功能模块的编号:').strip()
                    if hasattr(self,user_view):
                         getattr(self,user_view)()
                    # if user_view=='1':
                    #      Manage_school().add_course()
                    # elif user_view=='2':
                    #     main.Manage_school().add_grade()
                    # elif user_view=='3':
                    #     main.Manage_school().add_teacher()
                    # elif user_view=='4':
                    #     self.school_obj.show_course()
                    # elif user_view=='5':
                    #     self.school_obj.show_grade()
                    # elif user_view=='6':
                    #     self.school_obj.show_teacher()
                    # elif user_view=='7':
                    #      self.school_db.close()
                    #      print('欢迎下次使用管理视图')
                    # else:
                    #     print('功能编码选择错误')
    def add_course(self):
        course_name=input('请输入增加的课程名称：').strip()
        course_price = input('请输入课程的价格：').strip()
        course_time = input('请输入课程周期：').strip()
        if course_name in self.school_obj.school_course:
            print('课程已存在')
            self.school_obj.create_course(course_name,course_price,course_time)
            print('课程更新完毕')
        else:
            self.school_obj.create_course(course_name, course_price, course_time)
            print('课程添加成功')
        self.school_db.update({self.choice_school:self.school_obj})

    def add_grade(self):
        grade_name=input('请输入班级名称：').strip()
        course_name=input('请输入课程名称:').strip()
        if grade_name not in self.school_obj.school_grade:
            if course_name in self.school_obj.school_course:
                course_obj=self.school_obj.school_course[course_name]
                self.school_obj.create_grade(grade_name,course_obj)
                self.school_db.update({self.choice_school:self.school_obj})
                print('班级创建成功')
            else:
                print('系统错误：班级关联课程不存在，请先创建课程')
        else:
            print('系统错误：班级已经存在')

    def add_teacher(self):
        teacher_name=input('请输入教师姓名：').strip()
        teacher_age = input('请输入教师年龄：').strip()
        teacher_salary = input('请输入教师工资：').strip()
        grade_name = input('请输入教师所在班级名称：').strip()
        if grade_name in self.school_obj.school_grade:
            grade_obj=self.school_obj.school_grade[grade_name]
            if teacher_name not in self.school_obj.school_teacher:
                self.school_obj.create_teacher(teacher_name,teacher_age,teacher_salary,grade_name,grade_obj)
                print('教师添加成功')
            else:
                self.school_obj.update_teacher_grade(teacher_name,grade_name,grade_obj)
                print('教师信息更新成功！')
            self.school_db.update({self.choice_school:self.school_obj})
        else:
            print('系统错误：班级关联班级不存在，请先创建班级')

    def check_course(self):
        self.school_obj.show_course()

    def check_grade(self):
        self.school_obj.show_grade()

    def check_teacher(self):
        self.school_obj.show_teacher()

    def exit(self):
        self.school_db.close()
        #sys.exit('欢迎下次使用学员管理系统')
        Manage_center().run()


class Manage_student(object):
    def __init__(self):
        if(os.path.exists(setting.school_db_file+'.db')):
            self.school_db=shelve.open(setting.school_db_file)
            self.run_manage()
            self.school_db.close()
        else:
            print('数据库文件不存在，请先创建学校')
            exit()
    def run_manage(self):
        for key in self.school_db:
            print('学校名称：%s' % key)
        choice_school=input('请选择注册的学校名称：').strip()
        if choice_school in self.school_db:
            self.choice_school=choice_school
            self.school_obj=self.school_db[choice_school]
            student_name=input('请输入学生名称：').strip()
            student_age=input('请输入学生年龄：').strip()
            self.school_obj.show_grade_course()
            grade_choice=input('请输入班级名称：').strip()
            if grade_choice in self.school_obj.school_grade:
                self.school_obj.create_student(student_name,student_age,grade_choice)
                self.school_db.update({self.choice_school:self.school_obj})
                print('学生注册成功')
            else:
                print('输入班级不存在')

        else:
            print('输入的学校不存在！')

class Manage_teacher(object):
    def __init__(self):
        if(os.path.exists(setting.school_db_file+'.db')):
            self.school_db=shelve.open(setting.school_db_file)
            self.run_manage()
            self.school_db.close()
        else:
            print('数据库文件不存在，请先创建学校')
            exit()
    def run_manage(self):
        for key in self.school_db:
            print('学校名称：%s' % key)
        choice_school = input('请选择注册的学校名称：').strip()
        if choice_school in self.school_db:
            self.choice_school=choice_school
            self.school_obj=self.school_db[choice_school]
            teacher_name=input("请输入老师姓名：").strip()
            while True:
                if teacher_name in self.school_obj.school_teacher:
                    print('欢迎进入教师视图：\n1.查看班级\n2.退出')
                    user_fun=input('请输入操作功能的编号：').strip()
                    if user_fun=='1':
                        self.school_obj.show_teacher_grade_info(teacher_name)
                    elif user_fun=='2':
                        Manage_center().run()
                    else:
                        print('输入操作功能的编号错误！')
                else:
                    print('教师不存在！！！！')
                    Manage_center().run()


