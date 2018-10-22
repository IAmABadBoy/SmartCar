from socket import *
import abc
import threading


class Client(threading.Thread):
    def __init__(self, threadID, name, controller, port=9999, host='127.0.0.1'):
        threading.Thread.__init__(self)
        self.c=controller
        self.threadID = threadID
        self.name = name
        self.PORT = port
        self.HOST = host
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind((self.HOST, self.PORT))
        self.mode = ''

    def run(self):
        while True:
            try:
                data, address = self.s.recvfrom(1024)
                print(data, address)
                d_data = data.decode()
                self.c.process()
            except Exception as e:
                print(e)


