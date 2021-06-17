from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html") 

@app.route("/articles")
@app.route("/articles/<string:page>")
def articles(page=None):
    if page is None:
        return render_template("articles.html")
    return render_template(f"articles_{page}.html")
