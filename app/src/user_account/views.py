from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import signup_bp, login_bp, user_bp
from .forms import SignupForm, LoginForm
from .models import User
from datetime import timedelta

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)
    if request.method == "GET":
        return render_template("user_account/signup.html", form=form)
        
    elif request.method == "POST" and form.validate_on_submit():
        user = User.add_user(form.username.data, form.email.data, form.password.data)
        print(user.password)
        if user:
            flash("登録しました")
            #ちゃんとしたredirectを後で書く
            return render_template("user_account/signup.html", form=form)
        else:
            flash("メールアドレスがすでに存在しています")
            return render_template("user_account/signup.html", form=form)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    print(form)
    if request.method == "GET":
        return render_template("user_account/login.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        user = User.select_by_emial(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=True, duration=timedelta(seconds=600))
            flash("ログインしました")
            #return render_template("user_account/user.html")
            return redirect(url_for("user.user"))
        elif user == None:
            flash("ユーザーが存在しません")
            return render_template("user_account/login.html", form=form)
    
    return render_template("user_account/login.html", form=form)

@user_bp.route("/user")
@login_required
def user():
    return render_template("user_account/user.html")

@login_bp.route("/logout", methods=[ "POST"])
@login_required
def logout():
    logout_user()
    flash("ログアウトしました")
    return redirect(url_for("home.home"))
    #return render_template("user_account/user.html")