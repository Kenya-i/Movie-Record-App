from flask import Flask
#from app.app import app

app = Flask(__name__)

@app.route("/index")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)