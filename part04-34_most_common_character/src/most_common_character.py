# Write your solution here
def most_common_character(word: str): 
    num = 0
    letter = ""

    for i in range(0, len(word) - 1, 1): 
        if word.count(word[i]) > num: 
            num = word.count(word[i])
            letter = word[i]
        else: 
            continue
    
    return letter

if __name__ == "__main__": 
    first_string = "abcdbde"
    print(most_common_character(first_string))

