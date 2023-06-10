# Write your solution here
import string

def change_case(orig_string: str):
    changedStr = ""
    for letter in orig_string: 
        if letter in string.ascii_lowercase: 
            changedStr += letter.upper()
        elif letter in string.ascii_uppercase: 
            changedStr += letter.lower()
        else: 
            changedStr += letter
    
    return changedStr


def split_in_half(orig_string: str): 
    length = len(orig_string) // 2
    p1, p2 = orig_string[:length], orig_string[length:]
    
    return p1, p2

def remove_special_characters(orig_string: str):
    charSet = string.ascii_letters + string.digits + " "

    newStr = ""
    for letter in orig_string: 
        if letter in charSet: 
            newStr += letter
        else: continue
    
    return newStr
