from flask import render_template, request, redirect, url_for, flash
from . import movie_bp
from flask_login import login_required, current_user
from .. import api3

@movie_bp.route("/movie", methods=["GET", "POST"])
@login_required
def movie():
    pass
#    form = SignupForm(request.form)
#    if request.method == "GET":
#        return render_template("user_account/signup.html", form=form)
        
#    elif request.method == "POST" and form.validate_on_submit():
#        user = User.add_user(form.username.data, form.email.data, form.password.data)
#        print(user.password)
#        if user:
#            flash("登録しました")
            #ちゃんとしたredirectを後で書く
#            return render_template("user_account/signup.html", form=form)
#        else:
#            flash("メールアドレスがすでに存在しています")
#            return render_template("user_account/signup.html", form=form)


@movie_bp.route("/movie/<int:id>", methods=["GET", "POST"])
@login_required
def movie_works(id):
    if request.method == "GET":
        movie = api3.movies_get_details(movie_id=id, language="ja-JP")
        print(movie)
        return render_template("movie/movie_works.html", movie=movie)
    if request.method == "POST":
        print(id)
        pass