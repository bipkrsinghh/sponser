from flask import Flask
from flask_security import Security
from flask_cors import CORS
from application.models import db
from config import DevelopmentConfig
from application.resources import api
from application.sec import datastore
from application.worker import celery_init_app
import flask_excel as excel

def create_app(): #defining app instance function
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    CORS(app)
    db.init_app(app) #initializing the database
    api.init_app(app) #initializing the api instance
    excel.init_excel(app)
    app.security = Security(app,datastore)
    
    with app.app_context():
        import application.views

    return app

app = create_app() #calling function to create app
celery_app = celery_init_app(app)


if __name__ == '__main__':
    app.run(debug=True)
