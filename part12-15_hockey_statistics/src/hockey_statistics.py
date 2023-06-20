# Write your solution here

# Create a class Player. class Player should include the following parametres:
    # Player's name 
    # Player's nationality 
    # Player's assists
    # Player's goals 
    # Player's penalties
    # Player's team ?
    # Player's games

# Create a class Team, which consists of all players from a certain team 
# Create a class AllTeams
# Create a class UserApplication
    # Input name of file 

# FUNCTIONS
# Function: search for single player's stats
# List all the abbreviations for team names in alphabetical order
# List all the abbreviations for countries in alphabetical order
# ------------------------------------

import json

class Player: 
    def __init__(self, name: str, nationality: str, assists: int, 
                 goals: int, penalties: int, team: str, games: int):
        self.__name = name 
        self.__nationality = nationality
        self.__assists = assists
        self.__goals = goals
        self.__penalties = penalties
        self.__team = team
        self.__games = games
    
    def __str__(self) -> str:
        return f"{self.__name : <21}{self.__team : >3} {self.__goals : >3} + {self.__assists : >2} = {self.__assists + self.__goals :>3}"
    
    def name(self): 
        return self.__name
    
    def team(self):
        return self.__team
    
    def country(self): 
        return self.__nationality
    
    def points(self): 
        return self.__goals + self.__assists
    
    def goals(self):
        return self.__goals
    
    def games(self): 
        return self.__games
   
class AllPlayers: 
    def __init__(self) -> None:
        self.__all_players = []

    def read_file(self, file_name: str): 
        with open(file_name) as f: 
            data = f.read()
            f.close()
        player_data = json.loads(data)
        return player_data
    
    def add_player(self, player: dict):
        self.__all_players.append(Player(
                player["name"],
                player["nationality"],
                player["assists"],
                player["goals"],
                player["penalties"],
                player["team"],
                player["games"]))
        
    def all_players(self): 
        return self.__all_players
    
    def search_by_name(self, name: str): 
        for player in self.__all_players: 
            if player.name() == name: 
                return player
        return None
    
    def team_names_abbr(self): 
        return sorted(set([player.team() for player in self.__all_players]))
    
    def countries_abbr(self): 
        return sorted(set([player.country() for player in self.__all_players]))

    def order_players_from_team(self, team: str): 
        if team not in [player.team() for player in self.__all_players]:
            return None
        return sorted(
            [player for player in self.__all_players if player.team() == team], 
            key=lambda player: player.points(), 
            reverse=True
            )
    
    def order_players_from_country(self, country: str):
        if country not in [player.country() for player in self.__all_players]:
            return None
        return sorted(
            [player for player in self.__all_players if player.country() == country], 
            key=lambda player: player.points(), 
            reverse=True
            )
    
    def players_with_most_points(self): 
        return sorted(self.__all_players, key=lambda player: (player.points(), player.goals()), reverse=True)
    
    def players_with_most_goals(self):
        return sorted(self.__all_players, key=lambda player: (player.goals(), -player.games()), reverse=True)
        
class UserApplication: 
    def __init__(self):
        self.__all_players = AllPlayers()
    
    def help(self): 
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")
    
    def execute(self): 
        file_name = input("file name: ")
        player_data = self.__all_players.read_file(file_name)
        
        print(f"read the data of {len(player_data)} players")
        print()
        
        for player in player_data:
            self.__all_players.add_player(player)
        
        # Commands list
        self.help()
        
        while True: 
            print()
            command = input("command: ")
            
            # Search by name
            if command == "1": 
                name = input("name: ")
                search_by_name = self.__all_players.search_by_name(name)
                if search_by_name == None: 
                    print("No such player.")
                    continue
                print(search_by_name)
            # Teams
            elif command == "2":
                for team in self.__all_players.team_names_abbr(): 
                    print(team)
            # Countries
            elif command == "3":
                for country in self.__all_players.countries_abbr(): 
                    print(country)
            # List players in a specific team in the order of points scored
            elif command == "4": 
                team = input("team: ")
                ordered_players_team = self.__all_players.order_players_from_team(team)
                if ordered_players_team == None: 
                    print("No such team.")
                    continue
                for player in ordered_players_team: 
                    print(player)
            # List players from a specific country in the order of points scored
            elif command == "5": 
                country = input("country: ")
                ordered_players_country = self.__all_players.order_players_from_country(country)
                if ordered_players_country == None: 
                    print("This country does not participate in the NHL.")
                    continue
                for player in ordered_players_country: 
                    print(player)
            # List players with highest points
            elif command == "6": 
                num_of_players = int(input("how many: "))
                players = self.__all_players.players_with_most_points()
                for num in range(0, num_of_players, 1): 
                    print(players[num])
            # List players with most goals
            elif command == "7":
                num_of_players = int(input("how many: "))
                players = self.__all_players.players_with_most_goals()
                for num in range(0, num_of_players, 1): 
                    print(players[num])
            # ALL PLAYERS TEST COMMAND - REMOVE LATER
            elif command == "8": 
                for player in self.__all_players.all_players():
                    print(player)
                print("123456789012345678901234567890123456789")
            elif command == "0":
                break
            else: 
                print("Wrong command. Try again!")
                continue

