from flask import render_template, request, flash
from flask_login import login_required
from . import search_bp
from .forms import SearchForm
import urllib.parse
from .. import api3

@search_bp.route("/search", methods=["GET", "POST"])
@login_required
def search():
    form = SearchForm(request.form)
    if request.method == "GET":
        #検索ページ表示
        return render_template("search/search.html", form=form)
    elif request.method == "POST" and form.validate_on_submit():
        
        #検索対象文字列のURLエンコード
        search_word = urllib.parse.quote(form.title.data)
        #TMDbAPIで映画情報取得
        responses = api3.search_search_movies(query=search_word,  language="ja-JP", region="JP")
        movies = responses["results"]

        return render_template("movie/movie.html", form=form, movies=movies)
    
    flash('エラーが発生しました', 'danger')
    return render_template("search/search.html", form=form)