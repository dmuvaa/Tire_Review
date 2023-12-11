from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import routes  # Import routes if you have a separate routes.py file
