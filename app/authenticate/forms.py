from flask_wtf import FlaskForm
# from forms.validators import Required, Email, EqualTo
# from model_user import model_user
from wtforms import Form, StringField, BooleanField, PasswordField, SubmitField
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    Email=StringField('Email')
    username=StringField('Username',)
    password = PasswordField('password' )

    submit = SubmitField('Submit to sign up')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')
class LoginForm():
    Username=StringField('username')
    password = PasswordField('password')

    submit = SubmitField('login')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')