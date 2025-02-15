from flask import Flask, render_template
from .model.user import User
from .routing.user import user_bp
from .model.db.connection import session

app = Flask(__name__)

app.register_blueprint(user_bp)

@app.route("/")
def index():

    #user = User(name="kenji", email="test2@test.com", password="a")
    #session.add(user)
    #session.commit()

    return render_template("index.html")