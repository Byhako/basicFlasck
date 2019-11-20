# conda install -c anaconda psycopg2
import os

class Config(object):
    SECRET_KEY = 'my_secret_key'

class DevelopmentConfig(Config):
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://usuario:password@URL/base_de_datos'
    SQLALCHEMY_DATABASE_URI = 'postgresql://ruben:ruben@localhost/baseFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False