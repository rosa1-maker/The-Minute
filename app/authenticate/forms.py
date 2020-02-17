from flask import FlaskForm
from forms.validators import Required, Email, EqualTo
from model_user import model_user
from forms import StringFields, PasswordField, SubmitField, BooleanField
from forms import ValidationError


class RegistrationForm(FlaskForm):
    Email=StringFields('Email', validators=[Required(), Email()])
    username=StringFields('Username', validators=[Required() ])
    password = PasswordField('password,' validators=[Required])

    submit = SubmitField('Submit to sign up')
    