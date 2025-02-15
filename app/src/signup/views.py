from flask import render_template
from . import signup_bp

@signup_bp.route("/")
def signup():
    return render_template("signup/signup.html")