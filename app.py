from flask import Flask, render_template, make_response


app = Flask(__name__)


USER_TYPES_MAP = {
    # See UsersModel for more
    "mi": "medical institution",
    "ms": "medical supply vendor",
}

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


@app.route("/login/<string:user_type>")
def login(user_type):
    """
    Renders the login pages for mi: medical institutions and ms: medical suppliers

    Args:
        user_type (str): Type of the user. See UsersModel for more
    """
    expanded_user_type = USER_TYPES_MAP.get(user_type)
    if expanded_user_type is None:
        return make_response("Unknown User", 404)
    return render_template("login.html", user_type=expanded_user_type)


@app.route("/supplies")
def supplies():
    """
    Renders the supplies request/offer page

    """
    return render_template("supplies.html")

