# Write your solution here
def no_shouting(wordList: list): 
    newList = []
    for item in wordList: 
        if item.isupper(): 
            continue
        else: 
            newList.append(item)

    return newList

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)