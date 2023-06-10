# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word) > len(player2_word): 
            return 1
        elif len(player1_word) < len(player2_word): 
            return 2
        else: 
            return 0

class MostVowels(WordGame): 
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def count_vowels(self, word: str): 
        vowels = "aeiouy"
        counter = 0
        for character in word: 
            if character in vowels: 
                counter += 1
        return vowels
    
    def round_winner(self, player1_word: str, player2_word: str):
        if self.count_vowels(player1_word) > self.count_vowels(player2_word): 
            return 1
        elif self.count_vowels(player2_word) > self.count_vowels(player1_word): 
            return 2
        else: 
            return 0

class RockPaperScissors(WordGame): 
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        choices = {
            "rock" : 0, 
            "paper" : 1, 
            "scissors" : 2
        }
        # Not good first
        if player1_word not in choices.keys() and player2_word not in choices.key(): 
            return 0
        
        if player1_word not in choices.keys(): 
            return 2 
        
        if player2_word not in choices.keys():
            return 1 

        # Use dictionary to calculate the difference between
        # choices. For example: player 1 selects paper, value is 1
        # player2 selects rock, value is 0
        # player 1 wins when the difference is 1 or -2
        # player 2 wins when the difference is -1 ot 2
        # 0 means that both selected the same choice

        difference = choices[player1_word] - choices[player2_word]

        if difference == 0: 
            return 0
        
        if difference == 1 or difference == -2: 
            return 1 
        
        return 2 

        # options = ["rock", "paper", "scissors"]

        # if player1_word == "rock" and player2_word == "paper":
        #     return 2 
        # elif player1_word == "rock" and player2_word == "scissors":
        #     return 1 
        # elif player1_word == "paper" and player2_word == "rock": 
        #     return 1
        # elif player1_word == "paper" and player2_word == "scissors": 
        #     return 2 
        # elif player1_word == "scissors" and player2_word == "paper": 
        #     return 1
        # elif player1_word == "scissors" and player2_word == "rock":
        #     return 2
        # elif player1_word not in options and player2_word in options: 
        #     return 2
        # elif player1_word in options and player2_word not in options: 
        #     return 1 
        # elif player1_word not in options and player2_word not in options: 
        #     pass
        # else: 
        #     pass

def main():
    p = RockPaperScissors(3)
    p.play()


if __name__ == "__main__": 
    main()
