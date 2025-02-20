from flask import render_template, request, redirect, url_for, flash
from . import movie_bp
from flask_login import login_required, current_user
from .. import api3
from .forms import MovieForm
from app.src.user_account.models import User
from .models import Movie

@movie_bp.route("/movie", methods=["GET"])
@login_required
def movie():
    if request.method == "GET":
        movie = Movie.query.where(Movie.user_id == current_user.id).all()
        return render_template("record/record.html", movie=movie)
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
    form = MovieForm(request.form)
    if request.method == "GET":
        movie = api3.movies_get_details(movie_id=id, language="ja-JP")
        print(movie)
        return render_template("movie/movie_works.html", movie=movie, form=form)
    if request.method == "POST" and form.validate_on_submit():

        #値を変数に割り当て(title=映画タイトル, overview=あらすじ, comment=映画に対するコメント, date=見た日付, poster_path=ポスター画像, api独自の映画ナンバー)
        title = form.title.data
        overview = form.overview.data
        comment = form.comment.data
        date = form.date.data
        poster_path = form.poster_path.data
        movie_number = id

        #Movieテーブルにレコード挿入
        Movie.add_movie(title, overview, comment, date, movie_number, poster_path, current_user.id)
        
        return redirect(url_for("record.record"))
        #return render_template("record/record.html", movies=movies)