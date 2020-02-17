from flask_login import login_user, logout_user, login_required
from ..email import mail_message
from flask import render_template, redirect, url_for, flash
from . import authenticate
from model_user import user
from .forms import RegistrationForm, LoginForm
from .. import db

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    login_form= LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is ! None and user.verify_paassword(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('min.index'))

        flash('Invalid username or password')
    return render_template('authenticate/login_form,', login_form=login_form)    
