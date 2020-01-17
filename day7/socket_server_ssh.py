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
            conn.send(res.encode('utf-8'))
server.close()


'''
将命令结果长度传给客户端的时候,中文字节长度是3,
如果在发送给客户端长度时候没有encode,
会造成传给客户端的长度和计算出来的长度不一样,传给客户端的数值偏小
'''