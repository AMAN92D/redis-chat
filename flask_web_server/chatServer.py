# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask_login import LoginManager
from flask_mongoengine import MongoEngine
from flask_redis import Redis
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
import pusher

#### App Init ####

pusher_client = pusher.Pusher(
  app_id='767564',
  key='fabd2102b489229ba7b7',
  secret='467be41fedd0cbf0a815',
  cluster='eu',
  ssl=True
)

app = Flask(__name__)

app.config['SECRET_KEY'] = "║kjksdf_Jtjmlfk654!86§$€uepXuf!_!_!_-por"

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://chat-mongo:27017/chat',
    'db': 'chat'
}

app.config['REDIS1_URL'] = 'redis://chat-redis:6379/1'
app.config['UPLOADED_PHOTOS_DEST'] = 'static/profile_pic'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)

db = MongoEngine(app)
redis = Redis(app, 'REDIS1')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#### Exposing Views ####

from views.homepage import *
from views.profil import *
from views.login import *


#### Manage User ####

from models.users_models import *

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.objects(pk=user_id).first()
    except:
        return None


def login_exempt(f):
    f.login_exempt = True
    return f

#### Handling Erros ####

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
    app.run(host='0.0.0.0', debug=True)