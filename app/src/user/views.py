from flask import Blueprint, render_template
from . import user_bp
#from src import db
from .user_logic import Logic


@user_bp.route("/user")
def user():
    Logic()
    
    return render_template("user/user.html")