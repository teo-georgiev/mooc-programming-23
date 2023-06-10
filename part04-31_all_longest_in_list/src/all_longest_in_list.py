
# Write your solution here
def all_the_longest(strList: list): 
    newList = []
    word = ""

    for item in strList: 
        if len(item) > len(word): 
            word = item
            newList = []
            newList.append(item)
        elif len(item) == len(word): 
            newList.append(item)
        else: 
            continue
    
    return newList

#    for name in strList: 
#        if newList == [] or len(name) > len(newList[0]): 
#            newList = [name]
#        elif len(name) == len(newList[0]): 
#            newList.append(name)


if __name__ == "__main__": 
    my_list = ['Alan', 'Grace', 'Steve', 'Kim', 'Susan']
    
    result = all_the_longest(my_list)
    print(result) 
