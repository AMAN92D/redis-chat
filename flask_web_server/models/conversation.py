import sys
sys.path.append('/var/www/flask_web_server')
from chatServer import db
from models.message import Message


class Conversation(db.Document):
    meta = {'collection': 'conversation'}
    users = db.ListField()
    messages = db.EmbeddedDocumentListField(Message)