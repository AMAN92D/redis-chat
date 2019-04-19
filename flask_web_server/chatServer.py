# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['SECRET_KEY'] = "║kjksdf_ètjmlfk654-+:§$€uçàçufç_(_(_-por"

# app.config['MONGODB_HOST'] = 'mongodb://chat-mongo:27017/chat'

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://chat-mongo:27017/chat',
    'db': 'chat'
}

socketio = SocketIO(app)
db = MongoEngine(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

from views.homepage import *
from views.profil import *
from views.login import *

####### Handling Erros #########

@app.errorhandler(401)
def error401(e):
    return render_template('401.html'), 401

@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500

######### Start the Server ##########

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', debug=True)