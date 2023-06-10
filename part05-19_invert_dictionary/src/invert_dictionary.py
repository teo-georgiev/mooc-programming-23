# Write your solution here

def invert(dictionary: dict): 
    newDict = {}
    temp = ""
    for key in dictionary: 
        temp = dictionary[key]
        newDict[temp] = key
    dictionary.clear()
    for key in newDict: 
        dictionary[key] = newDict[key]

if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)
