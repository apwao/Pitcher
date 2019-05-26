from flask_bootstrap import Bootstrap
from config import config_options
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail

# creating instances of the extensions
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet("photos", IMAGES)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
mail = Mail()

def create_app(config_name):
    """
    create_app function responsible for initializing
    the app and all the extensions the app needs to function
    and passing them to the manage.py module for running
    """
    # creating an instance of Flask
    app = Flask(__name__)
    
    app.config.from_object(config_options[config_name])
    
    #Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    
    # Registering blue prints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')
    
    
    
    return app