from sqlalchemy import Column, Integer, String, Float, DateTime
#from db.connection import Engine
from .db.connection import Base, Engine

class User(Base):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(255), nullable=False)
    email = Column("email", String(255), nullable=False, unique=True)
    age = Column("age", Integer)
    password = Column("password", String(64), nullable=False)
    #image = Column(LargeBinary)
    #createdAt = Column("createdAt", DateTime)
    #updatedAt = Column("updatedAt", DateTime)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

Base.metadata.create_all(bind=Engine)