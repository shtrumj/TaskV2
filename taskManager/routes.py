from flask import Blueprint, render_template, request, url_for, redirect, flash, session
from taskManager.models import Users, Customers, Employees, Tasks
from wtforms import ValidationError
from flask_login import login_user, login_required, logout_user, current_user
from taskManager.forms import Loginform, RegistrationForm, CustomersForm, EmployeeForm, TasksForm
from taskManager.extentions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms_sqlalchemy.fields import QuerySelectField

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
        #password = generate_password_hash(password, 'sha256')
        # form.password.data = ''
        user = Users.query.filter_by(email=email).first()
        if user.check_password(password) and user is not None:
            flash('התחברות בוצעה בהצלחה', category='success')
            login_user(user, remember=False)
            session['username'] = user.firstName
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                flash('נא להתחבר!', category='danger')
                next = url_for('main.home')

            return redirect(next)
            # return render_template('home.html', user=user)
        else:
            flash('שם משתמש וֿ.או ססמא לא נכונים', category='danger')
            return redirect(url_for('main.login'))

    return render_template('login.html', form=form, user=user, password=password)


@main.route('/reg', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        password = form.password.data
        pass_confirm = form.pass_confirm.data

        def check_email(self, field):
            if Users.query.filter_by(email=field.data).first():
                raise ValidationError('דואר אלקטרוני קיים במערכת')

        new_user = Users(firstName=firstName, lastName=lastName, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('משתמש נוצר בהצלחה!', category='success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/home', methods=('GET', 'POST'))
@login_required
def home():
    if 'username' in session:
        username = session['username']

    return render_template('home.html',user=username)


@main.route('/addCustomer', methods=('GET', 'POST'))
def addCustomer():
    form = CustomersForm()
    if form.validate_on_submit():
        name = form.name.data
        city = form.city.data
        address = form.address.data
        internalDomain = form.internalDomain.data
        externalDomain = form.externalDomain.data
        owaAdd = form.owaadd.data
        new_customer = Customers(name=name, city=city, address=address, internalDomain=internalDomain,
                                 externalDomain=externalDomain, owaAdd=owaAdd)
        db.session.add(new_customer)
        db.session.commit()
        flash('לקוח נוצר בהצלחה!', category='success')
        return redirect(url_for('main.addCustomer'))
    return render_template('addcustomer.html', form=form)


@main.route('/addEmployee', methods=('GET', 'POST'))
def addEmployee():
    form = EmployeeForm()
    if form.validate_on_submit():
        firstName = form.firstName.data
        lastName = form.lastName.data
        email = form.email.data
        if db.session.query(Employees.email).filter_by(email=email).first():
            flash ("Email Already registered", category="danger")
            return redirect(url_for('main.addEmployee'))
        else:
            phone = form.phone.data
            new_employee = Employees(firstName=firstName, lastName=lastName, email=email, phone=phone)
            db.session.add(new_employee)
            db.session.commit()
            flash('עובד נוצר בהצלחה!', category='success')
            return redirect(url_for('main.addEmployee'))
    return render_template('addsysadmin.html', form=form)


@main.route('/addTask', methods=('GET', 'POST'))
def addTask():
    form = TasksForm()
    # assignQuery = Employees.query.order_by(Employees.firstName).all()
    if form.validate_on_submit():
        # return '<h1>{}</h1>'.format(form.assignTo.data)
        description = str(form.description.data)
        customer = str(form.customer.data)
        deadline = str(form.deadline.data)
        reportTo = str(form.reportTo.data)
        assignTo = str(form.assignTo.data)
        new_task = Tasks(description=description, customer=customer, deadline=deadline, reportTo=reportTo, assignTo=assignTo)
        #return '<h1>Report to: {} </h1>'.format(reportTo)
        db.session.add(new_task)
        db.session.commit()
        flash('משימה נוצרה בהצלחה!', category='success')
        return redirect(url_for('main.addTask'))
    return render_template('addtask.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash("בוצעה התנתקות", category="success")
    return redirect(url_for('main.login'))
