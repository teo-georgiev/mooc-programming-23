# Write your solution here

# MODEL SOLUTION 
# from random import sample

# def roll(die: str): 
#     dices = {
#         "A": [3, 3, 3, 3, 3, 6],
#         "B": [2, 2, 2, 5, 5, 5],
#         "C": [1, 4, 4, 4, 4, 4]
#     }

#     return sample(dices[die], 1)[0]

# def play(die1: str, die2: str, times: int):
#     v1 = 0
#     v2 = 0
#     t = 0

#     for i in range(times): 
#         n1 = roll(die1)
#         n2 = roll(die2)
#         if n1 > n2: 
#             v1 += 1 
#         elif n1 < n2: 
#             v2 += 1
#         else: 
#             t += 1
    
#     return v1, v2, t

# MY SOLUTION
from random import choice

def roll(die: str): 
    if die == "A": 
        dieNums = [3, 3, 3, 3, 3, 6]
    elif die == "B": 
        dieNums = [2, 2, 2, 5, 5, 5]
    elif die == "C":
        dieNums = [1, 4, 4, 4, 4, 4]

    return choice(dieNums)

def play(die1: str, die2: str, times: int): 
    count = 0
    win1 = 0
    win2 = 0
    tie = 0
    
    while count < times: 
        # Check the value of the dice
        # Die 1 number
        roll1 = roll(die1)

        # Die 2 number 
        roll2 = roll(die2)
        
        # Compare dice
        if roll1 > roll2: 
            win1 += 1
        elif roll1 < roll2: 
            win2 += 1
        else: 
            tie += 1
        count += 1

    return (win1,win2,tie)
    
if __name__ == "__main__": 
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
    print()

    result = play("A", "C", 3)
    print(result)
    result = play("B", "B", 3)
    print(result)