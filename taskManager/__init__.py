from flask import Flask
from flask_migrate import Migrate
from .extentions import db, migrate
from flask import Blueprint
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from taskManager.routes import main
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(base_dir,'data.sqlite3' )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] ='xncv bjhbhdskc9iu3egbcikeniolwer'
    migrate.init_app(app, db)
    app.register_blueprint(main)
    return app