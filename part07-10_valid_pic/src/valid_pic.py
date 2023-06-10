# Write your solution here
from datetime import datetime

def is_it_valid(pic: str): 
    if len(pic) != 11: 
        return False

    # Breaking down the first 6 characters into the birthdate 
    day = pic[0:2]
    if pic[2] == "0": 
        month = pic[3]
    else: 
        month = pic[2:4]
    if pic[6] == "-":
        year = "19" + pic[4:6]
    elif pic[6] == "+": 
        year = "18" + pic[4:6]
    elif pic[6] == "A":
        year = "20" + pic[4:6]

    day = int(day)
    month = int(month)
    year = int(year)
    
    # Checking if the birthdate is a valid date
    try: 
        birthdate = datetime(year, month, day)
    except ValueError: 
        return False
    
    # Checking if the birthdate is more than the current date
    today = datetime.now()
    if today < birthdate: 
        return False
    
    # Checking control character
    ctrlChar = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    pIdent = pic[7:10] # Personal identifier 

    charID = int(pic[0:6] + pIdent) % 31 
    if ctrlChar[charID] != pic[10]: 
        return False
    
    return True

if __name__ == "__main__": 
    print(is_it_valid("230827-906F"))
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))