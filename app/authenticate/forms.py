from flask_wtf import FlaskForm
from app.models import User
from wtforms import Form, StringField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, EqualTo


class RegistrationForm(FlaskForm):
    Email = StringField('Email')
    username = StringField('Username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])

    submit = SubmitField('Signup')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError(
                'There is already an account with that email. Check spelling or try another email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken. Try another one')


class LoginForm(FlaskForm):
    Username = StringField('username', validators=[Required()])
    password = PasswordField('password', validators=[Required()])

    submit = SubmitField('login')
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS')


class Comment(FlaskForm):

    title = StringField('The Pitch', validators=[Required()])
    Comment = TextAreaField('Pitch Comment', validators=[Required()])
    submit = SubmitField('Submit')
