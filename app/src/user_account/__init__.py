from flask import Blueprint

signup_bp = Blueprint("signup", __name__, template_folder='templates')
login_bp = Blueprint("login", __name__, template_folder='templates')
user_bp = Blueprint("user", __name__, template_folder='templates')

from .import views, models