from flask import Flask
from forms import stringField, PasswordField, SubmitField, BooleanField, TextAreaField, ValidationError
from form.validators import Required, Email,EqualTo
from model_user import user



class ProfileUpdate(FlaskForm):
    bio = TextAreaField('As a User', validators=[Required()])
    submit = SubmitField('Submit')