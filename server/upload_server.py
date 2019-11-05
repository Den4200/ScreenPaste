import os
import time
import random
import socket
from logger import log

class Server:

    def __init__(self, host='0.0.0.0', port=5555):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host, port))
        self.sock.listen(3)

        self.key_length = 10
        self.key_file = 'keys.csv'

    def _genRandKey(self):
        lower_keys = [random.randrange(97, 123, 1) for _ in range(self.key_length)]
        upper_keys = [random.randrange(65, 91, 1) for _ in range(self.key_length)]
        keys = [chr(list(zip(lower_keys, upper_keys))[y][x]) for y in range(self.key_length) for x in range(2)]
        key = ''.join(k for k in keys)

        return key

    def _randKey(self):
        key = self._genRandKey()

        with open(self.key_file, 'r') as f:
            keys = f.readlines()

        run = True

        for k in keys:
            if k.split(',')[1][:-1] == key:
                self._randKey()
                run = False
                break
            
        if run:
            with open(self.key_file, 'a') as f:
                f.write(f'{time.ctime()},{key}\n')

            return key

    def main(self):
        while True:
            conn, addr = self.sock.accept()
            log('NEW CONNECTION', addr)

            while True:
                data = conn.recv(81920000)

                if not data:
                    break
                
                else:

                    b = b''
                    img_name = f'screenshot_{self._randKey()}.png'
                    conn.send(bytes(f'http://127.0.0.1:5000/static/{img_name}', 'utf8'))

                    while data:
                        log('INFO', f'Packet Size: {len(data)}')
                        b += data
                        data = conn.recv(81920000)

                    with open(os.path.join('static', img_name), 'wb') as f:
                        f.write(b)

                    log('NEW IMAGE', img_name)

if __name__ == "__main__":
    s = Server()
    print(s._randKey())
