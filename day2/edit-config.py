#/usr/bin/env python
#存在一个问题就是在删除的时候只有推出程序才会生成文件 ----bug







'''
########search
search_contant=input("please input search content:")
file_search=open('config','r')
for line in file_search:
    line=line.strip()
    if (search_contant in line) and (line.startswith('backend')):
        for server_line in file_search.readlines():
            if ('server' in server_line):
                print(server_line.strip())
'''
'''
############add_contest
file_add=open('config','r+')
arg = {
            'bakend': 'www.taobao.org',
            'record':{
                'server': '100.1.7.3',
                'weight': 10,
                'maxconn': 20
            }
        }
add_contant=arg['bakend'].strip()
for line in file_add.readlines():
    line=line.strip()
    if add_contant  in line:
        print(arg['bakend'].strip(), 'is exist!!!')
        break
else:
    file_add.write('\n')
    file_add.write('bakend  ')
    file_add.write(str(arg['bakend']))
    file_add.write('\n       ')
    for k, v in arg['record'].items():
        file_add.write(k.rjust(len(k) + 1, ' '))
        file_add.write(str(arg['record'][k]).rjust(len(str(arg['record'][k])) + 1, ' '))
    file_add.close()
'''
'''
####delete-content
file_delete=open('config1','r+')
arg = {'backend': 'www.taobao.org', 'record': {'server': '100.1.7.3', 'weight': 10, 'maxconn': 20}}
#arg=eval(input('please input add content:'))
for line_delete in file_delete:
    if  arg['backend']  in line_delete.strip() and line_delete.startswith('backend'):
        pass
    elif arg['record']['server'] in line_delete.strip() and str(arg['record']['weight']) in line_delete.strip() and str(arg['record']['maxconn']) in line_delete.strip():
    #elif (arg['record']['server'] in line_delete.strip()) and (arg['record']['weight'] in line_delete.strip()):
        pass
    else:
        file_delete_new=open('config2','a+')
        file_delete_new.write(line_delete)
        #print(line_delete)
file_delete.close()
'''




while True:
    choose=input("input operation num(1.查看,2.增加，3.删除,4.退出程序):")
    file_search = open('config', 'r+')
    if choose=='1' :
        search_contant = input("please input search content:").strip()
        for line in file_search:
             line = line.strip()
             if (search_contant in line) and (line.startswith('backend')):
                 for server_line in file_search.readlines():
                     if ('server' in server_line):
                         print(server_line.strip())
                     else:
                         break
        file_search.close()
    elif choose=='2':
        arg=eval(input('please input add content:'))
        add_contant = arg['backend'].strip()
        file_search.seek(0)
        #print(file_search.tell())
        for line in file_search:
            line = line.strip()
            if add_contant in line:
                print(arg['backend'].strip(), 'is exist!!!')
                break
        else:
            file_search.write('\n')
            file_search.write('backend  ')
            file_search.write(str(arg['backend']))
            file_search.write('\n       ')
            for k, v in arg['record'].items():
                file_search.write(k.rjust(len(k) + 1, ' '))
                file_search.write(str(arg['record'][k]).rjust(len(str(arg['record'][k])) + 1, ' '))
            print('add_content success!!!')
        file_search.close()
    elif choose=='3':
        #file_delete = open('config_new','a+')
        arg=eval(input('please input delete content:'))
        for line_delete in file_search:
            if arg['backend'] in line_delete.strip() and line_delete.startswith('backend'):
                pass
            elif arg['record']['server'] in line_delete.strip() and str(arg['record']['weight']) in line_delete.strip() and str(arg['record']['maxconn']) in line_delete.strip():
                pass
            else:
                file_delete = open('config_new', 'a+')
                file_delete.write(line_delete)
                file_delete.close()
        print('delete content success! file_name is config_new.')
        file_search.close()
        break
    elif choose == '4':
        break
    else:
        print('input num error!!!!')
        #print('please input again operation num(1.查看,2.增加，3.删除):')
