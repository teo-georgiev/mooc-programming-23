# Write your solution here
def no_vowels(strPhrase: str):
    newString = ""

    for i in range(0, len(strPhrase), 1): 
        if strPhrase[i] == "a" or strPhrase[i] == "e" or strPhrase[i] == "i": 
            continue
        elif strPhrase[i] == "o" or strPhrase[i] == "u": 
            continue
        else: 
            newString = newString + strPhrase[i]
    
    return newString

if __name__ == "__main__": 
    my_string = "this is an example"
    print(no_vowels(my_string))
