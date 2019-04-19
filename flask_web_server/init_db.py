from chatServer import db
from hashlib import sha512

import sys
sys.path.append('/var/www/flask_web_server/')

from models.users_models import User

try:
    existing_user = User.objects(username = "Aman").first()

    if not existing_user:
        User(
            username = "Aman",
            password = sha512("aman".encode()).hexdigest(),
            firstname = "Amd",
            lastname = "Mld",
            email = "aman@chat.fr",
            friends = []
        ).save()
    
    print("DATABASE INIT SUCCESSFULLY")

except Exception as e:
    print("ERROR DURING DATABASE INIT")
    raise e