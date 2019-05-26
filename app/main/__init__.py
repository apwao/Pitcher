from flask import Blueprint

main = Blueprint('main',__name__)

# import the views and errors modules to avoid circular dependencies
from . import views, errors