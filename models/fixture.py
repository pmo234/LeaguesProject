

class Fixture:
    def __init__(self,round, team1, team2, team1score = 0, team2score = 0, id = None):
        self.round = round
        self.team1 = team1
        self.team2 = team2
        self.team1score = team1score
        self.team2score = team2score
        self.id = id

    def calculate_result(team1score, team2score):
        if team1score == team2score:
