from app.src import db,login_manager
from sqlalchemy import Column, Integer, String, Float, DateTime
from flask_login import UserMixin
#from flask_bcrypt import Bcrypt
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

#bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    

class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    username = Column("username", String(255), nullable=False)
    email = Column("email", String(255), nullable=False, unique=True)
    age = Column("age", Integer)
    password = Column("password", String(255), nullable=False)
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
            db.session.rollback()
            user = None
            return user
    
    @classmethod
    def select_by_emial(cls, email):
        return cls.query.where(cls.email == email).one_or_none()
    
    def check_password(self, password):
        print(str(self.password))
        print(password)
        return check_password_hash(self.password, password)



#@app.before_request
#def set_login_user_name():
#    global login_user_name
#    login_user_name = current_user.username if current_user.is_authenticated else None