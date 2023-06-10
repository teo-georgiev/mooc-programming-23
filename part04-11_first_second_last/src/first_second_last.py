# Write your solution here

def first_word(sentence: str): 
    index = 0
    textFirst = ""

    while sentence[index] != " ": 
        textFirst += sentence[index]
        index += 1
    
    return textFirst

def second_word(sentence: str):
    index = 0
    textSecond = ""
    
    space = sentence.find(" ")
    sentence = sentence[space + 1 : ]

    if sentence.find(" ") == -1 : 
        textSecond = sentence
        return textSecond
    else: 
        while sentence[index] != " ": 
            textSecond += sentence[index]
            index += 1
    
    return textSecond

def last_word(sentence: str): 
    index = -1
    textLast = ""

    while sentence[index] != " ": 
        textLast = sentence[index] + textLast
        index -= 1

    #textLast = textLast[-1 : index]
    
    return textLast


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))