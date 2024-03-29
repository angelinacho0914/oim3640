PLAYERS = {
    'Karim Benzema': 93, # player's name: his rating
    'Robert Lewandowski': 94,
    'Kylian Mbappe': 97,
    'Luka Modric': 90,
    'Pedri': 93,
    'Pique': 88,
}

LEGENDARIES = {
    'Lionel Messi': (98, 1.1), # legendary player's name: (his rating, his chemistry booster value)
    'Cristiano Ronaldo': (97, 1.05),
}


class Team:
    """FIFA Ultimate Team"""

    def __init__(self, name, initial_players=None):
        """Initialize team and update squad and information if initial_players is provided
        name: string
        initial_players: a list of strings representing initial players in this team.
        """
        self.name = name
        if initial_players == None:
            initial_players = []
        self.squad = initial_players
        self.sum_of_ratings = 0
        if len(initial_players) > 0:
            for player in initial_players:
                self.sum_of_ratings += PLAYERS[player]
            self.rating = self.sum_of_ratings/len(initial_players)
        else:
            self.rating = self.sum_of_ratings

    def __str__(self):
        """Return a string representation of this team, including team name and squad."""
        if len(self.squad) > 0:
            team_players = ', '.join(self.squad)
            return f'{self.name} has {team_players}. The rating is {self.rating}.'
        else:
            return f'{self.name} has no player yet.' 

    def __gt__(self, another_team):
        return self.rating > another_team.rating

    def choose(self, player):
        """choose one player from PLAYERS and update team's rating which is the average rating of entire current squad.
        player: string
        """
        self.sum_of_ratings = 0
        self.squad.append(player)
        for p in self.squad:
            self.sum_of_ratings += PLAYERS[p]
        self.rating = self.sum_of_ratings/len(self.squad)


    def choose_legendary(self, player):
        """choose one player from LEGENDARIES and update team's rating which is the average rating of entire current squad multiplied by legendary's booster.
        player: string
        """
        self.squad.append(player)
        self.sum_of_ratings += LEGENDARIES[player][0]
        self.rating = self.sum_of_ratings/len(self.squad) * LEGENDARIES[player][1]


#############################################
# Please DO NOT change code in main function!
#############################################
def main():
    real_madrid = Team('Real Madrid', initial_players=['Karim Benzema'])
    barcelona = Team('Barcelona')
    print('Before choosing squad:')
    print(real_madrid)
    print(barcelona)
    print()
    print('After choosing squad:')
    real_madrid.choose('Luka Modric')
    real_madrid.choose('Kylian Mbappe')
    barcelona.choose('Pique')
    barcelona.choose('Pedri')
    barcelona.choose('Robert Lewandowski')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)
    print()
    print('After choosing legendary:')
    real_madrid.choose_legendary('Cristiano Ronaldo')
    barcelona.choose_legendary('Lionel Messi')
    print(real_madrid)
    print(barcelona)
    print()
    print('Will Real Madrid win against Barcelona?')
    print(real_madrid > barcelona)


if __name__ == '__main__':
    main()