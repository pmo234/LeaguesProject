from db.run_sql import run_sql

from models.team import Team
from models.league import League
from models.fixture import Fixture
import repositories.league_repository as league_repository
import repositories.team_repository as team_repository


def save(fixture):
    sql = "INSERT INTO fixtures (round, team1_id, team2_id ,team1score,team2score ) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [fixture.round, fixture.team1.id, fixture.team2.id, fixture.team1score, fixture.team2score]
    results = run_sql(sql, values)
    id = results[0]['id']
    fixture.id = id
    update_score()
    return fixture


def select_all():
    fixtures = []

    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)

    if fixtures == []:
        for row in results:
        
            team1 = team_repository.select(row['team1_id'])
            team2 = team_repository.select(row['team2_id'])
            fixture = Fixture(row['round'], team1, team2, row['team1score'], row['team2score'], row['id'] )
            
            fixtures.append(fixture)
        
        return fixtures

def update_score():
    fixtures = []

    sql = "SELECT * FROM fixtures"
    results = run_sql(sql)

    if results ==[]:
        fixture = Fixture(0,"a","b",0,0)
        fixture.set_fixtures()
    else:
         team1 = team_repository.select(results[len(results)-1]['team1_id'])
         team2 = team_repository.select(results[len(results)-1]['team2_id'])
         fixture = Fixture(results[len(results)-1]['round'], team1, team2, results[len(results)-1]['team1score'], results[len(results)-1]['team2score'], results[0]['id'] )
         fixture.calculate_result()
         fixtures.append(fixture)
                
         return fixtures



def select(id):
    fixture = None
    sql = "SELECT * FROM fixtures WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        team1 = team_repository.select(result['team1_id'])
        team2 = team_repository.select(result['team2_id'])
        fixture = Fixture(result['round'], team1, team2, result['team1score'], result['team2score'], result['id'] )
    return fixture


def delete_all():
    sql = "DELETE FROM fixtures"
    team_repository.delete_all()
    
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM fixtures WHERE id = %s"
    print("Deleting fixture")
    values = [id]
    run_sql(sql, values)


def update(fixture):
    sql = "UPDATE fixtures SET (round, team1_id, team2_id, team1score, team2score) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [fixture.round, fixture.team1.id, fixture.team2.id, fixture.team1score, fixture.team2score, fixture.id]
    print(fixture.team1.wins)
    # values.
    run_sql(sql, values)

# def leagues(fixture):
#     leagues = []

#     sql = "SELECT * FROM leagues WHERE team_id = %s"
#     values = [fixture.id]
#     results = run_sql(sql, values)

#     for row in results:
#         league = League(row['round'], row['team_id'], row['id'] )
#         leagues.append(league)
#     return leagues
