import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello! I am Binit Shah. This is my website."

if __name__ == "__main__":
    app.run()
