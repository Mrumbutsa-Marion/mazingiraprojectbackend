from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mazingira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db=SQLAlchemy(app)

def create_app(): 

    db.init_app(app)
    rest_api = Api(app)

    
    # add routes
    from app import routes

    return app

