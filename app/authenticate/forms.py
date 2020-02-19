from flask_wtf import FlaskForm
from app.models import User
from wtforms import Form, StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, EqualTo


class RegistrationForm(FlaskForm):
    Email=StringField('Email')
    username=StringField('Username', validators=[Required()])
    password = PasswordField('password', validators=[Required()] )

    submit = SubmitField('Signup')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')

class LoginForm(FlaskForm):
    Username=StringField('username', validators=[Required()])
    password = PasswordField('password',validators=[Required()])

    submit = SubmitField('login')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')



class Comment(FlaskForm):

    title = StringField('The Pitch',validators=[Required()])
    Comment = TextAreaField('Pitch Comment', validators=[Required()])
    submit = SubmitField('Submit')