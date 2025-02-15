#確認できるまで消さないで

#from app.src import db,login_manager
#from sqlalchemy import Column, Integer, String, Float, DateTime
#from flask_login import UserMixin


#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))
    

#class User(UserMixin, db.Model):
#    __tablename__ = "users"
    
#    id = Column("id", Integer, primary_key=True, autoincrement=True)
#    username = Column("username", String(255), nullable=False)
#    email = Column("email", String(255), nullable=False, unique=True)
#    age = Column("age", Integer)
#    password = Column("password", String(255), nullable=False)
#    #image = Column(LargeBinary)
#    #createdAt = Column("createdAt", DateTime)
#    #updatedAt = Column("updatedAt", DateTime)

#    def __init__(self, name, email, password):
#        self.name = name
#        self.email = email
#        self.password = password


#    @classmethod
#    def add_user(cls, username, email, password):
#        hashed_password = bcrypt.generate_password_hash(password)
#        user = cls(username=username, email=email, password=hashed_password)
#        db.session.add(user)
#        db.session.commit()
#        return user



##@app.before_request
##def set_login_user_name():
##    global login_user_name
##    login_user_name = current_user.username if current_user.is_authenticated else None