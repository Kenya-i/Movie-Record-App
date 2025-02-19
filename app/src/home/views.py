from flask import render_template
from . import home_bp

@home_bp.route("/")
def home():
    #search = tmdb.Search()
    #response = search.movie(query='クレヨンしんちゃん')
    
    return render_template("home/index.html")