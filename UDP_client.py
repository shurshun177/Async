import socket
UDP_IP_ADDRESS = '127.0.0.1'
UDP_PORT_NUMBER = 6789
message = b'Hellow, Server'
try:
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print('Socket exception')
for i in range(9):
    print(i)
    try:
        clientSock.sendto((message), (UDP_IP_ADDRESS, UDP_PORT_NUMBER))
    except:
        print('Vse')
    print('Vse hokkey')