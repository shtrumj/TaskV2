from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField, DateField, SelectField, TextAreaField
from wtforms.validators import DataRequired, length, EqualTo, Email
from .extentions import db
from wtforms_sqlalchemy.fields import QuerySelectField
from taskManager.models import customer_query, employees_names_query, bosses_names_query
import taskManager.routes


class Loginform(FlaskForm):
    email = StringField("כתובת דואר אלקטרוני", validators=[DataRequired(), Email()])
    password = PasswordField('סיסמא', validators=[DataRequired()])
    submit = SubmitField('שליחה')


class RegistrationForm(FlaskForm):
    firstName = StringField("שם פרטי")
    lastName = StringField("שם משפחה")
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


class HomeSubmit(FlaskForm):
    submit = SubmitField('עדכון')


class WorkReportForm(FlaskForm):
    customer = QuerySelectField('שם הלקוח', query_factory=customer_query, allow_blank=True)
    client = StringField('שם המשתמש')
    description = StringField('תאור הקריאה')
    classification = SelectField('סוג התקלה', choices=[('בעיית תוכנה','בעיית תוכנה'),('בעיית חומרה','בעיית חומרה')])
    # status = SelectField('סטטוס', choices=[('בעיה נפתרה', 'בעיה נפתרה'), ('בעיה בטיפול', 'בעיה בטיפול'),('טרם החל טיפול','טרם החל טיפול')])
    # status = SelectField('סטטוס', choices=[('טרם החל טיפול','טרם החל טיפול'),('בעיה נפתרה', 'בעיה נפתרה'), ('בעיה בטיפול', 'בעיה בטיפול')])
    status = SelectField('סטטוס', choices=[('1','טרם החל טיפול'),('2', 'בעיה נפתרה'), ('3', 'בעיה בטיפול')])
    resolve= TextAreaField('תיאור הפתרון')
    reason= TextAreaField('סיבה')
    whatHasBeenDone = TextAreaField('מה נעשה עד כה ?')
    submit = SubmitField('שלח דוח')