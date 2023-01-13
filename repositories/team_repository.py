from db.run_sql import run_sql

from models.team import Team
from models.league import League
import repositories.league_repository as league_repository

def save(team):
    sql = "INSERT INTO teams (name, leagues_id, wins,losses,draws,score ) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [team.name, team.leagues.id, team.wins, team.losses, team.draws, team.score]
    results = run_sql(sql, values)
    id = results[0]['id']
    team.id = id
    return team


def select_all():
    teams = []

    sql = "SELECT * FROM teams"
    results = run_sql(sql)

    for row in results:
        league = league_repository.select(row['leagues_id'])
        team = Team(row['name'], league, row['wins'], row['losses'], row['draws'],row['score'], row['id'] )
        teams.append(team)
    return teams


def select(id):
    team = None
    sql = "SELECT * FROM teams WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = league_repository.select(row['leagues_id'])
        team = Team(result['name'], league, result['wins'], result['losses'], result['draws'], result['score'], result['id'] )
    return team


def delete_all():
    sql = "DELETE  FROM teams"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM teams WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(team):
    sql = "UPDATE teams SET (name, leagues_id, wins, losses, draws, score) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [team.name, team.leagues.id, team.wins, team.losses, team.draws,team.score, team.id]
    run_sql(sql, values)

def leagues(team):
    leagues = []

    sql = "SELECT * FROM leagues WHERE team_id = %s"
    values = [team.id]
    results = run_sql(sql, values)

    for row in results:
        league = League(row['name'], row['team_id'], row['id'] )
        leagues.append(league)
    return leagues
