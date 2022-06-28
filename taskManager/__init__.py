from flask import Flask
from .extentions import db
from flask_migrate import Migrate
from flask_login import LoginManager
from flask import Blueprint
from taskManager.routes import main
import os

base_dir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    login_manager = LoginManager()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(base_dir,'data.sqlite3' )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] ='xncv bjhbhdskc9iu3egbcikeniolwer'
    db.init_app(app)
    app.register_blueprint(main)
    Migrate(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    return app