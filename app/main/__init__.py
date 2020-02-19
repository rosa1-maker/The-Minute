from flask import Blueprint
main = Blueprint('main', __name__)
from app.authenticate import views,forms
