import os
import socket

class Client:

    def __init__(self, host='127.0.0.1', port=5555, link=''):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.link = link

    def send_img(self):
        with open(os.path.join('screenshots', 'screenshot.png'), 'rb') as f:
            self.sock.sendfile(f, offset=0, count=None)

        self.link = self.sock.recv(4096).decode('utf8')

        print('Image sent successfully to server')
        print(self.link)
