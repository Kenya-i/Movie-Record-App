from flask import Blueprint

record_bp = Blueprint("record", __name__, template_folder='templates')

from .import views