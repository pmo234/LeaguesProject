import pdb
from models.league import League
from models.team import Team

import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

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

