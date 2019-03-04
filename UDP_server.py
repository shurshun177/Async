import socket
UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NUMBER = 6789
message = 'Hellow, Server'
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NUMBER))
while True:
    data, addr = serverSock.recvfrom(1024)
    print('Message: ', data)