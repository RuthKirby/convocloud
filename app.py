import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from flask_bootstrap import Bootstrap
import nlp.mainMod as mainMod
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev')
socketio = SocketIO(app)
Bootstrap(app)

@app.route('/')
def hello():
    return render_template('index.html')

@socketio.on('json_button')
def handle_message(json):
    print('{0}'.format(json))
    """words = mainMod.processText(json)"""
    emit('processed', mainMod.processText(json))

@socketio.on('connect')
def test_connect():
    print("Connection established")

if __name__ == '__main__':
    """
    app.run()
    """
    socketio.run(app)