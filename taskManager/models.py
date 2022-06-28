from .extentions import db, login_manager
from flask_login import UserMixin
from wtforms import StringField, PasswordField, BooleanField
from werkzeug.security import check_password_hash, generate_password_hash



@login_manager.user_loader
def load_users(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.TEXT)
    lastName = db.Column(db.TEXT)
    email = db.Column(db.TEXT, unique=True)
    password_hash = db.Column(db.TEXT)

    def __init__(self, firstName, lastName, email, password):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password_hash = generate_password_hash(password, 'sha256')

    def check_password(self, password):
        return check_password_hash(password,'sha256')



class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firsName = db.Column(db.TEXT)
    lasName = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)

    def __init__(self, firstName, lastName, email, phone):
        self.firsName = firstName
        self.lasName = lastName
        self.email = email
        self.phone =phone



