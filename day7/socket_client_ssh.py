#/usr/bin/env python

import socket

client=socket.socket()

client.connect(('localhost',9999))

while True:
    cmd=input('请输入执行的命令:').strip()
    if len(cmd):
        client.send(cmd.encode('utf-8'))
        data_res_size = client.recv(1024)
        print('recv_data_size:', data_res_size.decode())
        #循环获取所有数据
        receive_size=0
        receive_data=b''
        while receive_size < int(data_res_size.decode()):
            data_recv=client.recv(1024)
            receive_size+=len(data_recv)
            receive_data+=data_recv
            #print(str(receive_size).encode('utf-8'))  #显示数据大小
        else:
            print('cmd res recrive success!!!,len:%s'%receive_size)
            print(receive_data.decode())
    else:
        continue
client.close()