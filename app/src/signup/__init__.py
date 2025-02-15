from flask import Blueprint

signup_bp = Blueprint("signup", __name__, url_prefix="/signup", template_folder='templates')

from .import views