from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import search_bp
from app.src import db
from .forms import SearchForm
#from .. import tmdb
#from tmdb3 import searchMovie
import urllib.parse
from .. import api3
import requests



@search_bp.route("/search", methods=["GET", "POST"])
@login_required
def search():
    form = SearchForm(request.form)
    if request.method == "GET":
        return render_template("search/search.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        
        search_word = urllib.parse.quote(form.title.data)
        responses = api3.search_search_movies(query=search_word,  language="ja-JP", region="JP")
        movies = responses["results"]
        print(responses["results"])

        return render_template("movie/movie.html", form=form, movies=movies)
    
    flash('エラーが発生しました', 'danger')
    return render_template("search/search.html", form=form)


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