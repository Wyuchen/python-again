#/usr/bin/env python
#没有解决数据长的问题
import socket,os

server=socket.socket()
server.bind(('localhost',6969)) #绑定监听端口
server.listen()  #监听端口
while True:
    print('开始等待客户端访问')
    #conn_client 客户端连过来在服务端为其生成的是一个连接实例
    conn_client,addr=server.accept()  #等待访问
    print(conn_client)
    print(addr)
    print('客户端已经访问了')
    while True:
        server_data=conn_client.recv(1024)
        if server_data :
            print('server_data:',server_data.decode())
            res=os.popen(server_data.decode()).read()
            #conn_client.send(server_data.upper())
            conn_client.send(res.encode('utf-8'))
            #conn_client.sendall(res)   #一次性将数据发送出去
        else:
            break
server.close()


