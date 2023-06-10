# WRITE YOUR SOLUTION HERE:

# MODEL SOLUTION
# from string import punctuation

# def most_common_words(filename: str, lower_limit: int):
#     with open(filename) as f: 
#         content = f.read()

#         # remove line breaks and punctuation
#         for punctuation_mark in punctuation: 
#             content = content.replace(punctuation_mark, "")

#         words = content.split(" ")
#         return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

# MY SOLUTION
from string import punctuation

def most_common_words(filename: str, lower_limit: int): 
    with open(filename) as f:
        full_text = f.read()
        words_dict = {} 
        
        # for line in f: 
        #     line = line.replace("\n", "")
        #     parts = line.split(" ")
        #     full_text += parts
        #     full_text_string = " ".join(full_text)
        full_text = full_text.replace('\n', ' ')
        for char in punctuation: 
            full_text = full_text.replace(char, '')

        words = full_text.split(" ")

        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}
 
if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))