import pdb
from models.league import League
from models.team import Team
from models.fixture import Fixture
import random

import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

league_repository.delete_all()
team_repository.delete_all()
league1 = League("League 1")
league_repository.save(league1)
league2 = League("League 2")
league_repository.save(league2)

team1 = Team("Blackrock",league1, 199,3,4,100)
team_repository.save(team1)
team2 = Team("Clontarf", league1, 2,5,6,101)
team_repository.save(team2)
team3 = Team("Shannon", league2, 4,0,6,189889)
team_repository.save(team3)
team4 = Team("Young Munster", league2, 5,8,2,20)
team_repository.save(team4)

team_repository.select_all()

all_teams = team_repository.select_all()

fixture1 = Fixture(1,team1, team2, 42 ,17)
# fixture_repository.save(fixture1)



fixtures = {}
for x in range(0, len(all_teams)):
    y = len(all_teams) -x-1
    if y <= x:
        break
    fixtures["match{0}".format(x+1)] = Fixture(1,all_teams[x], all_teams[y], random.randrange(3,51), random.randrange(3,51))
    print(fixtures["match{0}".format(x+1)])
    fixture_repository.save(fixtures["match{0}".format(x+1)])
print(len(fixtures))

# for fixture in fixtures:
    # print(fixture)
    # fixture_repository.save(fixture)


