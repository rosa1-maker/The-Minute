from flask import Flask
from wtforms import  SubmitField,TextAreaField
from wtforms.validators import Required, Email,EqualTo
from app.models import User



class ProfileUpdate():
    bio = TextAreaField('As a User', validators=[Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField('Pitch Title', validators=[Required()])
    body = TextAreaField('Enter your comment here', validators=[Required()])
    author = StringField('Author', validators=[Required()])
    category = RadioField('Pick Category',
                          choices=[('business', 'business'),
                                   ('jobs', 'jobs')],
                          validators=[Required()])
    submit = SubmitField('Submit')