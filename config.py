import os

class Config:
    """
    General configuration parent class
    """

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://sowayi:Sowasse@localhost/pitch'
SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProdConfig(Config):
    """
    Production configuration class inheriting
    from the main Main Configuration class
    """
    pass

class DevConfig(Config):
    """
    Development configuration class inheriting from
    the main configuration class
    """
    
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://sowayi:Sowasse@localhost/pitch'
    
    DEBUG = True
    
    config_options = {
        'development': DevConfig,
        'production': ProdConfig,
        
    }