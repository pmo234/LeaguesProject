from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.league import League
from models.team import Team
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

leagues_blueprint = Blueprint("leagues", __name__)

@leagues_blueprint.route("/leagues")
def teams():
    teams = team_repository.select_all()
    return render_template("leagues/index.html", all_teams = teams)

@leagues_blueprint.route("/leagues/new")
def leagues():
    leagues = league_repository.select_all()
    return render_template("leagues/new.html", all_leagues = leagues)

@leagues_blueprint.route("/leagues/new", methods=['GET'])
def new_team():
    teams = team_repository.select_all()
    return render_template("leagues/new.html", all_teams = teams)

@leagues_blueprint.route("/leagues",  methods=['POST'])
def create_team():
    name = request.form['name']
    league_id = request.form['league_id']
    wins    = 0
    losses   = 0
    draws   = 0
    score   = 0
    leagues   = league_repository.select(league_id)
    team      = Team(name, leagues, wins, losses,draws,score)
    team_repository.save(team)
    return redirect('/leagues')