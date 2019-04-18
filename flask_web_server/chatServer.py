# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = "║kjksdf_ètjmlfk654-+:§$€uçàçufç_(_(_-por"

#TODO fix import homepage. Only retreive 404
from views import homepage

# @app.route('/')
# def homepage():
#     return render_template('homepage.html'), 200

@app.errorhandler(401)
def error401(e):
    return render_template('401.html'), 401

@app.errorhandler(404)
def error404(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500

######### Start the Server ##########

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')