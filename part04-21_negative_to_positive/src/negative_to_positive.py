# Write your solution here
numPositive = int(input("Please type in a positive integer: "))

for i in range (numPositive * -1, numPositive + 1, 1): 
    if i != 0: 
        print(i)