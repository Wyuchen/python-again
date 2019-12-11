# /usr/bin/env python
'''
存在的问题：
1.当输入登录成功后或者输入锁定的用户的时候程序没有结束---->解决使用exit（）退出程序
2.用户被重复写入到文件中   -已经解决
3.没有判断文件是否存在    解决-导入os模块
'''
import os
_username = 'admin'
_passwd = '123456'
count = 3
if os.path.exists("login_error_username.txt"):
    while count > 0:
        username = input("please input login_name:")
        passwd = input("please input login_passwd:")
        file_read = open('login_error_username.txt', 'r')
        for line in file_read.readlines():
            line = line.strip()
            if username != line:
                if _username == username and _passwd == passwd:
                    print("login success!")
                    exit()
            else:
                print("username is locked")
                exit()
        file_read.close()
        count -= 1
    else:
        file_write = open('login_error_username.txt', 'a+')
        for line_write in file_write.readlines():
            line_write = line_write.strip()
            if line_write == username:
                exit()
        else:
            file_write.write(username)
            file_write.write("\n")
        file_write.close()
        print('username：',username,"add black_list_name,you try too many time!")
else:
    print("黑名单文件不存在，创建文件中，请重新启动程序！")
    f = open("login_error_username.txt", 'a+')
    f.close()