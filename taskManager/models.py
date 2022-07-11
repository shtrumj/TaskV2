from .extentions import db, login_manager
from flask_login import UserMixin
from wtforms import StringField, PasswordField, BooleanField, SelectField, DateTimeField
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms_sqlalchemy.fields import QuerySelectField


def employees_names_query():
    query = Employees.query.all()
    return query


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
    firstName = db.Column(db.TEXT)
    lastName = db.Column(db.TEXT)
    email = db.Column(db.String(25), unique=True)
    phone = db.Column(db.TEXT)
    customers = db.relationship('Customers', secondary=EmployeeSysadmin, backref='administrators')
    tasks = db.relationship('Tasks', backref='employee', lazy=True)

    def __init__(self, firstName, lastName, email, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone

    def __repr__(self):
        return str(self.id) + ".  " + self.firstName + " " + str(self.lastName)


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

    def __repr__(self):
        return self.name


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignTo = db.Column(db.String(20))
    description = db.Column(db.String(20))
    customer = db.Column(db.String(100))
    deadline = db.Column(db.String(12))
    reportTo = db.Column(db.String(20))
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

    def __init__(self, assignTo, description, customer, deadline, reportTo, employee_id):
        self.assignTo = assignTo
        self.description = description
        self.customer = customer
        self.deadline = deadline
        self.reportTo = reportTo
        self.employee_id = employee_id


class WorkReports(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(20))
    client= db.Column(db.String(20))
    description = db.Column(db.String(30))
    status = db.Column(db.String(25))
    classification = db.Column(db.String(20))
    resolve = db.Column(db.String(150))
    reason = db.Column(db.String(150))
    whatHasBeenDone = db.Column(db.String(150))

    def __init__(self, customer, client, description,classification, resolve, status, reason, whatHasBeenDone):
        self.customer = customer
        self.client = client
        self.description = description
        self.classification = classification
        self.status = status
        self.resolve = resolve
        self.reason = reason
        self.whatHasBeenDone = whatHasBeenDone



def customer_query():
    query = db.session.query(Customers).all()
    return query


def bosses_names_query():
    query = db.session.query(Employees).all()
    return query
