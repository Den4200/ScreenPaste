import os
import time
import random
import string
import socket
import multiprocessing
from logger import log

class Server:

    def __init__(self, host='0.0.0.0', port=5555):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host, port))
        self.sock.listen(3)

        self.key_length = 20
        self.key_file = 'keys.csv'

    def _genRandKey(self):
        chars = string.ascii_letters + string.digits
        key = ''.join(random.choice(chars) for _ in range(self.key_length))

        # \/ Old method \/

        # lower_keys = [random.randrange(97, 123, 1) for _ in range(self.key_length//2)]
        # upper_keys = [random.randrange(65, 91, 1) for _ in range(self.key_length//2)]
        # keys = [chr(list(zip(lower_keys, upper_keys))[y][x]) for y in range(self.key_length//2) for x in range(2)]
        # key = ''.join(k for k in keys)

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

    def connection(self, conn, addr):
        while True:
            data = conn.recv(81920000)

            if not data:
                break
                
            else:

                b = b''
                img_name = f'screenshot_{self._randKey()}.png'
                conn.send(bytes(f'http://screenpaste.sytes.net:5000/static/{img_name}', 'utf8'))

                while data:
                    log('INFO', f'Packet Size: {len(data)}')
                    b += data
                    data = conn.recv(81920000)

                with open(os.path.join('static', img_name), 'wb') as f:
                    f.write(b)

                log('NEW IMAGE', img_name)



    def main(self):
        while True:
            conn, addr = self.sock.accept()
            log('NEW CONNECTION', addr)

            new_conn = multiprocessing.Process(target=self.connection, args=(conn, addr))
            new_conn.start()
            new_conn.join()
