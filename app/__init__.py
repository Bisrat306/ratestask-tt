import sys
from flask import Flask, jsonify

from app.config import config_by_name
from app.database import db
from app.namespaces import init_ns

from sqlalchemy.exc import OperationalError

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    #Register namespaces
    init_ns(app)
    db.init_app(app)

    #Checks db connection on server start
    try:
        with app.app_context():
            db.create_all()
    except OperationalError as e:
        #Output the error message to the console
        error_message = "Database connection failed: {}".format(str(e))
        print(error_message) 
        sys.exit(1)

    return app
