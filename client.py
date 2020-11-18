# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2020/11/18 下午5:44
# @File   : client.py

from socket import *

HOST = '127.0.0.1'
PORT = 40001
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)  # 建立TCP连接

while True:
    data = input("输入你要发送的消：")
    if not data:  # 当空数据的时候，连接就停止了。
        break
    tcpCliSock.send(data.encode('utf-8'))  # 发送数据
    data = tcpCliSock.recv(BUFSIZ)  # 接受对方回复消息
    if not data:
        break
    print(data.decode('utf-8'))  # 对数据解码

tcpCliSock.close()
