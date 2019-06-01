import sys
sys.path.append('/var/www/flask_web_server')
from chatServer import db


class Channel(db.Document):
    meta = {'collection': 'channel'}

    name = db.StriengField()
    from_user = db.StringField()
    to_user = db.StringField()