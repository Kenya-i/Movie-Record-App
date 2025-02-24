#import os

#class Config:
#    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
#    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

#class DevelopmentConfig(Config):
#    DEBUG = True

#class TestingConfig(Config):
#    TESTING = True

#class ProductionConfig(Config):
#    DEBUG = False
#    TESTING = False