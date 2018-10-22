from listen_ins import Client
from simple_ctl import sctl
from voice_ctl import vctl


class Controller:
    def __init__(self,sctl:sctl,vctl:vctl):
        self.mode = ''
        self.sctl = sctl
        self.vctl = vctl

    def start(self):
        thread = Client(1, 'Thread-1',self)
        thread.start()
        thread.join()

    def voice_ctl(self, data):
        self.vctl.get_data(data)

    def auto_slam(self):
        pass

    def simple_ctl(self,data):
        self.sctl.get_data(data)

    def set_mode(self, mode):
        self.mode = mode

    def process(self, data):
        if data == 'voice_ctl':
            self.set_mode('voice_ctl')
        elif data == 'auto_slam':
            self.set_mode('auto_slam')
        elif data == 'simple_ctl':
            self.set_mode('simple_ctl')
        elif data == 'main':
            self.set_mode('main')
        elif self.mode == 'voice_ctl':
            self.voice_ctl(data)
        elif self.mode == 'simple_ctl':
            self.simple_ctl(data)




if __name__ == '__main__':
    pass