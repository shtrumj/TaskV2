from flask import Blueprint, render_template, request, url_for, redirect
from taskManager.models import Users
from taskManager.forms import UsersForm
from taskManager import LoginManager
from taskManager.extentions import db
from werkzeug.security import generate_password_hash, check_password_hash
main = Blueprint('main', __name__, template_folder='taskManager/templates')


@main.route('/', methods=('GET', 'POST'))
@main.route('/login', methods=('GET', 'POST'))
def login():
    user = False
    password = False
    form = UsersForm()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
        password = form.password.data
        password = generate_password_hash(password, 'sha256')
        form.password.data = ''
        return '<h1> email address is ' + email + ' and password is ' + password

    return render_template('login.html', form=form, user=user, password=password)


@main.route('/reg',methods=('GET','POST'))
def register():
    form = UsersForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data
        new_user = Users(firstName=firstName, lastName=lastName, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html',form=form)


@main.route('/home', methods=('GET', 'POST'))
def home():
    return render_template('home.html')