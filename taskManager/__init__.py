from flask import Flask
from .extentions import db
import os

base_dir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ os.path.join(base_dir,'data.sqlite3' )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app