from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from datetime import datetime


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(init(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship("Pitches", backref="user", lazy="dynamic")
    

    @property
    def password(self):
        raise AttributeError('Cannot read password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return 'User{self.username}'


class PitchesCategory(db.Model):
    '''
    this class defines a pitch per category
    '''
    __tablename__ = 'pitch_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    pitch = db.relationship("Pitches", backref="categories", lazy="dynamic")

    def save_category(self):
        '''
        Function that saves a category
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        '''
        Function that returns all the data from the categories after being queried
        '''
        categories = PitchCategory.query.all()
        return categories


class Pitches(db.Model):
    '''
    This class will hokd all instances of the pitches in the different categories
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    actual_pitch = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_category_id = db.Column(db.Integer, db.ForeignKey("pitch_categories.id"))
   

    def save_pitch(self):
        '''
        Function to save a pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        """Function which clears all the pitches in a particular category"""
        Pitches.all_pitches.clear()

    @classmethod
    def get_pitches(cls, id):
        '''
        this function will get a pitch wjen requested with the date it was posted
        '''
        pitches = Pitches.query.order_by(
            Pitches.date_posted.desc()).filter_by(category_id=id).all()
        return pitches
