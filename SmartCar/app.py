from listen_ins import Client


# main function
def main():
    listen_ins()


def listen_ins():
    thread = Client(1, 'Thread-1')
    thread.start()
    thread.join()


def voice_ctl():
    pass


def auto_slam():
    pass


def simple_ctl():
    pass


if __name__ == '__main__':
    main()


