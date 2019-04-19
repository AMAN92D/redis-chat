from flask import render_template
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app

@app.route('/profil')
def profil():
    return render_template('profil.html'), 200