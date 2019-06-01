import sys
sys.path.append('/var/www/flask_web_server')
from chatServer import db


class Message(db.EmbeddedDocument, db.Document):
    meta = {'collection': 'message'}

    message = db.StriengField()
    from_user = db.StringField()
    to_user = db.StringField()
    channel_id = db.IntField()
    message_datetime = db.DateTimeField()