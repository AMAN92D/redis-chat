from flask import render_template
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app

@app.route('/')
def homepage():
    return render_template('homepage.html'), 200