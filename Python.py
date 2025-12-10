#It is a code that works with Flask.

from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('your html file') 

if __name__ == "__main__":
    app.run(debug=True)
