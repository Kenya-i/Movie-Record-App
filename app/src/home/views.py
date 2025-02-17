from flask import render_template
from . import home_bp
from app.src import tmdb

@home_bp.route("/")
def home():
    search = tmdb.Search()
    response = search.movie(query='クレヨンしんちゃん')
    
    return render_template("home/index.html", response=response)