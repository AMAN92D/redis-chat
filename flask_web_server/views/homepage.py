from flask import render_template, request, jsonify
from flask_login import login_required, current_user
import json
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app, pusher_client, db2
from blackList_words import words
from models.users_models import User
import pymongo

@app.route('/')
@login_required
def homepage():

    if request.method == "GET":
         
        # pusher_client.trigger('my-channel', 'my-event', {'message': 'hello event'})

        users = list(db2['chat_users'].find())
        
        for i, v in enumerate(users):
            del users[i]['_id']
            users[i]['subscribtionDate'] = users[i]['subscribtionDate'].isoformat()    

        for i, v in enumerate(users):
            if users[i]['username'] == current_user.username:
                    del users[i]    

        users = json.dumps(users)

    if request.method == "POST": 
        pusher_client.trigger('my-channel', 'my-chat', {'message': 'hello chat'})

    return render_template('homepage.html', user=current_user, users=users, words=words), 200


@app.route('/message', methods=['POST'])
def message():

    try:
        
        if request.is_json == True:
            print(request.get_json())
            username = request.json['username']
            send_to = request.json['send_to']
            message = request.json['message']

            pusher_client.trigger('chat-channel', 'new-message', {'username':username, 'send_to':send_to, 'message': message})
            
            return jsonify({"message": "success"}), 200

    except:
        return jsonify({"message": "Bad request"}), 400        
    