#/usr/bin/env python
import  socket,os,hashlib

server=socket.socket()
server.bind(('localhost',9999))
server.listen()

while True:
    conn,addr=server.accept()
    print('新链接地址是:%s'%str(addr))
    while True:
        data=conn.recv(1024)
        if not data:
            print('client 断开')
            break
        else:
            ftp_cmd,file_name=data.decode().split()
            print('ftp_cmd:%s,file_name:%s'%(ftp_cmd,file_name))
            if os.path.isfile(file_name):
                f=open(file_name,'rb')
                m=hashlib.md5()
                file_size=os.stat(file_name).st_size
                conn.send(str(file_size).encode('utf-8')) #发送文件大小
                client_size_recv=conn.recv(1024) #等待客户端确认
                for line in f:
                    m.update(line)
                    conn.send(line)
                #print('file md5:%s'%m.hexdigest())
                f.close()
                conn.send(m.hexdigest().encode())
            else:
                print('%s is not exist'%file_name)

server.close()