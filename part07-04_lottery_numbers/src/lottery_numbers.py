# Write your solution here
from random import randint

def lottery_numbers(amount: int, lower: int, upper: int): 
    listNum = []

    while len(listNum) < amount: 
        num = randint(lower + 1, upper - 1)
        if num not in listNum: 
            listNum.append(num)

    listNum = sorted(listNum)
    return listNum

if __name__ == "__main__": 

    for number in lottery_numbers(7, 1, 40):
        print(number)