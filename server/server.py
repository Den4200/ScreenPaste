import os
import threading
from flask import Flask
from upload_server import Server

app = Flask(__name__)

IMGS= 'static'
app.config['UPLOAD_FOLDER'] = IMGS

@app.route('/')
def home():
    return f'<img src="{ os.path.join(app.config["UPLOAD_FOLDER"], "screenshot.png") }" alt="screenshot">'

def main():
    s = Server()

    u_s = threading.Thread(target=s.main)
    a = threading.Thread(target=app.run)

    u_s.start()
    a.start()

    u_s.join()
    a.join()
    

if __name__ == '__main__':
    main()
