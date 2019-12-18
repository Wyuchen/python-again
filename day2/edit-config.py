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
file_add=open('config','r+')
arg = {
            'bakend': 'www.oldboy.org',
            'record':{
                'server': '100.1.7.9',
                'weight': 20,
                'maxconn': 30
            }
        }

print(str(arg))

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
        print(2)
    elif choose=='3':
        print(3)
    else:
        print('input error!!!!')
        print('please input again:',choose)
'''
