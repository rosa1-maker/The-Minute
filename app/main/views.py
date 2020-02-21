from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import login_required
from app.models import User, PitchesCategory, Pitches
from .. import db
from .forms import PitchForm, CommentForm, Vote, ProfileUpdate


@main.route('/')
def index():
    """
    A views root page funcction that returns index page and the various pitch categories
    """
    pitches = Pitch.queery.all()

    return render_template('index.html', categories=categories)


@main.route('/business')
def business():
    """
    Function that renders the business category pitches and its content
    """
    business_pitch = Pitch.query.filter_by(category='business').all()

    return render_template('business.html', business=business_pitch)


@main.route('/jobs')
def technology():
    """
    Function that renders the job category pitches and its content
    """

    technology_pitch = Pitch.query.filter_by(category='technology').all()

    return render_template('technology.html', technology=technology_pitch)


@main.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    pitch_form = PitchForm()

    if pitch_form.validate_on_submit():
        title = pitch_form.title.data
        body = pitch_form.body.data
        author = pitch_form.author.data
        category = pitch_form.category.data
        # category=category
        new_pitch = Pitch(title=title, body=body,
                          author=author, category=category, upvotes=0,
                          downvotes=0,
                          users=current_user)
        new_pitch.save_pitches()
        return redirect(url_for('main.index'))

    return render_template('new.html', pitch_form=pitch_form)


@main.route('/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    vote_radio = Vote()
    pitch = Pitch.query.get(id)
    if comment_form.validate_on_submit():
        title = comment_form.title.data
        comment = comment_form.comment.data
        # category=category
        new_comment = Comment(comment=comment,
                              title=title,
                              user=current_user)
        new_comment.save_comment()
        return redirect(url_for('main.index'))

    return render_template('comment.html',
                           comment_form=comment_form,
                           pitch=pitch,
                           vote_radio=vote_radio)


@main.route('/update', methods=['POST'])
def update():
    pitch = Pitch.query.get(id)
    pitch.upvotes = request.args.get('jsdata')
    pitch.downvotes = request.args.get('jsdata')

    return render_template('button.html', pitch=pitch)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    """
    Function that renders the profile page of our user
    """
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)
