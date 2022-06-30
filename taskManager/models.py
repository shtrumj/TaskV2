from .extentions import db, login_manager
from flask_login import UserMixin
from wtforms import StringField, PasswordField, BooleanField
from werkzeug.security import check_password_hash, generate_password_hash

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


EmployeeSysadmin = db.Table('EmployeeSysadmin',
                            db.Column('employee_id', db.Integer, db.ForeignKey('employees.id')),
                            db.Column('customer_id', db.Integer, db.ForeignKey('customers.id'))
                            )


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
        return check_password_hash(self.password_hash, password)


class Employees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firsName = db.Column(db.TEXT)
    lasName = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)
    customers = db.relationship('Customers', secondary=EmployeeSysadmin, backref='administrators')

    def __init__(self, firstName, lastName, email, phone):
        self.firsName = firstName
        self.lasName = lastName
        self.email = email
        self.phone = phone


class Customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    city = db.Column(db.String(10))
    address = db.Column(db.String(20))
    internalDomain = db.Column(db.String(15))
    externalDomain = db.Column(db.String(20))
    owaAdd = db.Column(db.String(20))

    def __init__(self, name, city, address, internalDomain, externalDomain, owaAdd):
        self.name = name
        self.city = city
        self.address = address
        self.internalDomain = internalDomain
        self.externalDomain = externalDomain
        self.owaAdd = owaAdd


# class Tasks(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String(20))
#     customer = db.


