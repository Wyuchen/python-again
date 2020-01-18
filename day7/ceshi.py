#/usr/bin/env python

cmd,file_name=input('please input:').split()

if len(cmd) and len(file_name):
    print('cmd:%s' % cmd, 'file_name:%s' % file_name)

else:
    'error!'