class Team:
    def __init__(self, name, leagues, wins = 0, losses = 0, draws = 0, score = 0, id = None):
        self.name = name
        self.leagues = leagues
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.score = score
        self.id = id

    def calculate_score(self):
        self.score = self.wins*3 + self.draws
