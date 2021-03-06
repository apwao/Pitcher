import os

class Config:
    """
    General configuration parent class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sowayi:Sowasse@localhost/pitcher'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    """
    Production configuration class inheriting
    from the main Main Configuration class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    """
    Development configuration class inheriting from
    the main configuration class
    """
    
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://sowayi:Sowasse@localhost/pitcher'
    
    DEBUG = True
    
config_options = {
    'development': DevConfig,
    'production': ProdConfig,
        
    }