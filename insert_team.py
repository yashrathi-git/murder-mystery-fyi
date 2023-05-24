from dataclasses import asdict
from murder_mystery.login import Team, db


def insert_team(team: Team):
    team_data = asdict(team)
    db["teams"].insert_one(team_data)


team = Team(team_name="test", password="test")
insert_team(team)
