#/usr/bin/env python
import socket,os,hashlib

client=socket.socket()

client.connect(('localhost',9999))

while True:
    cmd=input('请输入执行的命令:').strip()
    if len(cmd):
        if cmd.startswith('get'):
            client.send(cmd.encode('utf-8'))
            server_file_size=client.recv(1024)
            print('下载文件大小:%s'%server_file_size)
            client.send('准备下载文件....'.encode('utf-8'))
            file_size=int(server_file_size.decode())
            receive_size=0
            file_name=cmd.split()[1]
            f=open(file_name+'.new','wb')
            m=hashlib.md5()
            while receive_size < file_size:
                if file_size-receive_size > 1024:
                    size=1024
                else:
                    size=file_size-receive_size
                receive_data=client.recv(size)
                m.update(receive_data)
                f.write(receive_data)
                receive_size+=len(receive_data)
            else:
                new_file_md5 = m.hexdigest()
                print('%s 下载完毕,文件大小:%s'%(file_name,receive_size))
                f.close()
            receive_md5=client.recv(1024)
            print('server file md5:%s \n client file md5:%s'%(receive_md5,new_file_md5))


    else:
        continue
client.close()