# -*- coding: utf-8 -*-
# @Author : yanpengfei
# @time   : 2020/11/18 下午5:13
# @File   : server.py

from socket import *
from time import ctime

def bind_tcp_server(host, port, number=5):

    ADDR = (host, port)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)  # 绑定IP地址和端口号
    tcpSerSock.listen(number)  # 监听，使得主动变为被动
    return tcpSerSock


def start_server(tcp_server, buf_size=1024):

    try:
        while True:
            print('正在等待连接....')
            tcpCliSock, addr = tcp_server.accept()  # 当来新的连接时，会产生一个的新的套接字为客户端服务
            print(f"收到来自{addr}的连接.......")
            while True:
                data = tcpCliSock.recv(buf_size)  # 接受数据，缓存区设置为1kb
                if not data:
                    break
                tcpCliSock.send('[%s] %s' % (bytes(ctime(), 'utf-8'), data))  # 加上时间戳，并对数据编码
            tcpCliSock.close()
    except Exception as e:
        print(f"错误：{e}")
    finally:
        tcp_server.close()


if __name__ == "__main__":

    HOST = ''
    PORT = '40001'

    tcp_server = bind_tcp_server(host=HOST, port=PORT)

    start_server(tcp_server, 1024)

