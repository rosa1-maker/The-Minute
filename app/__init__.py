from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
# from flask_moment import Moment


login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'authenticate.login'

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)

    app.config.from_object(config_options[config_name])

    # initializing extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # moment.init_app(app)
    # mail.init_app(app)

    from app.main import main as main_blueprint
    from app.authenticate import authenticate as authenticate_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(authenticate_blueprint, url_prefix='/authenticate')

    return app
