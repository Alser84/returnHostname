import os

from flask import Flask, render_template
import socket
app = Flask(__name__)
print(socket.gethostname())

#env
app_port = int(os.environ.get('app_port', 5000))

@app.route('/')
def returnHostname():
    #return socket.gethostname()
    return render_template('index.html', hostname = socket.gethostname() )

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000)
