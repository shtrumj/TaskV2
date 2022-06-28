from .extentions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary=True)
    email = db.Column(db.TEXT)
    password = db.Column(db.TEXT)

    def __init__(self, email, password):
        self.email = email
        self.password = password


class Employees(db.Model):
    id = db.Column(db.Integer, primary=True)
    firsName = db.Column(db.TEXT)
    lasName = db.Column(db.TEXT)
    email = db.Column(db.TEXT)
    phone = db.Column(db.TEXT)

    def __init__(self, firstName, lastName, email, phone):
        self.firsName = firstName
        self.lasName = lastName
        self.email = email
        self.phone =phone



