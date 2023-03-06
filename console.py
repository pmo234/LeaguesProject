import pdb
from models.league import League
from models.team import Team
# from models.fixture import Fixture
import random

import repositories.league_repository as league_repository
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository

league_repository.delete_all()
team_repository.delete_all()
league1 = League("League 1")
league_repository.save(league1)
# league2 = League("League 2")
# league_repository.save(league2)




