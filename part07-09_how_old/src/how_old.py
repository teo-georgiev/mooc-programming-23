# Write your solution here
from datetime import datetime

if True: 
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
else: 
    day = 10
    month = 9
    year = 1979

millennium = datetime(1999, 12, 31)
birthdate = datetime(year, month, day)

if millennium < birthdate: 
    print("You weren't born yet on the eve of the new millennium.")
else:
    result = millennium - birthdate
    print(f"You were {result.days} days old on the eve of the new millennium.")