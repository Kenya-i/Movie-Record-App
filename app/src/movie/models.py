from app.src import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.src.user_account.models import User

class Movie(db.Model):
    __tablename__ = "movies"
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(db.String(1000), nullable=False)
    original_number: Mapped[int] = mapped_column(db.Integer, nullable=True)
    overview: Mapped[str] = mapped_column(db.String(2000), nullable=True)
    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="movies")
    

    def __init__(self, title):
        self.title = title
        #self.email = email
        #self.password = password