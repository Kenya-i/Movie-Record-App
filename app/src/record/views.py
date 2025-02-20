from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import record_bp
from app.src import db
from app.src.movie.models import Movie

@record_bp.route("/record", methods=["GET", "POST"])
@login_required
def record():
    if request.method == "GET":

        #ユーザーに紐づく映画を見た日付降順・id降順で全て抽出
        movies = Movie.query.where(Movie.user_id == current_user.id).order_by(
                                                                        Movie.date.desc(), 
                                                                        Movie.id.desc()).all()

        return render_template("record/record.html", movies=movies)
    
    return render_template("home/home.html")
    #elif request.method == "POST" and form.validate_on_submit():
        #user = User.add_user(form.username.data, form.email.data, form.password.data)
        #if user:
        #    login_user(user, remember=True, duration=timedelta(seconds=600))
        #    flash("登録しました")
        #    return redirect(url_for('user.user'))
        #else:
        #    flash("メールアドレスがすでに存在しています")
        #    print(user)
        #    return render_template("user_account/signup.html", form=form)