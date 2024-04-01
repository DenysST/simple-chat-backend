from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)


@socketio.on('message')
def handle_message(message):
    print('Message received:', message)
    emit('message', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, log_output=True, use_reloader=True)
