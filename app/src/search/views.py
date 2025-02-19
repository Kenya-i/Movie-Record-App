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
        #image = api3.movies_get_images(movie_id=350, language="ja-JP")
        #print(image)
        #print(image["posters"])


        #response = requests.get("https://image.tmdb.org/t/p/w500/n4nXOWVOn3Y2zYqtsMSQusVVxBt.jpg")
        
        #print(response.url)
        search_word = urllib.parse.quote(form.title.data)
        print(search_word)
        responses = api3.search_search_movies(query=search_word,  language="ja-JP", region="JP")
        movies = responses["results"]
        print(responses["results"])
        info = {}
        #for movie in movies:
        #    id = movie["id"]
        #    title = movie["title"]
        #    overview = movie["overview"]
        #    release_date = movie["release_date"]
        #    image = movie["poster_path"]
        #    info.update(movie_id=id, title=title, overview=overview, release_date=release_date, image=image)

        #responses = search.movie(query=form.title.data)
        #responses.page = "2"
        #print(form.title.data)
        #responses = searchMovie('クレヨンしんちゃん')
        #form.title.data = ""
        return render_template("movie/movie.html", form=form, movies=movies) #, result=result 


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