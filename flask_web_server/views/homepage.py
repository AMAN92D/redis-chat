from flask import render_template, request
from flask_login import login_required, current_user
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app, pusher_client

users = []

@app.route('/')
@login_required
def homepage():

    if request.method == "GET": 
        pusher_client.trigger('my-channel', 'my-event', {'message': 'hello event'})

    if request.method == "POST": 
        pusher_client.trigger('my-channel', 'my-chat', {'message': 'hello chat'})

    return render_template('homepage.html', user=current_user), 200


@app.route('/message', methods=['POST'])
def message():

    try:
        if request.is_json == True:
            
            username = request.json['username']
            send_to = request.json['send_to']
            message = request.json['message']

            pusher_client.trigger('chat-channel', 'new-message', {'username':username, 'send_to':send_to, 'message': message})
            
            return render_template('homepage.html', user=current_user), 200
            
        else:
            return 400

    except:
        return 400        

    return render_template('homepage.html', user=current_user), 200
    