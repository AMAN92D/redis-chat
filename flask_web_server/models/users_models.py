from flask_login import UserMixin

import sys
sys.path.append('/var/www/flask_web_server/')
from chatServer import db


class User(db.Document, UserMixin):
    meta = {'collection': 'chat_users'}

    username = db.StringField()
    password = db.StringField()
    first_name = db.StringField()
    last_name = db.StringField()
    email = db.StringField()
    token = db.StringField()
    friends = db.ListField()