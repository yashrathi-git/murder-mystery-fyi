from flask import Flask
from flask_pymongo import MongoClient
from flask_login import LoginManager


client = MongoClient("localhost", 27017)
db = client["FYI"]

app = Flask(__name__)

app.secret_key = "HX"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login.login"


@app.route("/")
def index():
    return "<h1>Hello World"
