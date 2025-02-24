from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .models import Base
from flask_login import LoginManager
from dotenv import load_dotenv
from tmdbapis.api3 import API3
from flask_bootstrap import Bootstrap5
from opensubtitlescom import OpenSubtitles

app = Flask(__name__)
db = SQLAlchemy()

#ログインマネージャー設定
login_manager = LoginManager()
login_manager.login_view = "login.login"
login_manager.login_message = "ログインしてください"

#APIキー設定・取得
load_dotenv()
app.config['TMDB_API_KEY'] = os.environ.get('TMDB_API_KEY')
app.config['SUBTITLES_APP_VERSION'] = os.environ.get('SUBTITLES_APP_VERSION')
app.config['SUBTITLES_API_KEY'] = os.environ.get('SUBTITLES_API_KEY')
app.config['SUBTITLES_USER_NAME'] = os.environ.get('SUBTITLES_USER_NAME')
app.config['SUBTITLES_LOGIN_ID'] = os.environ.get('SUBTITLES_LOGIN_ID')
api3 = API3(apikey=app.config['TMDB_API_KEY'])
subtitles = OpenSubtitles(app.config['SUBTITLES_APP_VERSION'], app.config['SUBTITLES_API_KEY'])
subtitles.login(app.config['SUBTITLES_USER_NAME'], app.config['SUBTITLES_LOGIN_ID'])

#bootstrap設定
bootstrap = Bootstrap5(app)

def setup():

    #config設定
    app.config["SECRET_KEY"] = os.urandom(24)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    #ログインマネージャーの初期化
    login_manager.init_app(app)
    
    #DB初期化
    db.init_app(app)
    db.model_class = Base
    
    #Blueprint読み込み
    from .home import home_bp
    from .movie import movie_bp
    from .user_account import signup_bp
    from .user_account import login_bp
    from .user_account import user_bp
    from .record import record_bp
    from .search import search_bp

    #Blueprint設定
    app.register_blueprint(home_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(record_bp)
    app.register_blueprint(search_bp)

    #DB作成
    with app.app_context():
        db.create_all()

    return app
