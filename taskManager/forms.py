from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import data_required, length


class UsersForm(FlaskForm):
    firstName = StringField("שם פרטי(באנגלית)")
    lastName = StringField("שם משפחה(באנגלית)")
    email = StringField("כתובת דואר אלקטרוני")
    password = PasswordField('סיסמא')
    submit = SubmitField('שליחה')

