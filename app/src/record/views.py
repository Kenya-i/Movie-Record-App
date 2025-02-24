from flask import render_template, request
from flask_login import login_required, current_user
from . import record_bp
from app.src.movie.models import Movie
from flask_paginate import Pagination, get_page_parameter
from app.src import subtitles
import re
import datetime
from sqlalchemy import func


#ページネーションパラメータのメッセージ日本語化
display_msg='視聴した{record_name}(全<b>{total}</b>件)のうち<b> {start} - {end} </b>件を表示中'

#辞書変換用タプル
sample = ('index', 'start_seconds', 'content')

#1ページ中に表示するレコード件数を10に固定
per_page=10


@record_bp.route("/record", methods=["GET", "POST"])
@login_required
def record():
    if request.method == "GET":

        movies = get_user_movie_group()

        #ページ番号を取得
        page = request.args.get(get_page_parameter(), type=int, default=1)

        #ページネーションパラメータ設定
        pagination = Pagination(page=page, per_page=per_page, total=len(movies), record_name="映画", display_msg=display_msg, css_framework='bootstrap5')

        #何件目から何件目まで取得するかを変数に格納
        start = (page - 1) * per_page
        end = start + per_page

        #表示する件数を指定
        displayed_movies = movies[start:end]

        return render_template("record/record.html", movies=displayed_movies, pagination=pagination)
    
    return render_template("home/home.html")

@record_bp.route("/record/<int:id>", methods=["GET"])
@login_required
def selected_movie(id):
    if request.method == "GET":

        #取得した映画IDに一致するユーザーに紐づく映画を新しく見た日付順ですべて取得
        movies = Movie.query.where(Movie.user_id == current_user.id, Movie.movie_number == id).order_by(Movie.date.desc()).all()

        response = subtitles.search(tmdb_id=movies[0].movie_number, languages="en")

        lists = []

        if response.data:
            #oOpneSubtitlesAPIを用いて映画の字幕をダウンロード
            srt = subtitles.download_and_parse(response.data[0])

            #リストから値をひとつづつ取り出す
            #取り出す形式は Subtitle(index=.*?, start=datetime.timedelta(seconds=.*?, microseconds=.*?), end=datetime.timedelta(seconds=.*?, microseconds=.*?), content='.*?', proprietary='')
            for item in srt:

                #取得したsrtファイル形式の値から正規表現で特定の値を取り出し、タプルを含むリスト形式*で出力  *[()]
                ##Subtitle\(index=(.*?), start=datetime.timedelta\(seconds=(.*?), microseconds=(.*?)\), end=datetime.timedelta.*, content=(\'.*\'|\".*\"), proprietary
                #results = re.findall(r'Subtitle\(index=(.*?[0-9]), start=datetime.timedelta\(seconds=(.*?[0-9]{0,5}).*content=(\'.*\'|\".*\"), proprietary',str(item))
                results = re.findall(r'Subtitle\(index=(.*?[0-9]), start=datetime.timedelta\(seconds=(.*?[0-9]{0,5}).*content=(\'.*\'|\".*\"), proprietary',str(item))
                
                #タプル同士を結合し、辞書化(値が何に対応しているかわかりやすくするため)
                srt_dic = dict(zip(sample, results[0]))
                seconds = int(srt_dic["start_seconds"])

                #秒数を時分秒形式(例 1:30:50)に変換
                srt_dic["start_seconds"] = str(datetime.timedelta(seconds=seconds))
            
                #字幕の余計な文字を削除
                srt_dic["content"] = srt_dic["content"].replace('\\n', ' ').replace('\\\\h', ' ').replace('{\\\\an8}', ' ').replace('<i>', ' ').replace('</i>', ' ')

                lists.append(srt_dic)


            return render_template("record/subtitle.html", movies=movies, lists=lists)
        
        else:

            return render_template("record/subtitle.html", movies=movies, lists=lists)
    

    return render_template("home/index.html")

def get_user_movie_group():

    #ユーザーに紐づく映画をmovie_number(TMDbの映画ID),Movie.title,Movie.poster_path,Movie.overviewでグループ化し、
    #視聴日Movie.dateが一番最近のものから順にmovie_number(TMDbの映画ID),映画の視聴回数,一番最近見た日付,映画タイトル,ポスター画像,あらすじを取得。
    ##select movie_number, count(movie_number), max(date), title, poster_path, overview from movie where user_id = ?
    ###group by movie_number order by max(date) desc;
    movies = Movie.query.with_entities(
                        Movie.movie_number,
                        func.count(Movie.movie_number),
                        func.max(Movie.date),
                        Movie.title,
                        Movie.poster_path,
                        Movie.overview
                                        ).where(Movie.user_id == current_user.id).group_by(
                                                                                    Movie.movie_number,
                                                                                    Movie.title,
                                                                                    Movie.poster_path,
                                                                                    Movie.overview
                                                                                        ).order_by(func.max(Movie.date).desc()).all()

    return movies
        