from .forms import RegistrationForm, LoginForm,Form
from .. import db
from flask_login import login_user, logout_user, login_required
from flask_mail import Mail
from flask import render_template, redirect, url_for, flash
from . import authenticate
from app.models import User, PitchesCategory, Pitches


def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('authenticate.login'))

    return render_template('authenticate/register.html', RegistrationForm=form)


@authenticate.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('authenticate.login'))

    return render_template('authenticate/register.html', RegistrationForm=form)


@authenticate.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_paassword(form.password.data):
            login_user(user, form.remember.data)
            return redirect(url_for('main.index'))

        flash('Invalid username or password')
    return render_template('login.html', login_form=form)


@authenticate.route('/logout',)
def logout():
    logout_user()
    return redirect(url_for("main.index"))
