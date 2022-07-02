from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField, DateField, SelectField
from wtforms.validators import DataRequired, length, EqualTo, Email
from .extentions import db
from taskManager.models import employees_names_query
from wtforms_sqlalchemy.fields import QuerySelectField
from taskManager.models import customer_query, employees_names_query, bosses_names_query
import taskManager.routes


class Loginform(FlaskForm):
    email = StringField("כתובת דואר אלקטרוני", validators=[DataRequired(), Email()])
    password = PasswordField('סיסמא', validators=[DataRequired()])
    submit = SubmitField('שליחה')


class RegistrationForm(FlaskForm):
    firstName = StringField("שם פרטי(באנגלית)")
    lastName = StringField("שם משפחה(באנגלית)")
    email = StringField("כתובת דואר אלקטרוני")
    password = PasswordField('סיסמא',
                             validators=[DataRequired(), EqualTo('pass_confirm', message='ססמאות חייבות להיות זהות')])
    pass_confirm = PasswordField('אימות סיסמא', validators=[DataRequired()])
    submit = SubmitField('הירשמו')


class CustomersForm(FlaskForm):
    name = StringField("שם הלקוח")
    city = StringField("עיר")
    address = StringField("כתובת")
    internalDomain = StringField("דומיין פנימי")
    externalDomain = StringField("דומיין חיצוני")
    owaadd = StringField("כתובת OWA")
    submit = SubmitField('יצירת לקוח')


class EmployeeForm(FlaskForm):
    firstName = StringField("שם פרטי")
    lastName = StringField("שם משפחה")
    email = StringField("כתובת דואר אלקטרוני")
    phone = StringField("מספר טלפון נייד")
    submit = SubmitField('הוספת מנהל רשת')


# class TasksForm(FlaskForm):
#     assignTo = SelectField('אחראי משימה', choices=[])
#     description = StringField('תאור המשימה')
#     customer = SelectField('שם הלקוח', choices=[])
#     deadline = DateField('תאריך יעד')
#     reportTo = SelectField('ממנה משימה', choices=[])
#     submit = SubmitField('צור משימה')

class TasksForm(FlaskForm):
    assignTo = QuerySelectField('אחראי משימה' ,query_factory=employees_names_query, allow_blank=True)
    description = StringField('תאור המשימה')
    customer = QuerySelectField('שם הלקוח', query_factory=customer_query, allow_blank=True)
    deadline = DateField('תאריך יעד')
    reportTo = QuerySelectField('ממנה משימה', query_factory=bosses_names_query, allow_blank=True)
    submit = SubmitField('צור משימה')
