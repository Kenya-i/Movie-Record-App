from flask import Flask
from .model.user import User
from .model.db.connection import session

app = Flask(__name__)

@app.route("/index")
def index():

    user = User(name="takashi", email="test@test.com", password="a")
    session.add(user)
    session.commit()

    return f"hello, {user.name}"