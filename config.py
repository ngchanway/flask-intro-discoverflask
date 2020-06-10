# default config
import os

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xc9N+G\x03\xcb\x92lm\x9f\xb9\x19\xef\x1c\xd2\xe6\xd1\x08\x10)&\xb0\x1c\x1f'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False
