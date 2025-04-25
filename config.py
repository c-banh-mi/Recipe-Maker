#config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Secret Key for form security and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secretty_secret_key'

    # SQLAlchemy configuration
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
