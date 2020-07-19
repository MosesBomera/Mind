# Standard library imports.
import os

# Related third party code.
from flask import Flask, session, render_template, request, redirect
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import requests

# Custom libraries.
from login import Login
from forms import LoginForm
from models import *

app = Flask(__name__)

# Check environment variables.
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE NOT SET.")
else:
    DATABASE_URL = os.getenv("DATABASE_URL")

if not os.getenv("SECRET_KEY"):
    raise RuntimeError("SECRET KEY NOT FOUND.")
else:
    SECRET_KEY = os.getenv("SECRET_KEY")

# Configure session to use filesystem.
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/", methods=["POST", "GET"])
def index():
    """
    Landing page:
        Presents the visitor with a login form.
        Username: jane_doe
        Password: ********

    If not registered, the option is to register is just down
    below.
    """

    loginform = LoginForm()
    if loginform.validate_on_submit():
        username = loginform.username.data
        password = loginform.password.data

        # Verification

        # Start the session
        session["username"] = username

        return redirect("/home")
    return render_template("index.html", loginform=loginform)


@app.route("/home", methods=["POST"])
def home():
    """
        Question?
        Hi, first_name?
        Talk to someone?
        Talk to an AI?
    """

    # Log visitor in.
    return render_template("home.html")


@app.route("/mind", methods=["POST", "GET"])
@Login.logged_in
def mind():
    """
        The chat with the person/ai.
    """
    return render_template("mind.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    """
    Register a new user.
    Fields:
        Email: janedoe@mind.com
        Username: jane_doe
        Full Name: Jane Doe
        Password: ********
        verify_password: ********
    """

    # Check the kind of URL submission method.
    if request.method == "POST":
        # Get the new user's credentials.
        username = request.form.get("username")
        email = request.form.get("email")
        fullname = request.form.get("fullname")
        password = request.form.get("password")

    # Db functions


@app.route("/logout")
def logout():
    """
        Let's the user logout of the application.
    """
    # Remove all credentials associated to the user.
    session.pop('username', None)
    session.pop('fullname', None)
    session.pop('id', None)

    return render_template("index.html")
