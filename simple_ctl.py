import threading


class sctl(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.alive = False
        self.roate = True
        self.data = None

    def start(self):
        threading.Thread.start(self)
        self.alive = True

    def stop(self):
        self.alive = False

    def process(self):
        pass

    def run(self):
        while self.alive:
            if ~self.roate:
                self.process()
                self.roate=True

    def get_data(self,data):
        self.roate = False
        self.data = data