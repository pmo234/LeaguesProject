import pdb
from models.league import League
from models.team import Team

import repositories.league_repository as league_repository
import repositories.team_repository as team_repository

league_repository.delete_all()
team_repository.delete_all()

team1 = Team("Blackrock", 1,3,4,7)
team_repository.save(team1)
team2 = Team("Clontarf", 2,5,6,12)
team_repository.save(team1)
team_repository.save(team2)

team_repository.select_all()

league1 = League("League 1", team1)
league_repository.save(league1)
