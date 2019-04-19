from flask import render_template
from flask_socketio import send
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app, socketio

@app.route('/')
def home():
    return render_template('homepage.html'), 200

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)    