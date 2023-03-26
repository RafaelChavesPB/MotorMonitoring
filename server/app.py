from flask import Flask, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.get('/')
def get_index():
    return 'Olá! Este é o backend da aplicação motormonitoring.'


@app.post('/')
def get_post():
    data = request.get_json()
    current = int(data.get('current', 0))
    voltage = int(data.get('voltage', 0))
    time = datetime.now().strftime("%H:%M:%S")
    data = {'current': current, 'voltage': voltage, 'time': time}
    socketio.emit('incoming_data', data)
    return '200'


if __name__ == '__main__':
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True, host='0.0.0.0', port=5000)
