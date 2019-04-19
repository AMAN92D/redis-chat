from flask import render_template
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app

@app.route('/login')
def login():
    return render_template('login.html'), 200