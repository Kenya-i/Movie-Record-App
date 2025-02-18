from app.src import db,login_manager
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List
from uuid import uuid4
from datetime import datetime, timedelta
#from app.src.movie.models import Movie


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
    movies: Mapped[List["Movie"]] = relationship(back_populates="user")
    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)
    #image = Column(LargeBinary)
    #createdAt = Column("createdAt", DateTime)
    #updatedAt = Column("updatedAt", DateTime)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


    @classmethod
    def add_user(cls, username, email, password):
        try:
            hashed_password = generate_password_hash(password)
            user = cls(username=username, email=email, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            return user
        
        except IntegrityError as sqlalchemy_error:
            #db.session.rollback()
            user = None
            return user
    
    @classmethod
    def select_by_email(cls, email):
        return cls.query.where(cls.email == email).one_or_none()
    
    def check_password(self, password):
        print(self.password)
        print(password)
        return check_password_hash(self.password, password)


#class PasswordResetToken(db.Model):
#    __tablename__ = "password_reset_token"

#    id = db.Column(db.Integer, primary_key=True)
#    token = db.Column(db.String(64), unique=True, index=True, server_default=str(uuid4))
#    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
#    expire_at = db.Column(db.DateTime, default=datetime.now)
#    created_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)
#    updated_at: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)

#    def __init__(self, token, user_id, expire_at):
#        self.token = token
#        self.user_id = user_id
#        self.expire_at = expire_at

#    @classmethod
#    def publish_token(cls, user):
#        token = str(uuid4())

#        new_token = cls(
#            token=token,
#            user_id=user.id,
#            expire_at=datetime.now + timedelta(days=1)
#        )

#        db.session.add(new_token)
#        return token




#@app.before_request
#def set_login_user_name():
#    global login_user_name
#    login_user_name = current_user.username if current_user.is_authenticated else None