from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import signup_bp, login_bp, user_bp
from .forms import SignupForm, LoginForm, UserForm
from .models import User
from datetime import timedelta
from app.src import db
from werkzeug.security import generate_password_hash
from app.src.movie.models import Movie

@signup_bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)
    if request.method == "GET":
        return render_template("user_account/signup.html", form=form)
    
    elif request.method == "POST" and form.validate_on_submit():
        #Usersテーブルにユーザー追加
        user = User.add_user(form.username.data, form.email.data, form.password.data)
        
        if user:
            #ユーザーログイン
            login_user(user, remember=True, duration=timedelta(seconds=600))
            flash("登録しました", "primary")
            return redirect(url_for('user.user'))
        
        else:
            flash("メールアドレスがすでに存在しています", "danger")
            return render_template("user_account/signup.html", form=form)
    
    return render_template("user_account/signup.html", form=form)


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "GET":
        #ログインページ表示
        return render_template("user_account/login.html", form=form)
    
    elif request.method == "POST" and form.validate_on_submit():
        #メールアドレスが一致するユーザーを取得
        user = User.select_by_email(form.email.data)

        #ユーザー存在確認&パスワード一致確認
        if user and user.check_password(form.password.data):

            #ユーザーログイン
            login_user(user, remember=True, duration=timedelta(seconds=600))
            flash("ログインしました", "primary")
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
        #ユーザー編集ページ表示
        return render_template("user_account/user_edit.html", form=form)
    
    elif request.method == "POST" and form.validate_on_submit():

        #メールアドレスが一致するユーザーを取得
        user = User.select_by_email(current_user.email)

        if user:
            #各種値を変数格納
            user.username = form.username.data
            user.email = form.email.data
            user.password = generate_password_hash(form.password.data)

            #DBコミット
            db.session.commit()
            flash("ユーザー情報を更新しました")
            return render_template("user_account/user_edit.html", form=form)
        else:
            flash('ユーザーが存在しません','danger')
            return render_template("user_account/user_edit.html", form=form)

    return render_template("user_account/user_edit.html", form=form)
    

@user_bp.route("/user/delete", methods=["POST", "GET"])
@login_required
def user_delete():
    if request.method == "POST":
        #ユーザーに紐づく映画をすべて削除
        movies = Movie.query.where(Movie.user_id == current_user.id).all()

        #複数レコードデリート&コミット
        for movie in movies:
            db.session.delete(movie)
        
        db.session.commit()

        #メールアドレスが一致するユーザーを取得
        user = User.select_by_email(current_user.email)
        
        #ユーザデリート&コミット
        db.session.delete(user)
        db.session.commit()
        #ユーザーログアウト
        logout_user()
        
        flash("ユーザーを削除しました")
        return render_template("home/index.html")
    
    return render_template("home/index.html")


@login_bp.route("/logout", methods=["GET"])
@login_required
def logout():

    #ユーザーログアウト
    logout_user()
    flash("ログアウトしました", 'success')
    return render_template("home/index.html")
