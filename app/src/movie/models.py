from app.src import db
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Movie(db.Model):
    __tablename__ = "movies"
    
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(db.String(1000), nullable=False)
    original_number: Mapped[int] = mapped_column(db.Integer, nullable=False)
    overview: Mapped[str] = mapped_column(db.String(2000), nullable=True)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password