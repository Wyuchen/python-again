#/usr/bin/env python
# def search_config(var):
#     file_search=open('config','r')
#     for line in file_search:
#         line=line.strip()







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

#add_contant=evel(input("please input add contant:").strip())
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

while True:
    choose=input("input operation num(1.查看,2.增加，3.删除):")
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
        add_contant = arg['bakend'].strip()
        file_search.seek(0)
        #print(file_search.tell())
        for line in file_search:
            line = line.strip()
            if add_contant in line:
                print(arg['bakend'].strip(), 'is exist!!!')
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
        print(3)
    else:
        print('input error!!!!')
        print('please input again:',choose)
