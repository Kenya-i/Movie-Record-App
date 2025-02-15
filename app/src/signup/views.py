from flask import render_template, request, redirect, url_for
from . import signup_bp
from .forms import SignupForm
from .models import User

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if request.method == "GET":
        return render_template("signup/signup.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        User.add_user(form.username.data, form.email.data, form.password.data)
        return redirect(url_for("home.home"))
    
    return render_template("signup/signup.html", form=form)