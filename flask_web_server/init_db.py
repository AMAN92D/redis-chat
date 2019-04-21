from chatServer import db, redis
import datetime
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
            subscribtionDate = datetime.datetime.now(),
            friends = []
        ).save()
        
    print("\n==== INIT OUPUT ==== \n")
    print("MONGO DATABASE INIT SUCCESSFULLY :\nUsername : Aman\nPassword : aman")

except Exception as e:
    print("ERROR DURING MONGO DATABASE INIT")
    raise e

try:
    if redis.ping():
        print("\nREDIS DATABASE INIT SUCCESSFULLY")
        print(redis.info()['redis_version'])
    print("\n==== END ==== \n")

except Exception as e:
    print("ERROR DURING REDIS DATABASE INIT")
    raise e        