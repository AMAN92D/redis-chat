from flask_login import UserMixin
import datetime

import sys
sys.path.append('/var/www/flask_web_server')
from chatServer import db


class User(db.Document, UserMixin):
    meta = {'collection': 'chat_users'}

    username = db.StringField()
    password = db.StringField()
    firstname = db.StringField()
    lastname = db.StringField()
    email = db.StringField()
    token = db.StringField()
    country = db.StringField()
    language = db.StringField()
    avatarPath = db.StringField()
    facebookUsername = db.StringField()
    birthdate = db.DateTimeField()
    subscribtionDate = db.DateTimeField(default=datetime.datetime.now)
    friends = db.ListField()