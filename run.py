from app.src import create_app

app = create_app()

#from app.app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)