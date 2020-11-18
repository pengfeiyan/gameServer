# # -*- coding: utf-8 -*-
# # @Author : yanpengfei
# # @time   : 2020/11/18 下午5:13
# # @File   : server.py
#
# from socket import *
# import threading
# import time
#
# def bind_tcp_server(host, port, number=5):
#
#     ADDR = (host, port)
#     tcpSerSock = socket(AF_INET, SOCK_STREAM)
#     tcpSerSock.bind(ADDR)  # 绑定IP地址和端口号
#     tcpSerSock.listen(number)  # 监听，使得主动变为被动
#     return tcpSerSock
#
#
# def start_server(tcp_server, buf_size=1024):
#
#     try:
#         while True:
#             print('正在等待连接....')
#             tcpCliSock, addr = tcp_server.accept()  # 当来新的连接时，会产生一个的新的套接字为客户端服务
#             print(f"收到来自{addr}的连接.......")
#             while True:
#                 data = tcpCliSock.recv(buf_size)  # 接受数据，缓存区设置为1kb
#                 if not data:
#                     break
#                 tcpCliSock.send(f"[{bytes(str(time.time()), 'utf-8')}] {data}".encode("utf-8"))  # 加上时间戳，并对数据编码
#             tcpCliSock.close()
#     except Exception as e:
#         print(f"错误：{e}")
#     finally:
#         tcp_server.close()
#
#
# if __name__ == "__main__":
#
#     HOST = ''
#     PORT = 40001
#
#     tcp_server = bind_tcp_server(host=HOST, port=PORT)
#
#     start_server(tcp_server, 1024)
#

# 导入套接字模块
import socket
# 导入线程模块
import threading
import time

def dispose_client_request(tcp_client_1, tcp_client_address):
    while True:
        recv_data = tcp_client_1.recv(4096)
        if recv_data:
            global send_data
            send_data += recv_data
        else:
            clients.remove(tcp_client_1)
            tcp_client_1.close()
            break


def broadcast():

    while True:
        time.sleep(10)
        global send_data
        # 广播消息
        for client in clients:
            client.send(f"[{time.time()}]{send_data}".encode())
        # 广播之后，将数据清空
        send_data = b""


if __name__ == '__main__':

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server.bind(("", 40001))
    tcp_server.listen(32)

    clients = []
    send_data = b""

    sync_timer = threading.Timer(10, broadcast)
    sync_timer.start()

    while True:
        tcp_client_1, tcp_client_address = tcp_server.accept()
        clients.append(tcp_client_1)

        thd = threading.Thread(target=dispose_client_request, args=(tcp_client_1, tcp_client_address))
        thd.setDaemon(True)
        thd.start()

    # 关闭服务器套接字 （其实可以不用关闭，因为服务器一直都需要运行）
    # tcp_server.close()