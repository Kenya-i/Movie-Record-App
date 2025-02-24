from app.src import db,login_manager
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from uuid import uuid4
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    age: Mapped[int] = mapped_column(db.Integer, nullable=True)
    image_path: Mapped[str] = mapped_column(db.Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)
    movies: Mapped[List["Movie"]] = relationship(back_populates="user")

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    #ユーザー追加
    @classmethod
    def add_user(cls, username, email, password):
        try:
            #引数で渡されたパスワードをハッシュ化
            hashed_password = generate_password_hash(password)

            #Userインスタンス作成&ユーザー追加・コミット
            user = cls(username=username, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return user
        
        except IntegrityError as sqlalchemy_error:
            #db.session.rollback()
            user = None
            return user
    
    #メールアドレスが一致するユーザーを取得
    @classmethod
    def select_by_email(cls, email):
        return cls.query.where(cls.email == email).one_or_none()
    
    #@classmethod
    #def select_by_id(cls, id):
    #    return cls.query.where(cls.id == id).one_or_none()
    
    #DB内のハッシュ化済みパスワードと渡されてきたパスワードを比較
    def check_password(self, password):
        return check_password_hash(self.password, password)