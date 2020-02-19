import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:Access@localhost/pitch'
    SECRET_KEY = os.environ.get("SECREY_KEY")
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'PITCH'
    SENDER_EMAIL = 'teresawanjiku2000@gmail.com'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringaschool:Access@localhost/pitch'

    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
