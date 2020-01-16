#/usr/bin/env python

import socket
client=socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))
#client.send(b'hello world')        #发送普通字符--->需要转换称byte类型
'''
client.send('你好'.encode('utf-8')) #发送中文-->需要转换称byte类型
data=client.recv(1024)
#print('recv:',data)
print('recv:',data.decode())    #发送中文接收的时候在转换回来
'''
while True:
    msg=input('please input send message:').strip()
    if len(msg)==0:
        continue
    client.send(msg.encode('utf-8'))
    data=client.recv(10240)
    print('recv:',data.decode())
client.close()
