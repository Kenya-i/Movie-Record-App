from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .models import Base
from flask_login import LoginManager
from flask_migrate import Migrate
#import tmdbsimple
#from tmdbapis import TMDbAPIs
from tmdbapis.api3 import API3

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "login.login"
login_manager.login_message = "ログインしてください"
#tmdb = tmdbsimple
apikey = '47574f56da1ee67ef62869635c0164df'
#v4_access_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0NzU3NGY1NmRhMWVlNjdlZjYyODY5NjM1YzAxNjRkZiIsIm5iZiI6MTczOTgwMzU5Ni41ODA5OTk5LCJzdWIiOiI2N2IzNGJjYzVhY2E1YTcxZDI5ZmQ5YTIiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.dEJR3ICWrq643ULedfduu_kghvxIoF096wHahgJkFM8'
api3 = API3(apikey=apikey)

#tmdb = TMDbAPIs(apikey)
#tmdb = TMDbAPIs(apikey, v4_access_token=v4_access_token)
#tmdb.v4_authenticate()
#.v4_approved()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.urandom(24)
    
    #tmdb.API_KEY = '47574f56da1ee67ef62869635c0164df'
    

    #search = tmdb.Search()
    #response = search.movie(query='a')
    #print(response)
    #for s in search.results:
    #    print(s['title'], s['id'], s['release_date'], s['popularity'])

    

    #ログインマネージャーの初期化
    login_manager.init_app(app)
    

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin_user:m0vie_rec0d@db:5432/MOVIE_RECORD_DB"

    db.init_app(app)
    #Migrate(app,db)
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