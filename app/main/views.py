from flask import render_template, request,redirect,url_for,abort
from . import main
from flask_login import  login_required, current_user
from app.templates.models import  User, PitchCategory, Pitches, Comments, Likes, Dislikes
from .forms import ProfileUpdate, PitchForm, CommentForm, CategoriesForm
from .. import db,photos

@main.route('/')
def index():
    ""
    A views root page funcction that returns index page and the various news source
    ""

    categories = PitchCategory.get_categories()

    return render_template('index.html', categories=categories)

@main.route('/category/pitch/new/int:id>',methods=['GET', POST])
@login_required
def new_pitch(id):
    '''
    It will check Pitches form
    '''
    form = PitchForm()
    categories = PitchCategory.query.filter_by(id=id).first()

    if categories is None:
        abort(404)
                                                                                                                                                                                            



