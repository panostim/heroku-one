import os
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Bind to the port defined by the environment variable PORT
    PORT = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT)
