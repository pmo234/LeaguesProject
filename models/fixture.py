from models.team import Team
import repositories.team_repository as team_repository
import repositories.fixture_repository as fixture_repository
import math
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

    def reset_table(self):
        all_teams = team_repository.select_all()
        for team in all_teams:
            team.wins = 0
            team.losses = 0
            team.draws = 0
            team_repository.update(team)


    # Task: to reset the table
    #   get all the teams from the database
            # FOR each row in teams
                # EDIT the team wins to be equal 0
                # EDIT the team losses to be equal 0
                # EDIT the team draws to be equal 0
                # UPDATE the database with the new values
            #END FOR
            


    def set_fixtures(self):
        all_teams = team_repository.select_all()
        all_fixtures = fixture_repository.select_all()
       
        number_of_teams = list(range(0, len(all_teams)))
        
        number_of_teams2 = list(range(0, len(all_teams)))
        all_matches = {}
        match_number = 0
        if len(all_teams)>6:
            for first_team in number_of_teams:
                
                for second_team in number_of_teams2:
                    if first_team == second_team:
                        print("equal")
                    else:
                        match_number+=1

                        fixtures = Fixture(1, all_teams[number_of_teams[first_team]], all_teams[number_of_teams[second_team]], choice([i for i in range(0,5)]), choice([i for i in range(0,5)]))
                        all_matches.update({'match'+str(match_number): fixtures})
                        fixture_repository.save(fixtures)
                        
                number_of_teams2.pop(0)
        # i = math.floor(len(all_teams)/2)
        # print(i)
        # played_matches = []
        # # while all_matches:
        # for match in all_matches.values():
                
        #     j=-1
        #     while j < i:
        #         j+=1

        # for team1 in number_of_teams:
        #     for team2 in number_of_teams:


        
             

        

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

    def input_fixtures(self,scores):
        

        all_teams = team_repository.select_all()
        all_fixtures = fixture_repository.select_all()
        number_of_teams = list(range(0, len(all_teams)))
        print(number_of_teams)
        number_of_teams2 = list(range(0, len(all_teams)))
        accessing_scores_a = []
        accessing_scores_b = []
        match_number = 0
        if len(all_teams)>6:
            for first_team in number_of_teams:
                print(first_team)
                for second_team in number_of_teams2:
                    if first_team == second_team:
                        print("equal")
                    else:
                        match_number+=1
                        print(match_number)
                        print(1, all_teams[number_of_teams[first_team]], all_teams[number_of_teams[second_team]], scores['a'+ str(match_number)], scores["b"+ str(match_number)])
                        fixtures = Fixture(1, all_teams[number_of_teams[first_team]], all_teams[number_of_teams[second_team]], scores['a'+ str(match_number)], scores["b"+ str(match_number)])
                        fixture_repository.save(fixtures)
                number_of_teams2.pop(0)

            
        if len(all_teams) == 2:
            print("2 teams")
            fixtures = Fixture(1, all_teams[0], all_teams[1], scores['a1'], scores['b1'])
            fixture_repository.save(fixtures)
            return

        if len(all_teams) == 3:
            print("3 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], scores['a1'], scores['b1'])
            fixtures2 = Fixture(1, all_teams[0], all_teams[2], scores['a2'], scores['b2'])
            fixtures3 = Fixture(1, all_teams[2], all_teams[1], scores['a3'], scores['b3'])
            fixture_repository.save(fixtures1)
            fixture_repository.save(fixtures2)
            fixture_repository.save(fixtures3)
            return

        if len(all_teams) == 4:
            print("4 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], scores['a1'], scores['b1'])
            fixtures2 = Fixture(1, all_teams[0], all_teams[2], scores['a2'], scores['b2'])
            fixtures3 = Fixture(1, all_teams[2], all_teams[1], scores['a3'], scores['b3'])
            fixtures4 = Fixture(1, all_teams[3], all_teams[1], scores['a4'], scores['b4'])
            fixtures5 = Fixture(1, all_teams[0], all_teams[3], scores['a5'], scores['b5'])
            fixtures6 = Fixture(1, all_teams[2], all_teams[3], scores['a6'], scores['b6'])
            fixture_repository.save(fixtures1)
            fixture_repository.save(fixtures2)
            fixture_repository.save(fixtures3)
            fixture_repository.save(fixtures4)
            fixture_repository.save(fixtures5)
            fixture_repository.save(fixtures6)
            return

        if len(all_teams) == 5:
            print("5 teams")
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], scores['a1'], scores['b1'])
            fixtures2 = Fixture(1, all_teams[2], all_teams[3], scores['a2'], scores['b2'])
            fixtures3 = Fixture(1, all_teams[0], all_teams[2], scores['a3'], scores['b3'])
            fixtures4 = Fixture(1, all_teams[3], all_teams[1], scores['a4'], scores['b4'])
            fixtures5 = Fixture(1, all_teams[0], all_teams[3], scores['a5'], scores['b5'])
            fixtures6 = Fixture(1, all_teams[2], all_teams[1], scores['a6'], scores['b6'])
            fixtures7 = Fixture(1, all_teams[4], all_teams[0], scores['a7'], scores['b7'])
            fixtures8 = Fixture(1, all_teams[4], all_teams[1], scores['a8'], scores['b8'])
            fixtures9 = Fixture(1, all_teams[4], all_teams[2], scores['a9'], scores['b9'])
            fixtures10 = Fixture(1, all_teams[4], all_teams[3], scores['a10'], scores['b10'])
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
            fixtures1 = Fixture(1, all_teams[0], all_teams[1], scores['a1'], scores['b1'])
            fixtures2 = Fixture(1, all_teams[2], all_teams[3], scores['a2'], scores['b2'])
            fixtures3 = Fixture(1, all_teams[0], all_teams[2], scores['a3'], scores['b3'])
            fixtures4 = Fixture(1, all_teams[3], all_teams[1], scores['a4'], scores['b4'])
            fixtures5 = Fixture(1, all_teams[0], all_teams[3], scores['a5'], scores['b5'])
            fixtures6 = Fixture(1, all_teams[2], all_teams[1], scores['a6'], scores['b6'])
            fixtures7 = Fixture(1, all_teams[4], all_teams[0], scores['a7'], scores['b7'])
            fixtures8 = Fixture(1, all_teams[4], all_teams[1], scores['a8'], scores['b8'])
            fixtures9 = Fixture(1, all_teams[4], all_teams[2], scores['a9'], scores['b9'])
            fixtures10 = Fixture(1, all_teams[4], all_teams[3], scores['a10'], scores['b10'])
            fixtures11 = Fixture(1, all_teams[5], all_teams[0], scores['a11'], scores['b11'])
            fixtures12 = Fixture(1, all_teams[5], all_teams[1], scores['a12'], scores['b12'])
            fixtures13 = Fixture(1, all_teams[5], all_teams[2], scores['a13'], scores['b13'])
            fixtures14 = Fixture(1, all_teams[5], all_teams[3], scores['a14'], scores['b14'])
            fixtures15 = Fixture(1, all_teams[5], all_teams[4], scores['a15'], scores['b15'])
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


