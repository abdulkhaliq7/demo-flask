from flask import Flask
app = Flask(__name__)

@app.route("/")
def first_page():
    return "<h1>Testing App </h1>"

@app.route("/yo")
def hello():
    return "<h1>YOOOOOOOOOOOOOOOOOOO </h1>"


if __name__ == "__main__":
    app.run()