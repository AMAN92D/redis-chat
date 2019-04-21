from flask import render_template, redirect, url_for, request
from flask_login  import login_user, logout_user, login_required

import datetime
from hashlib import sha512
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app
from models.users_models import User
from views.forms import LoginForm, RegisterForm


@app.route('/login', methods=['GET', 'POST'])
def login():

    loginForm = LoginForm()
    
    if loginForm.data['submit'] == True and request.method == "POST":

        submitted_username = loginForm.data['username']
        submitted_password = loginForm.data['password']

        registred_user = User.objects(username=submitted_username).first()
        
        if registred_user :
            if (registred_user.password == sha512(submitted_password.encode()).hexdigest() ):
                login_user(registred_user)
                return redirect(url_for('homepage')), 200
            else:
                alert = "Incorect Password"
                return render_template("login.html", alert=alert, loginForm=loginForm), 401
        else:
            alert = "Unknown User"
            return render_template("login.html", alert=alert, loginForm=loginForm), 401
        

    return render_template('login.html', loginForm=loginForm), 200

@app.route('/signup', methods=['GET', 'POST'])
def signup():

    registerForm = RegisterForm()
    loginForm = LoginForm()
    
    if loginForm.data['submit'] == True and request.method == "POST":

        try:
    
            i = list(map((lambda x: registerForm.data[x]), ["firstname","lastname", "username", "email", "password", "confirm_password", "country", "language", "birthdate"]))

            if '' or None in [i[2], i[3], i[4], i[5], i[6], i[7]] or i[4] != i[5]:

                errormessage = "Invalid Form"
                return render_template('signup.html', errormessage = errormessage, registerForm=registerForm), 400
            
            else:

                if not User.objects(email = i[3]).first() and not User.objects(username = i[2]).first():

                    registred_user = User(
                        username = i[2],
                        password = sha512(i[4].encode()).hexdigest(),
                        firstname = i[0] if i[0] else None,
                        lastname = i[1] if i[1] else None,
                        email = i[3],
                        country = i[6],
                        language = i[7],
                        birthdate = i[8] if i[8] else None,
                        subscribtionDate = datetime.datetime.now(),
                        friends = []
                    ).save()

                    login_user(registred_user)

                    return render_template('login.html', loginForm=loginForm), 200
                
                else:
                    if User.objects(email = i[3]).first():
                        errormessage = "email already registered"

                    elif User.objects(username = i[2]).first():
                        errormessage = "username already used"
                    
                    return render_template('signup.html', errormessage = errormessage, registerForm=registerForm), 401

        except Exception as e:

            errormessage = str(e)

            return render_template('signup.html', errormessage = errormessage, registerForm=registerForm), 500

    return render_template('signup.html', registerForm=registerForm), 200

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login')), 200