import socket

"""
******功能描述说明******
1.获取键盘数据，并将其发送给对方
2.接收数据并显示
"""

def send_msg(udp_socket):
    """发送信息"""
    msg = input("\n请输入您要发送的信息：")
    dest_ip = input("\n请输入您要发送的ip:")
    dest_port = int(input("\n请输入对方的端口号："))

    # 发送数据到指定的电脑上的指定程序中,需要编码为bytes类型的数据进行发送
    udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))

def recv_msg(udp_socket):
    """接收信息"""
    # 接收到的数据recv_data是一个元组
    # 第1个元素是对方发送的bytes类型的数据
    # 第2个元素是对方的ip和端口
    recv_data = udp_socket.recvfrom(4096)
    recv_msg = recv_data[0].decode('utf-8')
    recv_ip = recv_data[1]
    print(">>>%s:%s" % (str(recv_ip),recv_msg))



def main():
    # 创建udp服务套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地的地址信息，包括IP和端口号：元组（‘ip字符串’， 端口号）
    udp_socket.bind(('', 7080))

    while True:

        """建立一个死循环，不断的收发信息"""
        print("*"*30)
        print("1.接收消息")
        print("2.发送消息")
        print("*"*30)
        opt_num = input("请输入你要选择的选项（1或2）：")

        if opt_num == '1':
            recv_msg(udp_socket)

        elif opt_num == '2':
            send_msg(udp_socket)

        else:
            print("您的输入有误，请重新输入")



if __name__ == '__main__':
    main()
