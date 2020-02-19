from flask import Flask
from wtforms import  SubmitField,TextAreaField
from wtforms.validators import Required, Email,EqualTo
from app.models import User



class ProfileUpdate():
    bio = TextAreaField('As a User', validators=[Required()])
    submit = SubmitField('Submit')
