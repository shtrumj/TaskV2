from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, length, EqualTo, Email

class Loginform(FlaskForm):
    email = StringField("כתובת דואר אלקטרוני", validators=[DataRequired(), Email()])
    password = PasswordField('סיסמא',validators=[DataRequired()])
    submit = SubmitField('שליחה')


class RegistrationForm(FlaskForm):
    firstName = StringField("שם פרטי(באנגלית)")
    lastName = StringField("שם משפחה(באנגלית)")
    email = StringField("כתובת דואר אלקטרוני")
    password = PasswordField('סיסמא',validators=[DataRequired(),EqualTo('pass_confirm',message='ססמאות חייבות להיות זהות')])
    pass_confirm = PasswordField('אימות סיסמא', validators=[DataRequired()])
    submit = SubmitField('הירשמו')

    # def check_email(self, field):
    #     if Users.query.filter_by(email=field.data.first)
