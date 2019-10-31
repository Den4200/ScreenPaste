import os
import socket
from logger import log

class Server:

    def __init__(self, host='0.0.0.0', port=5555):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host, port))
        self.sock.listen(3)

    def _readImgNum(self):
        with open('img_num.txt', 'r') as f:
            return int(f.read())

    def _updateImgNum(self):
        prev_num = self._readImgNum()
        with open('img_num.txt', 'w') as f:
            f.write(str(prev_num + 1))

    def main(self):
        while True:
            conn, addr = self.sock.accept()
            log('NEW CONNECTION', addr)

            while True:
                data = conn.recv(81920000)

                if not data:
                    break
                
                else:
                    self._updateImgNum()

                    b = b''
                    img_name = f'screenshot_{self._readImgNum()}.png'
                    conn.send(bytes(f'127.0.0.1:5000/{img_name}/', 'utf8'))

                    while data:
                        log('INFO', f'Packet Size: {len(data)}')
                        b += data
                        data = conn.recv(81920000)

                    with open(os.path.join('static', img_name), 'wb') as f:
                        f.write(b)

                    log('NEW IMAGE', img_name)
