from flask import Blueprint, request, render_template, redirect, url_for
from dataclasses import dataclass, asdict
from murder_mystery import login_manager, db
from flask_login import login_user

login_app = Blueprint("login", __name__)


@dataclass
class Team:
    team_name: str
    password: str

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.team_name  # Use team_name as the ID


@login_manager.user_loader
def load_team(team_name):
    team = db["teams"].find_one({"team_name": team_name})
    if team:
        return Team(team_name=team["team_name"], password=team["password"])
    return None


@login_app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        team_name = request.form["team_name"]
        team_password = request.form["password"]
        team = db["teams"].find_one({"team_name": team_name, "password": team_password})
        if team:
            team = Team(team_name=team_name, password=team_password)
            login_user(team)
            return redirect(url_for("game.quiz"))
        return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")
