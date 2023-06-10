# Write your solution here
def shortest(strList: list): 
    word = ""
    shortWord = strList[0]

    for i in range(0, len(strList), 1):
        wordPrev = word
        word = strList[i]

        if len(word) < len(wordPrev):
            shortWord = word
        else: 
            continue
    
    return shortWord

if __name__ == "__main__": 
    my_list = ["first", "second", "fourth", "eleventh"]

    result = shortest(my_list)
    print(result)
