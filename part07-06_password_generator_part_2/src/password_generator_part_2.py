# Write your solution here

# MODEL SOLUTION
from random import choice, randint
from string import ascii_lowercase, digits

def generate_strong_password (length: int, nums: bool, punct: bool):
    specialChars = "!?=+-()#"
    # One letter at the beginning of the password
    passwd = choice(ascii_lowercase)
    choice_set = ascii_lowercase

    # If numbers is wanted, add at least one number
    if nums: 
        passwd = add_character(passwd, digits)
        choice_set += digits
    
    # same for special characters 
    if punct: 
        passwd = add_character(passwd, specialChars)
        choice_set += specialChars
    
    # build the rest of the password from the whole set
    while (len(passwd) < length): 
        passwd = add_character(passwd, choice_set)

    return passwd

# Add a random character from the given set either
# at the beginning or the end of the string
def add_character(passwd: str, characters): 
    character = choice(characters)
    if randint(1,2) == 1: 
        return character + passwd
    else: 
        return passwd + character

# MY SOLUTION
# from string import ascii_lowercase, digits
# from random import sample
# def generate_strong_password(length: int, nums: bool, punct: bool):
#     characters = ascii_lowercase
#     specialChars = "!?=+-()#"
#     password = ""

#     if nums and punct:
#         characters += digits + specialChars
#         password = "".join(
#             sample(ascii_lowercase, 1) + 
#             sample(digits, 1) + 
#             sample(specialChars, 1) + 
#             sample(characters, length - 3)
#         )
#     elif nums: 
#         characters += digits
#         password = "".join(
#             sample(ascii_lowercase, 1) + 
#             sample(digits, 1) + 
#             sample(characters, length - 2)
#         )
#     elif punct: 
#         characters += specialChars
#         password = "".join(
#             sample(ascii_lowercase, 1) + 
#             sample(specialChars, 1) + 
#             sample(characters, length - 2)
#         )
#     else: 
#         password = "".join(
#             sample(ascii_lowercase, length)
#         )

#     password = "".join(sample(password, len(password)))
    
#     return password

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5, False, True))