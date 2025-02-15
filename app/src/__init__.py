from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from .models import Base
from flask_login import LoginManager
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = os.urandom(24)
    
    #ログインマネージャーの初期化
    login_manager.init_app(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin_user:m0vie_rec0d@db:5432/MOVIE_RECORD_DB"

    db.init_app(app)
    #Migrate(app,db)
    db.model_class = Base
    


    from .user import user_bp
    from .signup import signup_bp
    from .home import home_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(signup_bp)

    with app.app_context():
        db.create_all()

    return app