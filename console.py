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

team1 = Team("Blackrock",league1, 1,3,4,7)
team_repository.save(team1)
team2 = Team("Clontarf", league1, 2,5,6,12)
team_repository.save(team2)
team3 = Team("Shannon", league1, 4,0,6,18)
team_repository.save(team3)
team4 = Team("Young Munster", league1, 0,0,0,0)
team_repository.save(team4)

team_repository.select_all()

