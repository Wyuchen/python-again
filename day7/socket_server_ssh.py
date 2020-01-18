#/usr/bin/env python
import  socket,os

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
            print('执行的命令是:%s' % data)
            res = os.popen(data.decode()).read()
            if len(res)==0:
                res='cmd has no output...'
            conn.send(str(len(res.encode())).encode('utf-8'))
            client_ack=conn.recv(1024)
            conn.send(res.encode('utf-8'))
server.close()


'''
1.将命令结果长度传给客户端的时候,中文字节长度是3,
如果在发送给客户端长度时候没有encode,
会造成传给客户端的长度和计算出来的长度不一样,传给客户端的数值偏小

2.socket 粘包现象:当服务器端出现两次send的时候,可能服务端会将数据一起发给客户端.
   解决方法: 1)通过time.sleep(0.5)可以临时解决
            2)服务器端等待客户端的确认,确认之后再发下面的数据
            server:client_ack=conn.recv(1024)
            client:client.send('为防止粘包,客户端像服务器发送确认!'.encode('utf-8'))
        实例为scoket_server/client_ssh.py
            3)除最后一次外,其他都传1024,最后一次传小于1024大小的数据
              通过if判断,给定每次client.recv(size)中size的大小
        实例为scoket_server/client_ftp.py
            
'''