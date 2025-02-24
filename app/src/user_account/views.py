from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import signup_bp, login_bp, user_bp
from .forms import SignupForm, LoginForm, UserForm
from .models import User
from datetime import timedelta
from app.src import db
from werkzeug.security import generate_password_hash
###消さない
#from app.src import subtitles

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)
    if request.method == "GET":
        return render_template("user_account/signup.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        user = User.add_user(form.username.data, form.email.data, form.password.data)
        print(user)
        if user:
            login_user(user, remember=True, duration=timedelta(seconds=600))
            flash("登録しました", "success")
            return redirect(url_for('user.user'))
        else:
            flash("メールアドレスがすでに存在しています", "warning")
            return render_template("user_account/signup.html", form=form)
    
    return render_template("user_account/signup.html", form=form)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "GET":
        #response = subtitles.search(tmdb_id=346, languages="en")
        #print(a)
        #print(a.to_dict())

        #srt = subtitles.download_and_parse(response.data[0])

        #print(srt)

        return render_template("user_account/login.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        user = User.select_by_email(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user, remember=True, duration=timedelta(seconds=600))
            flash("ログインしました", "success")
            return redirect(url_for("user.user"))
        else:
            flash("ユーザーが存在しません", "danger")
            return render_template("user_account/login.html", form=form)
    
    return render_template("user_account/login.html", form=form)


@user_bp.route("/user")
@login_required
def user():
    return render_template("user_account/user.html")


@user_bp.route("/user/edit", methods=["GET", "POST"])
@login_required
def user_edit():
    form = UserForm(request.form)
    if request.method == "GET":
        return render_template("user_account/user_edit.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        user = User.select_by_email(current_user.email)
        if user:
            user.username = form.username.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)
            db.session.commit()
            flash("ユーザー情報を更新しました")
            return render_template("user_account/user_edit.html", form=form)
        else:
            flash('ユーザーが存在しません','danger')
            return render_template("user_account/user_edit.html", form=form)

    return render_template("user_account/user_edit.html", form=form)
    

@user_bp.route("/user/delete", methods=["POST"])
@login_required
def user_delete():
    if request.method == "POST":
        user = User.select_by_email(current_user.email)
        
        db.session.delete(user)
        db.session.commit()
        logout_user()
        flash("ユーザーを削除しました")
        return render_template("home/index.html")
    
    return render_template("user_account/user.html")
    #return redirect(url_for("home.home"))


@login_bp.route("/logout", methods=[ "GET"])
@login_required
def logout():
    logout_user()
    flash("ログアウトしました", 'success')
    #return redirect(url_for("home.home"))
    return render_template("home/index.html")



#@user_bp.route("/forgot_password", methods=["GET", "POST"])
#def forgot_password():
#    form = ForgotPasswordForm(request.form)
#    if request.method == "POST" and form.validate_on_submit():
#        email = form.email.data
#        user = User.select_by_email(email)
#        if user:
#            with db.session.begin(subtransactions=True):
#                token = PasswordResetToken.publish_token(user)
#            db.session.commit()
#            reset_url = f"http://127.0.0.1:5000/reset_password/{token}"