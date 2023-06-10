# Write your solution here
import string
from random import choice

def generate_password(length: int):
    password = ""
    while len(password) < length:  
        x = choice(string.ascii_lowercase)
        password += x
    return password

if __name__ == "__main__": 
    for i in range(10):
        print(generate_password(8))