# conda install -c anaconda psycopg2
import os

class Config(object):
    SECRET_KEY = 'my_secret_key'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT =465
    MAIL_USE_SSL = True
    MAIL_USE_TSL = False
    MAIL_USERNAME = 'eldragondera1@gmail.com'
    MAIL_PASSWORD = os.environ.get('PASSWORD_EMAIL_CF')


class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://usuario:password@URL/base_de_datos'
    SQLALCHEMY_DATABASE_URI = 'postgresql://ruben:ruben@localhost/baseFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False