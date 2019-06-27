from flask import jsonify, request

import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app
from models.users_models import User
import pusher


@app.route('/api/pusher/auth', methods=['POST'])
def pusher_authentification():
    channel_name = request.form.get('channel_name')
    socket_id = request.form.get('socket_id')
    print(socket_id)
    return jsonify({"channel_name": channel_name, "socket_id": socket_id})