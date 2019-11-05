import os
import socket
from logger import log

class Client:

    def __init__(self, host='screenpaste.sytes.net', port=5555, link=''):
        host = socket.gethostbyname(host)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.link = link

    def send_img(self):
        try:
            with open(os.path.join('screenshots', 'screenshot.png'), 'rb') as f:
                self.sock.sendfile(f, offset=0, count=None)

            log('INFO', 'Image sent successfully to server')

            self.link = self.sock.recv(4096).decode('utf8')
            log('LINK', self.link)
            
            self.sock.close()

        except Exception as e:
            log('ERROR', e)

    def returnLink(self):
        return self.link
