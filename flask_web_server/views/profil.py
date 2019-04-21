from flask import render_template, request, send_from_directory
from flask_login import login_required, current_user
import os
import sys
sys.path.append('/var/www/flask_web_server')

from chatServer import app, photos
from models.users_models import User

@app.route('/profil', methods=['GET', 'POST'])
@login_required
def profil():

    static_pic_folder_path = app.static_folder + "/profile_pic/"
    user_image_name = current_user.username + "_profil_pic."

    def findFilePic(name, path):
        for root, dirs, files in os.walk(path):
            for f in files:
                if name in f:
                    return True, f
            else:
                return False, None    

    existing_file = findFilePic(user_image_name, static_pic_folder_path)

    if request.method == 'GET':

        if current_user.avatarPath:

            return render_template('profil.html', user=current_user), 200

        else:        
            
            if existing_file[0] == True:
                current_user.avatarPath = existing_file[1]
                return render_template('profil.html', user=current_user), 200
            else:
                current_user.avatarPath = ""
                return render_template('profil.html', user=current_user), 200


    if request.method == 'POST':

        if request.files['photo']:

            try:
                uploadedFilenameType = request.files['photo'].filename.split(".")[1]

                if existing_file[0] == True:  
                    os.remove(static_pic_folder_path + (existing_file[1]))

                user_image_name += uploadedFilenameType
                current_user.avatarPath = user_image_name
                
                photos.save(request.files['photo'], name=user_image_name)
                User.objects(username=current_user.username).update(set__avatarPath=user_image_name)
                
                return render_template('profil.html', user=current_user), 200

            except Exception as e:
                errormsg = "Failed !!"
                err = str(e)
                print(err)
                return render_template('profil.html', errormessage=errormsg, user=current_user), 500

    return render_template('profil.html', user=current_user), 200


@app.route('/profil/<filename>')
def send_image(filename):
    return send_from_directory("static/profile_pic", filename)