from main import app
from application.sec import datastore
from application.models import db, Role,User
#from flask_security import hash_password
#from werkzeug.security import generate_password_hash

with app.app_context():
    db.create_all()
    datastore.find_or_create_role(name="admin", description="User is an admin")
    datastore.find_or_create_role(
        name="sponser", description="User is an sponser")
    datastore.find_or_create_role(name="influncer", description="User is a influncer")
    db.session.commit()


    if not datastore.find_user(email="admin@email.com"):
        datastore.create_user(
            email="admin@email.com", name="admin",password="admin", roles=["admin"])
    if not datastore.find_user(email="inst1@email.com"):
        datastore.create_user(
            email="sponser@email.com", name="sponser",password="sponser", roles=["sponser"], active=False)
    if not datastore.find_user(email="stud1@email.com"):
        datastore.create_user(
            email="influncer@email.com",name="influncer", password="influncer", roles=["influncer"])
    

    db.session.commit()