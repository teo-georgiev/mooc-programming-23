# Write your solution here:

# MODEL SOLUTION
from random import choice

def word_generator(letters: str, length: int, amount: int):
    return ("".join([choice(letters) for i in range(length)]) for j in range(amount))

# # MY SOLUTION
# from random import choices

# def word_generator(characters: str, length: int, amount: int): 
#     for i in range(0, amount):
#         yield "".join(choices(characters, k = length))

if __name__ == "__main__":
    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen: 
        print(word)