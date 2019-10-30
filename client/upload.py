import os
import socket

class Client:

    def __init__(self, host='127.0.0.1', port=5555):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send_img(self):
        with open(os.path.join('screenshots', 'screenshot.png'), 'rb') as f:
            b = f.read()

        self.sock.sendall(b)
        print('Image sent successfully to server')

if __name__ == "__main__":
    c = Client()
    c.send_img()
