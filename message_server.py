
import socket
import threading
import sys
import time
import tkinter as tk
from tkinter import simpledialog

LosePort = 77
WinPort = 105

EndSequence = '1234567890)(*&^%$#@!'

messages = []
message_lock = threading.Lock()

class Message:
    def __init__(self, won, message, ip):
        self.won = won
        self.message = message
        self.ip = ip

class BaseThread(threading.Thread):
    def __init__(self):
        super(BaseThread, self).__init__()

    def handle_message(self, message, ip):
        message_lock.acquire()
        try:
            messages.append(Message(self._won, message, ip))
        finally:
            message_lock.release()

    def respond(self, ip_addr):
        pass

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('0.0.0.0', self._port))
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
                    self.handle_message(msg, s.getpeername()[0])
                except Exception as e:
                    print(e)
                    pass



class Winthread(BaseThread):
    def __init__(self):
        super(Winthread, self).__init__()
        self._port = WinPort 
        self._won = True

class Losethread(BaseThread):
    def __init__(self):
        super(Losethread, self).__init__()
        self._port = LosePort 
        self._won = False


winthread = Winthread()
losethread = Losethread()
winthread.start()
losethread.start()

while True:
    message_lock.acquire()
    try:
        if len(messages) > 0:
            window = tk.Tk() 
            window.withdraw()
            if messages[0].won:
                tk.messagebox.showinfo('You WIN!', messages[0].message)
            else:
                tk.messagebox.showinfo('You LOSE', messages[0].message)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.bind(('0.0.0.0', 0))
                    sock.connect((messages[0].ip, WinPort))
                    data = 'Good game.'.encode(encoding = 'utf-8') + EndSequence.encode(encoding = 'utf-8')
                    sock.send(data)

            messages.clear()
            window.destroy()
    finally:
        message_lock.release()
    time.sleep(0.3)

