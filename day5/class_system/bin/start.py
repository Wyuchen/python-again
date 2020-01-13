#/usr/bin/env python
import os,sys,platform

if platform.system()=='Windows':
    BASE_DIR = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])
else:
    BASE_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

sys.path.insert(0,BASE_DIR)

from core import main
from conf import setting

if __name__=='__main__':
    m=main.Manage_center()
    m.run()
