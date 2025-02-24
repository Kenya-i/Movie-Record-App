from app.src import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.src.user_account.models import User
from datetime import datetime

class Movie(db.Model):
    __tablename__ = "movie"
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(db.String(500), nullable=True)
    overview: Mapped[str] = mapped_column(db.String(2000), nullable=True)
    comment: Mapped[str] = mapped_column(db.String(2000), nullable=True)
    date: Mapped[datetime] = mapped_column(db.DateTime, default=datetime.now)
    movie_number: Mapped[int] = mapped_column(db.Integer, nullable=False)
    poster_path: Mapped[str] = mapped_column(db.String(100), nullable=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="movies")
    

    def __init__(self, title, overview, comment, date, movie_number, poster_path, user_id):
        self.title = title
        self.overview = overview
        self.comment = comment
        self.date = date
        self.movie_number = movie_number
        self.poster_path = poster_path
        self.user_id = user_id
    
    #映画追加
    @classmethod
    def add_movie(cls, title, overview, comment, date, movie_number, poster_path, user_id):
        movie = cls(
                title = title,
                overview = overview,
                comment=comment,
                date=date,
                movie_number=movie_number,
                poster_path=poster_path,
                user_id=user_id)
        
        db.session.add(movie)
        db.session.commit()