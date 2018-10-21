from socket import *
import threading


class Client(threading.Thread):
    def __init__(self, threadID, name, port=9999, host='127.0.0.1'):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.PORT = port
        self.HOST = host
        self.s = socket(AF_INET, SOCK_DGRAM)
        self.s.bind((self.HOST, self.PORT))
        self.mode = ''
        self.d_data = ''


    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    def run(self):
        try:
            while True:
                data, address = self.s.recvfrom(1024)
                print(data, address)
                d_data = data.decode()
                self.d_data = d_data
                if d_data == 'reset':
                    self.mode = ''
                    continue
                if(self.mode == ''):
                    if(d_data=='yykz'):
                        self.s.sendto('yykz is open now'.encode(), address)
                        self.mode = 'yykz'
                    elif(d_data=='auto_slam'):
                        self.s.sendto('auto_slam is open'.encode(), address)
                        self.mode = 'auto_slam'
                    elif(d_data=='simple_ctl'):
                        self.s.sendto('simple_ctl is open'.encode(),address)
                        self.mode = 'simple_ctl'
                if(self.mode == 'yykz'):
                    if(self.is_number(d_data)):
                        pass
                if(self.mode == 'auto_slam'):
                    pass
                if(self.mode == 'simple_cctl'):
                    pass
        except Exception as e:
            print(e)
    def get_mode(self):
        return self.mode
    def get_data(self):
        return self.d_data