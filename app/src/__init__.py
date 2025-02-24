from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .models import Base
from flask_login import LoginManager
from flask_migrate import Migrate
from dotenv import load_dotenv
from tmdbapis.api3 import API3
from flask_bootstrap import Bootstrap5
#from .config import DevelopmentConfig, TestingConfig, ProductionConfig
from opensubtitlescom import OpenSubtitles

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login.login"
login_manager.login_message = "ログインしてください"

load_dotenv()
#app.config['API_KEY'] = os.environ.get('API_KEY')
apikey = ''
api3 = API3(apikey=apikey)


#消さない
#subtitles = OpenSubtitles("Movie-Record-App v1.0.0", " ")

#消さない
#subtitles.login("", "")



app = Flask(__name__)
bootstrap = Bootstrap5(app)


def create_app():
    

    

    app.config["SECRET_KEY"] = os.urandom(24)

    #ログインマネージャーの初期化
    login_manager.init_app(app)
    
    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    db.model_class = Base
    

    from .home import home_bp
    from .movie import movie_bp
    from .user_account import signup_bp
    from .user_account import login_bp
    from .user_account import user_bp
    from .record import record_bp
    from .search import search_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(movie_bp)
    app.register_blueprint(signup_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(record_bp)
    app.register_blueprint(search_bp)

    with app.app_context():
        db.create_all()

    return app