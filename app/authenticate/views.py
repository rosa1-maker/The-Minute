from flask_login import login_user, logout_user, login_required
from flask_mail import Mail
from flask import render_template, redirect, url_for, flash
from . import authenticate
from .forms import RegistrationForm, LoginForm
from .. import db

@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    login_form= LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()
        if user is not None and user.verify_paassword(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(url_for('min.index'))

        flash('Invalid username or password')
    return render_template('authenticate/login_form,', login_form=login_form)    

@authenticate.route('/register', methods=['GET', 'POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('authenticate.login'))

    return render_template('authenticate/register.html', RegistrationForm = form)    