def main():
    application = UserApplication()
    application.execute()
    
main()
# ------------------------------------

# # MODEL SOLUTION
# import json 
# class Statistics: 
#     def __init__(self, players: list): 
#         self.__players = players
    
#     def by_points(self, p): 
#         return p['goals'] + p['assists']
    
#     def by_goals(self, p): 
#         # if the number of goals is equal, less played games is better
#         return (p['goals'], -p['games'])
    
#     def player_data(self, name: str): 
#         for player in self.__players:
#             if player['name'] == name: 
#                 return player
#         return None
    
#     def countries(self): 
#         return sorted(list(set(p['nationality'] for p in self.__players))) 
    
#     def teams(self):
#         return sorted(list(set(p['team'] for p in self.__players)))
    
#     def players_in_team(self, team: str): 
#         players = [p for p in self.__players if p['team'] == team]
#         return sorted(players, key=self.by_points, reverse=True)
    
#     def players_from_country(self, country: str): 
#         players = [p for p in self.__players if p['nationality'] == country]
#         return sorted(players, key=self.by_points, reverse=True)
    
#     def most_points(self, num): 
#         players = sorted(self.__players, key=self.by_points, reverse=True)
#         return players[0: num]
    
#     def most_goals(self, num): 
#         players = sorted(self.__players, key=self.by_goals, reverse=True)
#         return players[0: num]

# class Application: 
#     def __init__(self):
#         self.__statistics = None
    
#     def instructions(self): 
#         instructions = """
#         commands:
#         0 quit
#         1 search for player
#         2 teams
#         3 countries
#         4 players in team
#         5 players from country
#         6 most points
#         7 most goals"""
#         print(instructions)
        
#     def f(self, p: dict): 
#         """
#             helper method, which creates a string out of players formatted for output
#         """
#         points = p['goals'] + p['assists']
#         return f"{p['name']:20} {p['team']}  {p['goals']:2} + {p['assists']:2} = {points:3}"
    
#     def read_file(self): 
#         file_name = input("file: ")
#         with open(file_name) as file: 
#             data = file.read()
        
#         players = json.loads(data)
#         print(f"read the data of {len(players)} players")
#         self.__statistics = Statistics(players)
        
#     def get_players(self): 
#         name = input("name: ")
#         player = self.__statistics.player_data(name)
#         if player: 
#             print(self.f(player))
    
#     def get_teams(self): 
#         for team in self.__statistics.teams():
#             print(team)
    
#     def get_countries(self): 
#         for country in self.__statistics.countries():
#             print(country)
            
#     def players_in_team(self):
#         team = input("team: ")
#         for player in self.__statistics.players_in_team(team): 
#             print(self.f(player))
    
#     def players_from_country(self):
#         country = input("country: ")
#         for player in self.__statistics.players_from_country(country): 
#             print(self.f(player))
    
#     def most_points(self): 
#         number = int(input("how many: "))
#         for player in self.__statistics.most_points(number): 
#             print(self.f(player))
            
#     def most_goals(self): 
#         number = int(input("how many: "))
#         for player in self.__statistics.most_goals(number): 
#             print(self.f(player))
    
#     def execute(self): 
#         self.read_file()
#         self.instructions()
#         while True: 
#             print()
#             command = input("command: ")
#             if command == "0":
#                 return
#             elif command == "1":
#                 self.get_playes()
#             elif command == "2":
#                 self.get_teams()
#             elif command == "3":
#                 self.get_countries()
#             elif command == "4":
#                 self.players_in_team()
#             elif command == "5":
#                 self.players_from_country()
#             elif command == "6":
#                 self.most_points()
#             elif command == "7":
#                 self.most_goals()