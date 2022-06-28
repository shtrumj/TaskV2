from .extentions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.TEXT)
    lastName = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    password = db.Column(db.TEXT)


    def __init__(self, firstName, lastName, email, password):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password


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



