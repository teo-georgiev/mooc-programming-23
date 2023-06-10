# Write your solution here
import string

def separate_characters(my_string: str): 
    ascii = ""
    punct = ""
    misc = ""

    for i in range(len(my_string)):
        if my_string[i] in string.ascii_letters: 
            ascii += my_string[i]
        elif my_string[i] in string.punctuation:
            punct += my_string[i]
        else: 
            misc += my_string[i]

    parts = (ascii,punct,misc)
    return parts

if __name__ == "__main__": 
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])
