from flask import Blueprint, render_template, request, url_for, redirect, flash
from taskManager.models import Users
from wtforms import ValidationError
from flask_login import login_user, login_required,logout_user, current_user
from taskManager.forms import Loginform, RegistrationForm, CustomersForm
from taskManager.extentions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
main = Blueprint('main', __name__, template_folder='taskManager/templates', static_folder='taskManager/static')


@main.route('/', methods=('GET', 'POST'))
@main.route('/login', methods=('GET', 'POST'))
def login():
    user = False
    password = False
    form = Loginform()
    if form.validate_on_submit():
        email = form.email.data
        form.email.data = ''
        password = form.password.data
        password = generate_password_hash(password, 'sha256')
        form.password.data = ''
        user = Users.query.filter_by(email=email).first()
        if user:
            flash('התחברות בוצעה בהצלחה', category='success')
            login_user(user, remember=True)
            return render_template('home.html')

    return render_template('login.html', form=form, user=user, password=password)


@main.route('/reg',methods=('GET','POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data
        pass_confirm = form.pass_confirm.data
        def check_email(self,field):
            if Users.query.filter_by(email=field.data).first():
                raise ValidationError('דואר אלקטרוני קיים במערכת')

        new_user = Users(firstName=firstName, lastName=lastName, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html',form=form)


@main.route('/home', methods=('GET', 'POST'))
@login_required
def home():
    return render_template('home.html')


@main.route('/addCustomer', methods=('GET', 'POST'))
def addCustomer():
    form = CustomersForm()

    return render_template('addcustomer.html', form=form)