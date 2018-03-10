import socket

"""
*****需求：模拟客户端向服务发起tcp链接请求********
1. 创建客户端套接字
2. 发出连接请求
3. 收发数据
4. 关闭套接字
"""

# 1. 创建客户端套接字
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 获取服务器的IP地址和端口号
server_ip = input("请输入您要连接的服务器的ip地址：")
server_port = int(input("请输入服务器的端口号："))
# 2. 向服务器发起连接请求
tcp_client_socket.connect((server_ip, server_port))

#  3. 接收发送数据
send_data = input("请输入您要发送的数据")
tcp_client_socket.send(send_data.encode('utf-8'))

recv_data = tcp_client_socket.recv(4096)
print("收到的数据为：%s" % recv_data.decode('utf-8'))

# 4. 关闭套接字
tcp_client_socket.close()