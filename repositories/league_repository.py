from db.run_sql import run_sql

from models.league import League
from models.team import Team
import repositories.team_repository as team_repository


def save(league):
    sql = "INSERT INTO leagues (name) VALUES (%s) RETURNING *"
    values = [league.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    league.id = id
    return league


def select_all():
    leagues = []
    print('select all leagues activated')
    sql = "SELECT * FROM leagues"
    results = run_sql(sql)

    for row in results:
        # team = team_repository.select(row['teams_id'])
        league = League(row['name'], row['id'] )
        leagues.append(league)
    return leagues



def select(id):
    league = None
    sql = "SELECT * FROM leagues WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        league = League(result['name'], result['id'] )
    return league


def delete_all():
    sql = "DELETE  FROM leagues"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM leagues WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(league):
    sql = "UPDATE leagues SET (name, team_id) = (%s, %s) WHERE id = %s"
    values = [league.name, league.teams.id, league.duration, league.completed, league.id]
    run_sql(sql, values)
