#/usr/bin/env python
import os,sys,platform

if platform.system()=='Windows':
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
    database_path=os.path.join(BASE_DIR,"database_info")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    database_path = os.path.join(BASE_DIR, "database_info")


school_db_file=os.path.join(database_path,'school')
# teacher_db_file=os.path.join(database_path,'teacher')
# student_db_file=os.path.join(database_path,'student')
# grade_db_file=os.path.join(database_path,'grade')
# crouse_db_file=os.path.join(database_path,'crouse')
