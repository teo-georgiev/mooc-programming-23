# Write your solution here
def length_of_longest(stringList: list): 
    word = ""
    longWord = 0

    for i in range(0, len(stringList), 1): 
        wordPrev = word
        word = stringList[i]
        if len(word) >= longWord:
            longWord = len(word)
        else: 
            continue
    
    return longWord

if __name__ == "__main__": 
    my_list = ['Alan', 'Grace', 'Frances', 'Kim', 'Susan']

    result = length_of_longest(my_list)
    print(result)
