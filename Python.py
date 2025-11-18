#It is a code that works with Flask.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "site actived"

if __name__ == "__main__":
    app.run(debug=True)
