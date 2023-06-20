# Write your solution here
import re

# # MODEL SOLUTION
# def is_dotw(my_string: str): 
#     return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None

# def all_vowels(my_string: str): 
#     return re.search("^[aeiou]*$", my_string) is not None

# def time_of_day(my_string: str):
#     return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None

# MY SOLUTION
def is_dotw(my_string: str): 
    if re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string):
        return True
    return False

def all_vowels(my_string: str): 
    if re.search("^[aeiou]*$", my_string):
        return True
    return False

def time_of_day(my_string: str): 
    parts = my_string.split(":")
    if re.search("[0-1][0-9]|2[0-3]", parts[0]):
        if re.search("[0-5][0-9]", parts[1]):
            if re.search("[0-5][0-9]", parts[2]):
                return True
    return False

def main(): 
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("25:13:01"))

if __name__ == "__main__": 
    main()