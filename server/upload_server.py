import os
import socket
from logger import log

class Server:

    def __init__(self, host='0.0.0.0', port=5555):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((host, port))
        self.sock.listen()

    def main(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                log('NEW CONNECTION', addr)

                while True:
                    SIZE = 81920000
                    data = conn.recv(SIZE)

                    if not data:
                        break

                    else:
                        with open(os.path.join('static', 'screenshot.png'), 'wb') as f:
                            f.write(data)

                        log('INFO', f'Packet Size: {len(data)}')

            except KeyboardInterrupt:
                break

                
if __name__ == "__main__":
    s = Server()
    s.main()