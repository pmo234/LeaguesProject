from models.team import Team
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository
import random
from random import choice


class Fixture:
    def __init__(self,round, team1, team2, team1score = 0, team2score = 0, id = None):
        self.round = round
        self.team1 = team1
        self.team2 = team2
        self.team1score = team1score
        self.team2score = team2score
        self.id = id

    def calculate_result(self):
        
        if self.team1score == self.team2score:
            self.team1.draws += 1
            self.team2.draws += 1
            team_repository.update(self.team1)
            team_repository.update(self.team2)
        if self.team1score > self.team2score:
            
            self.team1.wins += 1
            
            self.team2.losses += 1
            team_repository.update(self.team1)
            team_repository.update(self.team2)
        if self.team1score < self.team2score:
            self.team1.losses += 1
            self.team2.wins += 1
            team_repository.update(self.team1)
            team_repository.update(self.team2)

    def set_fixtures(self):
        all_teams = team_repository.select_all()
        all_fixtures = fixture_repository.select_all()
        print(len(all_teams))

        # if len(all_teams) != 2 or len(all_teams) != 4 or len(all_teams) !=8:
        #     return

        if len(all_teams) == 2:
            print("2 teams")
            fixtures = Fixture(1, all_teams[0], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixture_repository.save(fixtures)
            return

        if len(all_teams) == 3:
            print("3 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures2 = Fixture(1, all_teams[0], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures3 = Fixture(1, all_teams[2], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixture_repository.save(fixtures1)
            fixture_repository.save(fixtures2)
            fixture_repository.save(fixtures3)
            return

        if len(all_teams) == 4:
            print("4 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures2 = Fixture(1, all_teams[2], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures3 = Fixture(1, all_teams[0], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures4 = Fixture(1, all_teams[3], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures5 = Fixture(1, all_teams[0], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures6 = Fixture(1, all_teams[2], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixture_repository.save(fixtures1)
            fixture_repository.save(fixtures2)
            fixture_repository.save(fixtures3)
            fixture_repository.save(fixtures4)
            fixture_repository.save(fixtures5)
            fixture_repository.save(fixtures6)
            return

        if len(all_teams) == 5:
            print("5 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures2 = Fixture(1, all_teams[2], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures3 = Fixture(1, all_teams[0], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures4 = Fixture(1, all_teams[3], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures5 = Fixture(1, all_teams[0], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures6 = Fixture(1, all_teams[2], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures7 = Fixture(1, all_teams[4], all_teams[0], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures8 = Fixture(1, all_teams[4], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures9 = Fixture(1, all_teams[4], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures10 = Fixture(1, all_teams[4], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixture_repository.save(fixtures1)
            fixture_repository.save(fixtures2)
            fixture_repository.save(fixtures10)
            fixture_repository.save(fixtures3)
            fixture_repository.save(fixtures9)
            fixture_repository.save(fixtures4)
            fixture_repository.save(fixtures8)
            fixture_repository.save(fixtures5)
            fixture_repository.save(fixtures6)
            fixture_repository.save(fixtures7)
            return

        if len(all_teams) == 6:
            print("6 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures2 = Fixture(1, all_teams[2], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures3 = Fixture(1, all_teams[0], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures4 = Fixture(1, all_teams[3], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures5 = Fixture(1, all_teams[0], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures6 = Fixture(1, all_teams[2], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures7 = Fixture(1, all_teams[4], all_teams[0], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures8 = Fixture(1, all_teams[4], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures9 = Fixture(1, all_teams[4], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures10 = Fixture(1, all_teams[4], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures11 = Fixture(1, all_teams[5], all_teams[0], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures12 = Fixture(1, all_teams[5], all_teams[1], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures13 = Fixture(1, all_teams[5], all_teams[2], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures14 = Fixture(1, all_teams[5], all_teams[3], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixtures15 = Fixture(1, all_teams[5], all_teams[4], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
            fixture_repository.save(fixtures1)
            fixture_repository.save(fixtures2)
            fixture_repository.save(fixtures15)
            fixture_repository.save(fixtures10)
            fixture_repository.save(fixtures3)
            fixture_repository.save(fixtures14)
            fixture_repository.save(fixtures9)
            fixture_repository.save(fixtures4)
            fixture_repository.save(fixtures13)
            fixture_repository.save(fixtures8)
            fixture_repository.save(fixtures12)
            fixture_repository.save(fixtures5)
            fixture_repository.save(fixtures6)
            fixture_repository.save(fixtures11)
            fixture_repository.save(fixtures7)
            return



        # current_round = [all_teams[0].wins + all_teams[0].losses + all_teams[0].draws]
        # # for team in all_teams:
        # #     if current_round.count(team.wins + team.losses + team.draws) == 0:
        # #         current_round.append(team.wins + team.losses + team.draws)
                
        # fixtures = {}
        # print(current_round)
        # for x in range(0, len(all_teams)):
        #     y = len(all_teams) -x-1
        #     if y <= x:
        #         fixture_repository.save(fixtures["match{0}".format(x)])
        #         break
        #     fixtures["match{0}".format(x+1)] = Fixture(all_teams[x].wins + all_teams[x].losses + all_teams[x].draws,all_teams[x], all_teams[y], choice([i for i in range(0,50)]), choice([i for i in range(0,50)]))

        
            # for played_fixtures in all_fixtures:
            #     i += 1
            #     if fixtures["match{0}".format(x+1)].team1 != played_fixtures.team1 and fixtures["match{0}".format(x+1)].team2 != played_fixtures.team2 and x == i:
            #         j+=1
            #         print('hello')
            #         print(len(fixtures["match{0}".format(x+1)]))
            #         if j >= len(all_teams):
            #             break
            # if current_round[len(current_round)-1] == 0:
            #     print("Round")
            #     fixture_repository.save(fixtures["match{0}".format(x+1)])


