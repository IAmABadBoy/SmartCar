from socket import *

HOST = '127.0.0.1'
PORT = 9999

s = socket(AF_INET, SOCK_DGRAM)
s.connect((HOST, PORT))
while True:
    message = input('send message:>>')
    s.send(message.encode())
    data = s.recv(1024)
    print(data)

s.close()