from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def homepage():
    """
    Renders the landing / dashboard page
    """
    return render_template("index.html") 


@app.route("/articles")
@app.route("/articles/<string:page>")
def articles(page=None):
    """
    Renders the articles and individual article pages

    Args:
        page (str): article page id
    """
    if page is None:
        return render_template("articles.html")
    return render_template(f"articles_{page}.html")


@app.route("/questionnaire")
@app.route("/questionnaire/<string:page>")
def questionnaires(page=None):
    """
    Renders the questionnaire and individual questionnaire pages

    Args:
        page (str): questionnaire page id
    """
    if page is None:
        return render_template("questionnaire.html")
    return render_template(f"questionnaire_{page}.html")

