
import socket
import threading

LosePort = 77
WinPort = 105

EndSequence = '1234567890)(*&^%$#@!'


class WinThread(threading.Thread):
    def __init__(self):
        super(WinThread, self).__init__()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('0.0.0.0', WinPort))
            sock.listen()
            while True:
                try:
                    (s, port) = sock.accept()
                    msg = ''
                    while EndSequence not in msg:
                        data = s.recv(1024)
                        if data == b'':
                            raise Exception
                        msg = msg + data.decode(encoding = 'utf-8')
                    msg = msg[:-len(EndSequence)]
                    print(msg)
                except Exception as e:
                    print(e)
                    pass

                
worker = WinThread()
worker.start()
worker.join()
