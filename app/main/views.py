from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required
from app.models import User, PitchesCategory, Pitches
# from app.main.form import ProfileUpdate
from .. import db


@main.route('/')
def index():
    """
    A views root page funcction that returns index page and the various pitch categories
    """

    categories = PitchesCategory.get_categories(id)
    Love_Pitch = ('Love_Pitch')
    Life_Pitch = ('Life_pitch')

    return render_template('index.html', categories=categories)


@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    It will check Pitches form
    '''
    form = PitchForm()
    categories = PitchCategory.query.filter_by(id=id).first()

    if categories is None:
        abort(404)
